from ..analyzers.java_analyzer import JavaCSTAnalyzer
from .code_chunker import CodeChunker
from ..chunking_strategies.smart_method_strategy import SmartMethodStrategy
from ..parsers.java_parser import JavaParser


def create_java_chunker(
    min_chunk_size: int = 500,      # Minimum viable chunk size
    max_chunk_size: int = 2000,     # Maximum chunk size before splitting
    max_class_size: int = 3000      # Complete class threshold
) -> CodeChunker:
    """
    Factory function to create a Java code chunker with smart grouping strategy.
    
    Args:
        min_chunk_size: Minimum chunk size to avoid tiny fragments (default: 500)
        max_chunk_size: Maximum chunk size before splitting (default: 2000) 
        max_class_size: Keep class complete if under this size (default: 3000)
    """
    parser = JavaParser()
    analyzer = JavaCSTAnalyzer(parser)
    strategy = SmartMethodStrategy(
        min_chunk_size=min_chunk_size,
        max_chunk_size=max_chunk_size, 
        max_class_size=max_class_size
    )
    return CodeChunker(parser, analyzer, strategy)