"""
Recursion guard utilities for RenzMC
Prevents stack overflow from deeply nested code
"""

from typing import Callable, Any
from functools import wraps
from renzmc.utils.logging import logger

class RecursionGuard:
    """
    Guard against excessive recursion depth
    """
    
    def __init__(self, max_depth: int = 1000):
        """
        Initialize recursion guard
        
        Args:
            max_depth: Maximum recursion depth allowed
        """
        self.max_depth = max_depth
        self.current_depth = 0
    
    def check(self):
        """
        Check if recursion limit exceeded
        
        Raises:
            RecursionError: If max depth exceeded
        """
        self.current_depth += 1
        if self.current_depth > self.max_depth:
            raise RecursionError(
                f"⚠️ Kedalaman rekursi maksimum tercapai: {self.max_depth}\n"
                f"Kode Anda mungkin terlalu kompleks atau memiliki struktur nested yang terlalu dalam.\n"
                f"Pertimbangkan untuk menyederhanakan struktur kode atau mengurangi tingkat nested."
            )
        logger.debug(f"Recursion depth: {self.current_depth}/{self.max_depth}")
    
    def release(self):
        """Release one level of recursion"""
        if self.current_depth > 0:
            self.current_depth -= 1
    
    def reset(self):
        """Reset recursion counter"""
        self.current_depth = 0
    
    def __enter__(self):
        """Context manager entry"""
        self.check()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.release()
        return False

def with_recursion_guard(max_depth: int = 1000):
    """
    Decorator to add recursion guard to a function
    
    Args:
        max_depth: Maximum recursion depth
        
    Usage:
        @with_recursion_guard(max_depth=500)
        def recursive_function():
            pass
    """
    def decorator(func: Callable) -> Callable:
        guard = RecursionGuard(max_depth)
        
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            with guard:
                return func(*args, **kwargs)
        
        # Expose guard for manual control if needed
        wrapper._recursion_guard = guard
        return wrapper
    
    return decorator