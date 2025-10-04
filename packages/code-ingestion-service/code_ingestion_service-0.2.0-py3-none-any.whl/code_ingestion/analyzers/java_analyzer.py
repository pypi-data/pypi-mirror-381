from typing import List, Tuple, Optional, Dict

from tree_sitter import Tree, Node

from ..analyzers.cst_analyzer import CSTAnalyzer
from ..analyzers.java_cst_types import JavaNodeTypes
from ..data_models.class_info import ClassInfo
from ..data_models.method_info import MethodInfo


class JavaCSTAnalyzer(CSTAnalyzer):
    """Java-specific CST analyzer."""
    
    # Configuration for path parameter extraction (easy to extend)
    PATH_PARAMETER_NAMES = [
        None,       # No key (single string literal) - @RequestMapping("/api")
        "value",    # Most common - @RequestMapping(value="/api")
        "path",     # Also valid - @RequestMapping(path="/api")
    ]
    
    # HTTP method mappings for Spring Boot annotations
    METHOD_MAPPINGS = {
        "@GetMapping": "GET",
        "@PostMapping": "POST", 
        "@PutMapping": "PUT",
        "@DeleteMapping": "DELETE",
        "@PatchMapping": "PATCH"
    }
    
    # Pre-compiled regex patterns (initialized once, reused many times)
    import re
    PATH_EXTRACTION_PATTERNS = [
        re.compile(r'@\w+\s*\(\s*"([^"]*)"'),                    # @RequestMapping("/api")
        re.compile(r'value\s*=\s*"([^"]*)"'),                     # value="/api"  
        re.compile(r'path\s*=\s*"([^"]*)"'),                      # path="/api"
        re.compile(r'@\w+\s*\(\s*value\s*=\s*"([^"]*)"'),        # @RequestMapping(value="/api")
    ]

    def extract_classes(self, tree: Tree, source_code: str) -> List[ClassInfo]:
        """Extract Java class information from CST."""
        classes = []
        current_annotations = []

        # Simple pass: collect annotations and apply them to the next class
        for node in tree.root_node.children:
            if node.type in [JavaNodeTypes.ANNOTATION, JavaNodeTypes.MARKER_ANNOTATION]:
                annotation_text = self.parser.extract_text(node, source_code)
                current_annotations.append(annotation_text)
            elif node.type == JavaNodeTypes.CLASS_DECLARATION:
                class_info = self._analyze_class(node, source_code, current_annotations)
                if class_info:
                    classes.append(class_info)
                current_annotations = []  # Reset for next class

        return classes

    def _analyze_class(self, class_node: Node, source_code: str, preceding_annotations: List[str] = None) -> Optional[ClassInfo]:
        """Analyze a single class node."""
        class_name = None
        methods = []
        fields = []
        constructors = []
        annotations = preceding_annotations or []  # Use preceding annotations from extract_classes

        # Extract class name and any additional annotations from modifiers or direct annotations
        for child in class_node.children:
            if child.type == JavaNodeTypes.IDENTIFIER:
                class_name = self.parser.extract_text(child, source_code)
            elif child.type == JavaNodeTypes.MODIFIERS:
                # Combine with any annotations found in modifiers
                modifier_annotations = self._extract_annotations_from_modifiers(child, source_code)
                annotations.extend(modifier_annotations)
            elif child.type in [JavaNodeTypes.ANNOTATION, JavaNodeTypes.MARKER_ANNOTATION]:  # Direct annotation nodes
                annotation_text = self.parser.extract_text(child, source_code)
                annotations.append(annotation_text.strip())

        if not class_name:
            return None

        # Extract class body (your existing logic - unchanged)
        for child in class_node.children:
            if child.type == JavaNodeTypes.CLASS_BODY:
                for member in child.children:
                    if member.type == JavaNodeTypes.METHOD_DECLARATION:
                        method_info = self._extract_method_info(member, source_code)
                        if method_info:
                            methods.append(method_info)
                    elif member.type == JavaNodeTypes.CONSTRUCTOR_DECLARATION:
                        constructor_info = self._extract_constructor_info(member, source_code, class_name)
                        if constructor_info:
                            constructors.append(constructor_info)
                    elif member.type == JavaNodeTypes.FIELD_DECLARATION:
                        field_names = self._extract_field_names(member, source_code)
                        fields.extend(field_names)

        start_line, end_line = self.parser.get_line_numbers(class_node)
        framework_type = self._detect_framework_type(annotations)  # NEW

        # NEW: Class-level path processing
        class_base_path = self._extract_class_base_path(annotations)
        if class_base_path:
            methods = self._enrich_methods_with_base_path(methods, class_base_path)

        return ClassInfo(
            name=class_name,
            modifiers=[],
            methods=methods,
            fields=fields,
            constructors=constructors,
            start_line=start_line,
            end_line=end_line,
            node=class_node,
            annotations=annotations,  # NEW
            framework_type=framework_type  # NEW
        )

    def _extract_modifiers(self, modifiers_node: Node, source_code: str) -> List[str]:
        """Extract modifiers from a modifiers node."""
        modifiers = []
        for child in modifiers_node.children:
            if child.type in JavaNodeTypes.ALL_MODIFIERS:
                modifiers.append(child.type)
        return modifiers

    def _extract_method_info(self, method_node: Node, source_code: str) -> Optional[MethodInfo]:
        """Extract method information."""
        name = None
        return_type = None
        annotations = []

        # Extract components - check for both MODIFIERS and direct ANNOTATION nodes
        for child in method_node.children:
            if child.type == JavaNodeTypes.IDENTIFIER:
                name = self.parser.extract_text(child, source_code)
            elif child.type in JavaNodeTypes.RETURN_TYPES:
                return_type = self.parser.extract_text(child, source_code)
            elif child.type == JavaNodeTypes.MODIFIERS:
                found_annotations = self._extract_annotations_from_modifiers(child, source_code)
                annotations.extend(found_annotations)
            elif child.type in [JavaNodeTypes.ANNOTATION, JavaNodeTypes.MARKER_ANNOTATION]:  # Direct annotation nodes
                annotation_text = self.parser.extract_text(child, source_code)
                annotations.append(annotation_text.strip())

        if not name:
            return None

        signature = self.parser.extract_text(method_node, source_code).split("{")[0].strip()
        start_line, end_line = self.parser.get_line_numbers(method_node)
        http_method, api_path = self._analyze_rest_annotations(annotations)  # NEW

        return MethodInfo(
            name=name,
            signature=signature,
            return_type=return_type,
            node=method_node,
            start_line=start_line,
            end_line=end_line,
            annotations=annotations,  # NEW
            http_method=http_method,  # NEW
            api_path=api_path  # NEW
        )

    def _extract_constructor_info(self, constructor_node: Node, source_code: str, class_name: str) -> Optional[
        MethodInfo]:
        """Extract constructor information."""
        signature = self.parser.extract_text(constructor_node, source_code).split("{")[0].strip()
        start_line, end_line = self.parser.get_line_numbers(constructor_node)

        return MethodInfo(
            name=class_name,
            signature=signature,
            return_type=None,
            node=constructor_node,
            start_line=start_line,
            end_line=end_line
        )

    def _extract_parameters(self, params_node: Node, source_code: str) -> List[Dict[str, str]]:
        """Extract parameter information."""
        parameters = []
        for child in params_node.children:
            if child.type == JavaNodeTypes.FORMAL_PARAMETER:
                param_info = {"type": None, "name": None}
                for param_child in child.children:
                    if param_child.type in JavaNodeTypes.PARAMETER_TYPES:  # ← Use your constant!
                        param_info["type"] = self.parser.extract_text(param_child, source_code)
                    elif param_child.type == JavaNodeTypes.IDENTIFIER:
                        param_info["name"] = self.parser.extract_text(param_child, source_code)
                parameters.append(param_info)
        return parameters

    def _extract_field_names(self, field_node: Node, source_code: str) -> List[str]:
        """Extract field names from a field declaration."""
        field_names = []
        for child in field_node.children:
            if child.type == JavaNodeTypes.VARIABLE_DECLARATOR:
                for var_child in child.children:
                    if var_child.type == JavaNodeTypes.IDENTIFIER:
                        field_names.append(self.parser.extract_text(var_child, source_code))
        return field_names

    def extract_package_and_imports(self, tree: Tree, source_code: str) -> Tuple[str, List[str]]:
        """Extract package declaration and imports."""
        package = None
        imports = []

        for node in tree.root_node.children:
            if node.type == JavaNodeTypes.PACKAGE_DECLARATION:
                package = self.parser.extract_text(node, source_code)
            elif node.type == JavaNodeTypes.IMPORT_DECLARATION:
                imports.append(self.parser.extract_text(node, source_code))

        return package, imports

    def extract_all_info(self, tree: Tree, source_code: str) -> Tuple[str, List[str], List[ClassInfo]]:
        """
        Single-pass CST extraction for optimal performance.
        Extracts package, imports, and classes in one traversal.
        """
        package = None
        imports = []
        classes = []

        # Single traversal of root level nodes
        for node in tree.root_node.children:
            if node.type == JavaNodeTypes.PACKAGE_DECLARATION:
                package = self.parser.extract_text(node, source_code)
            elif node.type == JavaNodeTypes.IMPORT_DECLARATION:
                imports.append(self.parser.extract_text(node, source_code))
            elif node.type == JavaNodeTypes.CLASS_DECLARATION:
                class_info = self._analyze_class(node, source_code)
                if class_info:
                    classes.append(class_info)

        return package, imports, classes

    def _extract_annotations_from_modifiers(self, modifiers_node: Node, source_code: str) -> List[str]:
        """Extract annotations from a modifiers node."""
        annotations = []
        for child in modifiers_node.children:
            if child.type in [JavaNodeTypes.ANNOTATION, JavaNodeTypes.MARKER_ANNOTATION]:
                annotation_text = self.parser.extract_text(child, source_code)
                annotations.append(annotation_text.strip())
        return annotations


    def _analyze_rest_annotations(self, annotations: List[str]) -> Tuple[Optional[str], Optional[str]]:
        """Analyze REST annotations for HTTP method and path"""
        http_method = None
        api_path = None

        for annotation in annotations:
            # Check for direct method mappings
            for annotation_type, method in self.METHOD_MAPPINGS.items():
                if annotation_type in annotation:
                    http_method = method
                    api_path = self._extract_path_from_mapping(annotation)
                    break

            # Special handling for @RequestMapping
            if "@RequestMapping" in annotation:
                if "GET" in annotation or "RequestMethod.GET" in annotation:
                    http_method = "GET"
                elif "POST" in annotation or "RequestMethod.POST" in annotation:
                    http_method = "POST"
                api_path = self._extract_path_from_mapping(annotation)

            # Extract path from @Path (JAX-RS)
            elif "@Path" in annotation:
                api_path = self._extract_path_from_mapping(annotation)

        return http_method, api_path
    
    def _extract_annotation_parameter(self, annotation_node: Node, param_name: Optional[str] = None) -> Optional[str]:
        """Extract parameter value from annotation CST node.
        
        Args:
            annotation_node: The annotation CST node
            param_name: Parameter name to extract (None for single string literal)
            
        Returns:
            The parameter value or None if not found
        """
        # Find annotation_argument_list
        for child in annotation_node.children:
            if child.type == "annotation_argument_list":
                return self._extract_from_argument_list(child, param_name)
        return None
    
    def _extract_from_argument_list(self, arg_list_node: Node, param_name: Optional[str]) -> Optional[str]:
        """Extract value from annotation argument list."""
        for child in arg_list_node.children:
            if child.type == "element_value_pair":
                # Named parameter: name = "value"
                if param_name:
                    param_value = self._extract_from_value_pair(child, param_name)
                    if param_value:
                        return param_value
            elif child.type == "string_literal" and param_name is None:
                # Single string literal (default value parameter)
                return self._extract_string_value(child)
        return None
    
    def _extract_from_value_pair(self, pair_node: Node, target_param: str) -> Optional[str]:
        """Extract value from element_value_pair if parameter name matches."""
        param_name = None
        param_value = None
        
        for child in pair_node.children:
            if child.type == "identifier":
                param_name = self.parser.extract_text(child, "").strip()
            elif child.type == "string_literal":
                param_value = self._extract_string_value(child)
        
        return param_value if param_name == target_param else None
    
    def _extract_string_value(self, string_literal_node: Node) -> Optional[str]:
        """Extract the actual string value from string_literal node."""
        for child in string_literal_node.children:
            if child.type == "string_fragment":
                return self.parser.extract_text(child, "").strip()
        return None

    def _detect_framework_type(self, annotations: List[str]) -> Optional[str]:
        """Detect framework type from class annotations"""
        for annotation in annotations:
            if any(spring_annotation in annotation for spring_annotation in 
                   ["@RestController", "@Controller", "@Service", "@Repository", "@Component"]):
                return "spring-boot"
            elif "@Path" in annotation:
                return "jax-rs"
        return None

    def _compute_full_api_path(self, class_annotations: List[str], method_api_path: Optional[str]) -> str:
        """Compute full API path by combining class @RequestMapping with method path."""
        # Extract base path from class annotations (legacy string-based for now)
        class_base_path = self._extract_class_base_path(class_annotations)
        
        # Always return a path, never null
        return self._combine_paths(class_base_path or "", method_api_path or "")
    
    
    
    def _extract_path_from_annotation_cst(self, annotation_node: Node) -> Optional[str]:
        """Extract path value from annotation CST node using priority-based parameter search."""
        for param_name in self.PATH_PARAMETER_NAMES:
            path_value = self._extract_annotation_parameter(annotation_node, param_name)
            if path_value:
                return path_value
        return None
    
    def _get_annotation_name(self, annotation_node: Node) -> Optional[str]:
        """Extract annotation name from CST node."""
        for child in annotation_node.children:
            if child.type == "identifier":
                return self.parser.extract_text(child, "").strip()
        return None
    
    def _combine_paths(self, base_path: str, method_path: str) -> str:
        """Combine base and method paths, ensuring proper format."""
        # Clean up paths
        base = base_path.strip().strip('/') if base_path else ""
        method = method_path.strip().strip('/') if method_path else ""
        
        # Build combined path
        if base and method:
            return f"/{base}/{method}"
        elif base:
            return f"/{base}"
        elif method:
            return f"/{method}"
        else:
            return "/"  # Default root path instead of null

    def _analyze_rest_annotations(self, annotations: List[str]) -> Tuple[Optional[str], Optional[str]]:
        """Analyze REST annotations for HTTP method and path"""
        http_method = None
        api_path = None

        for annotation in annotations:
            # Check for direct method mappings
            for annotation_type, method in self.METHOD_MAPPINGS.items():
                if annotation_type in annotation:
                    http_method = method
                    api_path = self._extract_path_from_mapping(annotation)
                    break

            # Special handling for @RequestMapping
            if "@RequestMapping" in annotation:
                if "GET" in annotation or "RequestMethod.GET" in annotation:
                    http_method = "GET"
                elif "POST" in annotation or "RequestMethod.POST" in annotation:
                    http_method = "POST"
                api_path = self._extract_path_from_mapping(annotation)

            # Extract path from @Path (JAX-RS)
            elif "@Path" in annotation:
                api_path = self._extract_path_from_mapping(annotation)

        return http_method, api_path

    def _extract_class_base_path(self, class_annotations: List[str]) -> Optional[str]:
        """Extract base path from class-level @RequestMapping"""
        for annotation in class_annotations:
            if "@RequestMapping" in annotation:
                return self._extract_path_from_annotation_string(annotation)
        return None

    def _extract_path_from_annotation_string(self, annotation: str) -> Optional[str]:
        """Extract path value from annotation string using pre-compiled patterns."""
        for pattern in self.PATH_EXTRACTION_PATTERNS:
            match = pattern.search(annotation)
            if match:
                return match.group(1)
        return None

    def _extract_path_from_mapping(self, annotation: str) -> Optional[str]:
        """Extract path from mapping annotation using pre-compiled patterns."""
        return self._extract_path_from_annotation_string(annotation)

    def _enrich_methods_with_base_path(self, methods: List[MethodInfo], class_base_path: str) -> List[MethodInfo]:
        """Combine class base path with method paths"""
        for method in methods:
            if method.api_path:
                method.api_path = self._combine_paths(class_base_path, method.api_path)
            elif method.http_method:
                method.api_path = class_base_path
        return methods

    def extract_dependencies(self, imports: List[str]) -> List[str]:
        """Extract class dependencies from imports with safe fallback."""
        try:
            dependencies = []
            for import_line in imports:
                # Extract class name from import statement
                # e.g., "import com.example.service.UserService;" -> "UserService"
                if 'import ' in import_line and ';' in import_line:
                    # Remove 'import ' and ';', then get last part after '.'
                    class_path = import_line.replace('import ', '').replace(';', '').strip()
                    if '.' in class_path:
                        class_name = class_path.split('.')[-1]
                        # Filter out common framework imports that don't add value
                        if not self._is_framework_import(class_path):
                            dependencies.append(class_name)
            return dependencies
        except Exception as e:
            print(f"Warning: Dependency extraction failed: {e}")
            return []  # Safe fallback

    def _is_framework_import(self, import_path: str) -> bool:
        """Filter out common framework imports that don't add RAG value."""
        framework_prefixes = [
            'java.',
            'javax.',
            'org.springframework.',
            'org.junit.',
            'com.fasterxml.jackson.',
            'io.swagger.',
            'lombok.',
        ]
        return any(import_path.startswith(prefix) for prefix in framework_prefixes)

