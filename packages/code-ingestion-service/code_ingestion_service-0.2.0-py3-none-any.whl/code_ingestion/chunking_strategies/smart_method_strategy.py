import re
from typing import List, Dict, Tuple
from ..chunking_strategies.base_strategy import BaseStrategy
from ..data_models.class_info import ClassInfo
from ..data_models.method_info import MethodInfo


class SmartMethodStrategy(BaseStrategy):
    """Smart method grouping strategy for cost-effective chunking."""

    # Pre-compiled regex patterns for whitespace compression
    NEWLINE_PATTERN = re.compile(r'\n\s*\n\s*\n')  # Max 2 consecutive newlines
    SPACE_PATTERN = re.compile(r'[ \t]+')           # Multiple spaces to single
    LEADING_SPACE_PATTERN = re.compile(r'^\s+', re.MULTILINE)  # Remove leading spaces

    def __init__(self, 
                 min_chunk_size: int = 500,    # Minimum viable chunk size
                 max_chunk_size: int = 2000,   # Maximum chunk size before splitting
                 max_class_size: int = 3000):  # Complete class threshold
        self.min_chunk_size = min_chunk_size
        self.max_chunk_size = max_chunk_size
        self.max_class_size = max_class_size

    def should_split_class(self, class_info: ClassInfo, source_code: str) -> bool:
        """Decide whether to split class into method chunks."""
        class_text = source_code[class_info.node.start_byte:class_info.node.end_byte]
        class_size = len(self._compress_whitespace(class_text))
        
        # If class is small enough, keep it complete
        if class_size <= self.max_class_size:
            return False
            
        # Simple size check - if class too big, we'll use size-based grouping
        return True

    def get_method_groups(self, class_info: ClassInfo, source_code: str) -> List[List[MethodInfo]]:
        """Get size-optimized method groups (backward compatibility)."""
        return self.get_size_based_method_groups(class_info, source_code)

    def get_size_based_method_groups(self, class_info: ClassInfo, source_code: str) -> List[List[MethodInfo]]:
        """Get size-optimized method groups using simple bin packing."""
        if not self.should_split_class(class_info, source_code):
            return []  # Use complete class chunking
            
        all_methods = class_info.methods + class_info.constructors
        
        # Calculate method sizes for size-based grouping
        method_sizes = []
        for method in all_methods:
            method_text = source_code[method.node.start_byte:method.node.end_byte]
            method_size = len(self._compress_whitespace(method_text))
            method_sizes.append((method, method_size))
        
        # Handle oversized methods
        oversized_methods = [(m, s) for m, s in method_sizes if s > self.max_chunk_size]
        if oversized_methods:
            print(f"Warning: {len(oversized_methods)} methods exceed max_chunk_size ({self.max_chunk_size})")
            
        # Use size-based bin packing (no relationship logic)
        return self._size_based_bin_packing(method_sizes)
    
    def _size_based_bin_packing(self, method_sizes: List[Tuple]) -> List[List[MethodInfo]]:
        """Size-based bin packing to minimize chunk count while respecting size constraints."""
        groups = []
        remaining_methods = method_sizes.copy()
        
        while remaining_methods:
            # Find the best combination for current chunk
            best_group = self._find_best_group(remaining_methods)
            
            if not best_group:
                # Fallback: take the first method if no valid group found
                best_group = [remaining_methods[0]]
            
            # Add group and remove methods from remaining
            groups.append([method for method, size in best_group])
            for method, size in best_group:
                remaining_methods.remove((method, size))
        
        # Filter out groups that don't meet minimum size (unless single large method)
        valid_groups = []
        for group in groups:
            group_size = sum(size for method, size in method_sizes if method in group)
            if group_size >= self.min_chunk_size or len(group) == 1:
                valid_groups.append(group)
            else:
                # Try to merge small group with previous group
                if valid_groups and len(valid_groups[-1]) < 3:  # Don't over-pack
                    prev_group_size = sum(size for method, size in method_sizes if method in valid_groups[-1])
                    if prev_group_size + group_size <= self.max_chunk_size:
                        valid_groups[-1].extend(group)
                    else:
                        valid_groups.append(group)  # Keep as separate small group
                else:
                    valid_groups.append(group)  # Keep as separate small group
        
        return valid_groups
    
    def _find_best_group(self, remaining_methods: List[Tuple]) -> List[Tuple]:
        """Find the best size-based combination of methods for a single chunk."""
        best_group = []
        best_size = 0
        
        # Try different starting methods, pack as efficiently as possible
        for i in range(len(remaining_methods)):
            current_group = [remaining_methods[i]]
            current_size = remaining_methods[i][1]
            
            # Add more methods to maximize space usage (size-based only)
            for j in range(len(remaining_methods)):
                if i == j:
                    continue
                    
                method, size = remaining_methods[j]
                if current_size + size <= self.max_chunk_size:
                    current_group.append((method, size))
                    current_size += size
            
            # Select group with best space utilization
            if (self.min_chunk_size <= current_size <= self.max_chunk_size and
                current_size > best_size):
                best_group = current_group
                best_size = current_size
        
        return best_group


    def _compress_whitespace(self, text: str) -> str:
        """Compress unnecessary whitespace while preserving structure."""
        # Use pre-compiled patterns for better performance
        compressed = self.NEWLINE_PATTERN.sub('\n\n', text)      # Max 2 consecutive newlines
        compressed = self.SPACE_PATTERN.sub(' ', compressed)     # Multiple spaces to single
        compressed = self.LEADING_SPACE_PATTERN.sub('', compressed)  # Remove leading spaces
        
        return compressed.strip()

    def optimize_chunk_content(self, content: str) -> str:
        """Optimize chunk content for embedding efficiency."""
        return self._compress_whitespace(content)