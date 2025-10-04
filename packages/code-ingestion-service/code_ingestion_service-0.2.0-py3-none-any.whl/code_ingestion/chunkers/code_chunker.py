from typing import List

from ..analyzers.cst_analyzer import CSTAnalyzer
from ..chunking_strategies.base_strategy import BaseStrategy
from ..data_models.chunk_metadata import ChunkMetadata
from ..data_models.class_info import ClassInfo
from ..data_models.code_chunk import CodeChunk
from ..data_models.method_info import MethodInfo
from ..enums.chunk_type import ChunkType
from ..parsers.code_parser import CodeParser


class CodeChunker:
    """Main orchestrator for code chunking."""

    def __init__(self,
                 parser: CodeParser,
                 analyzer: CSTAnalyzer,
                 strategy: BaseStrategy):
        self.parser = parser
        self.analyzer = analyzer
        self.strategy = strategy

    def chunk_code(self,
                   source_code: str,
                   file_path: str = "",
                   repo_url: str = "") -> List[CodeChunk]:
        """Main method to chunk code based on the strategy."""
        tree = self.parser.parse(source_code)
        chunks = []

        # Single-pass CST extraction for optimal performance
        package, imports, classes = self.analyzer.extract_all_info(tree, source_code)
        file_name = file_path.split("/")[-1] if file_path else ""
        
        # Extract dependencies once for all chunks (safe operation)
        dependencies = self.analyzer.extract_dependencies(imports) if hasattr(self.analyzer, 'extract_dependencies') else []

        for class_info in classes:
            chunks.extend(self._process_class(
                class_info, source_code, package, imports, dependencies,
                file_path, file_name, repo_url
            ))

        return chunks

    def _process_class(self,
                       class_info: ClassInfo,
                       source_code: str,
                       package: str,
                       imports: List[str],
                       dependencies: List[str],
                       file_path: str,
                       file_name: str,
                       repo_url: str) -> List[CodeChunk]:
        """Process a single class and decide chunking strategy."""
        chunks = []

        # Method-level context caching: build base context once per class
        base_context = self._build_context(package, imports)
        class_wrapper_start = f"public class {class_info.name} {{\n    // class header\n    \n"
        class_wrapper_end = "\n}"

        if not self.strategy.should_split_class(class_info, source_code):
            chunk = self._create_complete_class_chunk(
                class_info, source_code, base_context, dependencies,
                file_path, file_name, repo_url
            )
            chunks.append(chunk)
        else:
            # Use size-based method grouping for cost optimization
            if hasattr(self.strategy, 'get_method_groups'):
                size_optimized_groups = self.strategy.get_method_groups(class_info, source_code)
                for group in size_optimized_groups:
                    group_chunk = self._create_method_group_chunk(
                        class_info, group, source_code, base_context, class_wrapper_start, class_wrapper_end,
                        file_path, file_name, repo_url
                    )
                    chunks.append(group_chunk)
            else:
                # Fallback to individual method chunks (legacy behavior)
                method_chunks = self._create_method_chunks(
                    class_info, source_code, base_context, class_wrapper_start, class_wrapper_end,
                    file_path, file_name, repo_url
                )
                chunks.extend(method_chunks)

        return chunks

    def _create_complete_class_chunk(self,
                                     class_info: ClassInfo,
                                     source_code: str,
                                     base_context: str,
                                     dependencies: List[str],
                                     file_path: str,
                                     file_name: str,
                                     repo_url: str) -> CodeChunk:
        """Create a complete class chunk."""
        class_content = self.parser.extract_text(class_info.node, source_code)
        full_content = base_context + class_content

        # Optimize content for embedding efficiency
        if hasattr(self.strategy, 'optimize_chunk_content'):
            full_content = self.strategy.optimize_chunk_content(full_content)

        # Compute API path for class-level chunks
        class_api_path = self.analyzer._extract_class_base_path(class_info.annotations)
        
        metadata = ChunkMetadata(
            repo_url=repo_url,
            file_path=file_path,
            file_name=file_name,
            class_name=class_info.name,
            methods=[method.name for method in class_info.methods],
            fields=class_info.fields,
            chunk_type=ChunkType.COMPLETE_CLASS.value,
            chunk_size=len(full_content),
            start_line=class_info.start_line,
            end_line=class_info.end_line,
            language=self.parser.language.value,
            annotations=class_info.annotations,
            class_annotations=class_info.annotations,  # For class chunks, same as annotations
            framework_type=class_info.framework_type,
            is_rest_controller=self.analyzer.is_rest_api(class_info.annotations),
            http_methods=[m.http_method for m in class_info.methods if m.http_method],
            api_path=class_api_path,
            parent_chunk_id=None,  # Complete class chunks are top-level (no parent)
            dependencies=dependencies  # Add extracted dependencies
        )

        chunk_id = self._create_chunk_id(file_path, class_info.name)
        return CodeChunk(id=chunk_id, content=full_content, metadata=metadata)

    def _create_method_chunks(self,
                              class_info: ClassInfo,
                              source_code: str,
                              base_context: str,
                              class_wrapper_start: str,
                              class_wrapper_end: str,
                              file_path: str,
                              file_name: str,
                              repo_url: str) -> List[CodeChunk]:
        """Create method-level chunks."""
        chunks = []

        for method_info in class_info.methods:
            chunk = self._create_method_chunk(
                class_info, method_info, class_info.name, source_code, base_context, class_wrapper_start, class_wrapper_end,
                file_path, file_name, repo_url, ChunkType.METHOD
            )
            chunks.append(chunk)

        for constructor_info in class_info.constructors:
            chunk = self._create_method_chunk(class_info,
                constructor_info, class_info.name, source_code, base_context, class_wrapper_start, class_wrapper_end,
                file_path, file_name, repo_url, ChunkType.CONSTRUCTOR
            )
            chunks.append(chunk)

        return chunks

    def _create_method_chunk(self,
                             class_info: ClassInfo,
                             method_info: MethodInfo,
                             class_name: str,
                             source_code: str,
                             base_context: str,
                             class_wrapper_start: str,
                             class_wrapper_end: str,
                             file_path: str,
                             file_name: str,
                             repo_url: str,
                             chunk_type: ChunkType) -> CodeChunk:
        """Create a chunk for a single method."""
        method_content = self.parser.extract_text(method_info.node, source_code)

        # Use cached context parts to build method context efficiently
        indented_method = "    " + method_content.replace("\n", "\n    ")
        context = base_context + class_wrapper_start + indented_method + class_wrapper_end
        
        # Optimize content for embedding efficiency
        if hasattr(self.strategy, 'optimize_chunk_content'):
            context = self.strategy.optimize_chunk_content(context)

        # Combine class and method annotations for REST API detection
        all_annotations = class_info.annotations + method_info.annotations
        
        # Compute full API path (class base path + method path)
        full_api_path = self.analyzer._compute_full_api_path(class_info.annotations, method_info.api_path)
        
        metadata = ChunkMetadata(
            repo_url=repo_url,
            file_path=file_path,
            file_name=file_name,
            class_name=class_name,
            method_name=method_info.name,
            signature=method_info.signature,
            return_type=method_info.return_type,
            chunk_type=chunk_type.value,
            chunk_size=len(context),
            start_line=method_info.start_line,
            end_line=method_info.end_line,
            language=self.parser.language.value,
            annotations=method_info.annotations,  # Method annotations
            class_annotations=class_info.annotations,  # Class annotations for context
            framework_type=class_info.framework_type,
            is_rest_controller=self.analyzer.is_rest_api(all_annotations),  # Check both!
            http_methods=[method_info.http_method] if method_info.http_method else [],
            api_path=full_api_path,  # Full combined path
            parent_chunk_id=f"class:{class_name}"  # Method chunks belong to their class
        )

        chunk_id = self._create_chunk_id(file_path, class_name, method_info.name)
        return CodeChunk(id=chunk_id, content=context, metadata=metadata)

    def _create_method_group_chunk(self,
                                   class_info: ClassInfo,
                                   method_group: List[MethodInfo],
                                   source_code: str,
                                   base_context: str,
                                   class_wrapper_start: str,
                                   class_wrapper_end: str,
                                   file_path: str,
                                   file_name: str,
                                   repo_url: str) -> CodeChunk:
        """Create a chunk containing multiple methods grouped by size optimization."""
        # Build chunk content
        context = self._build_method_group_content(
            method_group, source_code, base_context, class_wrapper_start, class_wrapper_end
        )
        
        # Build chunk metadata
        metadata = self._build_method_group_metadata(
            class_info, method_group, context, file_path, file_name, repo_url
        )
        
        # Create chunk ID for internal use 
        chunk_id_suffix = f"group_{'_'.join([m.name for m in method_group[:3]])}" if len(method_group) > 1 else method_group[0].name
        chunk_id = self._create_chunk_id(file_path, class_info.name, chunk_id_suffix)
        return CodeChunk(id=chunk_id, content=context, metadata=metadata)

    def _build_method_group_content(self,
                                    method_group: List[MethodInfo],
                                    source_code: str,
                                    base_context: str,
                                    class_wrapper_start: str,
                                    class_wrapper_end: str) -> str:
        """Build content for method group chunk."""
        method_contents = []
        for i, method_info in enumerate(method_group):
            method_content = self.parser.extract_text(method_info.node, source_code)
            indented_method = "    " + method_content.replace("\n", "\n    ")
            
            # Add separator for clarity
            if i > 0:
                indented_method = "    // --- Method " + str(i + 1) + " ---\n" + indented_method
            
            method_contents.append(indented_method)
        
        combined_methods = "\n\n".join(method_contents)
        context = base_context + class_wrapper_start + combined_methods + class_wrapper_end
        
        # Apply content optimization if available
        if hasattr(self.strategy, 'optimize_chunk_content'):
            context = self.strategy.optimize_chunk_content(context)
            
        return context

    def _build_method_group_metadata(self,
                                     class_info: ClassInfo,
                                     method_group: List[MethodInfo],
                                     context: str,
                                     file_path: str,
                                     file_name: str,
                                     repo_url: str) -> ChunkMetadata:
        """Build metadata for method group chunk."""
        # Extract method information
        method_analysis = self._analyze_method_group(class_info, method_group)
        
        # Create chunk identifier for internal use (not shown to LLM)
        group_name = f"group_{'_'.join(method_analysis['method_names'][:3])}" if len(method_analysis['method_names']) > 1 else method_analysis['method_names'][0]
        
        # For single method groups, use the actual method name
        # For multi-method groups, don't set method_name (let it be None/excluded)
        method_name = method_analysis['method_names'][0] if len(method_analysis['method_names']) == 1 else None
        
        return ChunkMetadata(
            repo_url=repo_url,
            file_path=file_path,
            file_name=file_name,
            class_name=class_info.name,
            method_name=method_name,
            signature=f"Method group ({len(method_analysis['method_names'])} methods): {', '.join(method_analysis['method_names'])}",
            return_type=f"Multiple methods: {', '.join([m.return_type or 'void' for m in method_group])}",
            chunk_type=ChunkType.METHOD.value,
            chunk_size=len(context),
            start_line=method_group[0].start_line,
            end_line=method_group[-1].end_line,
            language=self.parser.language.value,
            annotations=method_analysis['all_method_annotations'],
            class_annotations=class_info.annotations,
            framework_type=class_info.framework_type,
            is_rest_controller=self.analyzer.is_rest_api(class_info.annotations + method_analysis['all_method_annotations']),
            http_methods=list(set(method_analysis['all_http_methods'])),
            api_path=method_analysis['final_api_path'],
            methods=method_analysis['method_names'],
            parent_chunk_id=f"class:{class_info.name}"  # Method groups belong to their class
        )

    def _analyze_method_group(self, class_info: ClassInfo, method_group: List[MethodInfo]) -> dict:
        """Analyze method group to extract consolidated information."""
        all_method_annotations = []
        all_http_methods = []
        api_paths = []
        method_names = []
        
        for method_info in method_group:
            all_method_annotations.extend(method_info.annotations)
            method_names.append(method_info.name)
            
            if method_info.http_method:
                all_http_methods.append(method_info.http_method)
            
            # Compute API path for this method
            full_api_path = self._compute_method_api_path(class_info, method_info)
            if full_api_path and full_api_path != "/":
                api_paths.append(f"{method_info.http_method or 'METHOD'} {full_api_path}")
        
        # Determine final API path representation
        final_api_path = self._consolidate_api_paths(api_paths)
        
        return {
            'all_method_annotations': all_method_annotations,
            'all_http_methods': all_http_methods,
            'api_paths': api_paths,
            'method_names': method_names,
            'final_api_path': final_api_path
        }

    def _compute_method_api_path(self, class_info: ClassInfo, method_info: MethodInfo) -> str:
        """Compute full API path for a single method."""
        if method_info.api_path:
            return method_info.api_path
        return self.analyzer._compute_full_api_path(class_info.annotations, method_info.api_path)

    def _consolidate_api_paths(self, api_paths: List[str]) -> str:
        """Consolidate multiple API paths into a single representation."""
        if len(set(api_paths)) == 1:
            return api_paths[0].split(' ', 1)[1] if api_paths else None
        elif len(api_paths) > 1:
            return f"Multiple: {', '.join(api_paths)}"
        return None

    def _build_context(self, package: str, imports: List[str]) -> str:
        """Build package and import context."""
        context = ""
        if package:
            context += package + "\n"
        if imports:
            context += "\n".join(imports) + "\n\n"
        return context

    def _create_chunk_id(self, file_path: str, class_name: str, method_name: str = None) -> str:
        """Create a unique chunk ID."""
        parts = [file_path.replace("/", ":")]
        if class_name:
            parts.append(class_name)
        if method_name:
            parts.append(method_name)
        return ":".join(parts)
