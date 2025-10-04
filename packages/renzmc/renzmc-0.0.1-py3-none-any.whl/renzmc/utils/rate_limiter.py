"""
Rate limiter module for RenzMC
Provides rate limiting functionality for operations
"""

from functools import wraps
import time
from collections import defaultdict
from threading import Lock
from typing import Callable, Any

class RateLimiter:
    """
    Thread-safe rate limiter decorator
    
    Usage:
        @RateLimiter(max_calls=10, period=60)
        def my_function():
            pass
    """
    
    def __init__(self, max_calls: int = 100, period: int = 60):
        """
        Initialize rate limiter
        
        Args:
            max_calls: Maximum number of calls allowed
            period: Time period in seconds
        """
        self.max_calls = max_calls
        self.period = period
        self.calls = defaultdict(list)
        self.lock = Lock()
    
    def __call__(self, func: Callable) -> Callable:
        """
        Decorator implementation
        
        Args:
            func: Function to rate limit
            
        Returns:
            Wrapped function with rate limiting
        """
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            with self.lock:
                now = time.time()
                key = func.__name__
                
                # Clean old calls outside the time window
                self.calls[key] = [
                    call_time for call_time in self.calls[key]
                    if now - call_time < self.period
                ]
                
                # Check if limit exceeded
                if len(self.calls[key]) >= self.max_calls:
                    raise RuntimeError(
                        f"⚠️ Rate limit tercapai untuk '{func.__name__}'\n"
                        f"Maksimum: {self.max_calls} panggilan per {self.period} detik\n"
                        f"Silakan tunggu beberapa saat sebelum mencoba lagi."
                    )
                
                # Record this call
                self.calls[key].append(now)
            
            # Execute the function
            return func(*args, **kwargs)
        
        return wrapper
    
    def reset(self, func_name: str = None):
        """
        Reset rate limit for a function
        
        Args:
            func_name: Function name to reset (None = reset all)
        """
        with self.lock:
            if func_name:
                self.calls[func_name] = []
            else:
                self.calls.clear()

# Global rate limiter instances for common use cases
http_rate_limiter = RateLimiter(max_calls=100, period=60)  # 100 requests per minute
file_rate_limiter = RateLimiter(max_calls=1000, period=60)  # 1000 file ops per minute