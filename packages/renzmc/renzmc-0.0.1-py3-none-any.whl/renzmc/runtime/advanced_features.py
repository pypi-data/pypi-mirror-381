"""
Advanced Python-like features for RenzmcLang

This module provides decorators, context managers, and enhanced generators.
"""

import functools
import contextlib
from renzmc.core.error import RuntimeError as RenzmcRuntimeError


class RenzmcDecorator:
    """
    Enhanced decorator system for RenzmcLang
    """
    
    def __init__(self, decorator_func, decorator_args=None, decorator_kwargs=None):
        self.decorator_func = decorator_func
        self.decorator_args = decorator_args or ()
        self.decorator_kwargs = decorator_kwargs or {}
        self.name = getattr(decorator_func, '__name__', 'decorator')
        
        # If decorator has arguments, call it to get the actual decorator
        if self.decorator_args or self.decorator_kwargs:
            try:
                # For decorator with arguments, we create a decorator factory
                self.actual_decorator = self.decorator_func(*self.decorator_args, **self.decorator_kwargs)
                # The factory should return a function that takes (func, *args, **kwargs)
                if not callable(self.actual_decorator):
                    raise RenzmcRuntimeError(f"Decorator factory '{self.name}' must return a callable")
            except Exception as e:
                raise RenzmcRuntimeError(f"Error creating decorator '{self.name}' with args: {str(e)}")
        else:
            self.actual_decorator = self.decorator_func
    
    def __call__(self, func):
        """Apply the decorator to a function"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return self.actual_decorator(func, *args, **kwargs)
            except Exception as e:
                raise RenzmcRuntimeError(f"Error dalam decorator '{self.name}': {str(e)}")
        return wrapper
    
    def __repr__(self):
        return f"<RenzmcDecorator '{self.name}'>"


class RenzmcContextManager:
    """
    Context manager implementation for RenzmcLang
    """
    
    def __init__(self, enter_func, exit_func, name="ContextManager"):
        self.enter_func = enter_func
        self.exit_func = exit_func
        self.name = name
        self.active = False
        self.resource = None
    
    def __enter__(self):
        """Enter the context"""
        try:
            self.active = True
            if self.enter_func:
                self.resource = self.enter_func()
                return self.resource
            return self
        except Exception as e:
            self.active = False
            raise RenzmcRuntimeError(f"Error masuk ke context manager '{self.name}': {str(e)}")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context"""
        try:
            if self.exit_func and self.active:
                self.exit_func(self.resource, exc_type, exc_val, exc_tb)
            return False  # Don't suppress exceptions
        except Exception as e:
            raise RenzmcRuntimeError(f"Error keluar dari context manager '{self.name}': {str(e)}")
        finally:
            self.active = False
    
    def __repr__(self):
        status = "active" if self.active else "inactive"
        return f"<RenzmcContextManager '{self.name}' ({status})>"


class RenzmcGenerator:
    """
    Enhanced generator implementation for RenzmcLang
    """
    
    def __init__(self, generator_func, *args, **kwargs):
        self.generator_func = generator_func
        self.args = args
        self.kwargs = kwargs
        self.generator = None
        self.started = False
        self.finished = False
        
    def __iter__(self):
        """Make the generator iterable"""
        if not self.started:
            self.generator = self.generator_func(*self.args, **self.kwargs)
            self.started = True
        return self
    
    def __next__(self):
        """Get the next value from the generator"""
        try:
            if self.finished:
                raise StopIteration
            
            if not self.started:
                self.generator = self.generator_func(*self.args, **self.kwargs)
                self.started = True
            
            if self.generator is not None:
                return next(self.generator)
            else:
                raise StopIteration
        except StopIteration:
            self.finished = True
            raise
        except Exception as e:
            raise RenzmcRuntimeError(f"Error dalam generator: {str(e)}")
    
    def send(self, value):
        """Send a value to the generator"""
        try:
            if not self.started:
                self.generator = self.generator_func(*self.args, **self.kwargs)
                self.started = True
            
            if self.generator is not None:
                return self.generator.send(value)
            else:
                raise StopIteration
        except StopIteration:
            self.finished = True
            raise
        except Exception as e:
            raise RenzmcRuntimeError(f"Error mengirim nilai ke generator: {str(e)}")
    
    def close(self):
        """Close the generator"""
        if self.generator and self.started:
            try:
                self.generator.close()
            except (StopIteration, GeneratorExit):
                # Expected exceptions when closing generator
                pass
            except Exception as e:
                # Log unexpected errors
                from renzmc.utils.logging import logger
                logger.warning(f"Error closing generator: {e}")
        self.finished = True
    
    def __repr__(self):
        status = "finished" if self.finished else ("active" if self.started else "ready")
        return f"<RenzmcGenerator ({status})>"


class AsyncFunction:
    """
    Async function wrapper for RenzmcLang
    """
    
    def __init__(self, func, name=None):
        self.func = func
        self.name = name or getattr(func, '__name__', 'async_function')
        self.is_coroutine = True
    
    async def __call__(self, *args, **kwargs):
        """Call the async function"""
        try:
            if hasattr(self.func, '__call__'):
                result = self.func(*args, **kwargs)
                # If the result is already a coroutine, await it
                if hasattr(result, '__await__'):
                    return await result
                return result
            else:
                raise RenzmcRuntimeError(f"'{self.name}' bukan fungsi yang dapat dipanggil")
        except Exception as e:
            raise RenzmcRuntimeError(f"Error dalam fungsi async '{self.name}': {str(e)}")
    
    def __repr__(self):
        return f"<AsyncFunction '{self.name}'>"


class AdvancedFeatureManager:
    """
    Manager for advanced RenzmcLang features
    """
    
    def __init__(self):
        self.decorators = {}
        self.context_managers = {}
        self.generators = {}
        self.async_functions = {}
    
    def create_decorator(self, name, decorator_func):
        """
        Create a new decorator
        
        Args:
            name (str): Name of the decorator
            decorator_func: The decorator function
            
        Returns:
            function: The stored decorator function
        """
        # Store the raw decorator function, not wrapped
        # Wrapping will happen at application time with proper arguments
        self.decorators[name] = decorator_func
        return decorator_func
    
    def create_context_manager(self, name, enter_func=None, exit_func=None):
        """
        Create a new context manager
        
        Args:
            name (str): Name of the context manager
            enter_func: Function to call on enter
            exit_func: Function to call on exit
            
        Returns:
            RenzmcContextManager: The created context manager
        """
        context_manager = RenzmcContextManager(enter_func, exit_func, name)
        self.context_managers[name] = context_manager
        return context_manager
    
    def create_generator(self, name, generator_func, *args, **kwargs):
        """
        Create a new generator
        
        Args:
            name (str): Name of the generator
            generator_func: The generator function
            *args: Arguments for the generator function
            **kwargs: Keyword arguments for the generator function
            
        Returns:
            RenzmcGenerator: The created generator
        """
        generator = RenzmcGenerator(generator_func, *args, **kwargs)
        self.generators[name] = generator
        return generator
    
    def create_async_function(self, name, func):
        """
        Create a new async function
        
        Args:
            name (str): Name of the async function
            func: The function to make async
            
        Returns:
            AsyncFunction: The created async function
        """
        async_func = AsyncFunction(func, name)
        self.async_functions[name] = async_func
        return async_func
    
    def apply_decorator(self, decorator_name, func):
        """
        Apply a decorator to a function
        
        Args:
            decorator_name (str): Name of the decorator
            func: Function to decorate
            
        Returns:
            Function: The decorated function
        """
        if decorator_name not in self.decorators:
            raise RenzmcRuntimeError(f"Decorator '{decorator_name}' tidak ditemukan")
        
        decorator = self.decorators[decorator_name]
        return decorator(func)
    
    def get_context_manager(self, name):
        """
        Get a context manager by name
        
        Args:
            name (str): Name of the context manager
            
        Returns:
            RenzmcContextManager: The context manager
        """
        if name not in self.context_managers:
            raise RenzmcRuntimeError(f"Context manager '{name}' tidak ditemukan")
        
        return self.context_managers[name]
    
    def list_features(self):
        """
        List all available advanced features
        
        Returns:
            dict: Dictionary of all features
        """
        return {
            'decorators': list(self.decorators.keys()),
            'context_managers': list(self.context_managers.keys()),
            'generators': list(self.generators.keys()),
            'async_functions': list(self.async_functions.keys())
        }


# Built-in decorators
def timing_decorator(func, *args, **kwargs):
    """
    Timing decorator that works with RenzmcLang decorator system
    
    This function is called when the decorated function is executed.
    """
    import time
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Fungsi '{func.__name__}' selesai dalam {end_time - start_time:.4f} detik")
    return result


def retry_decorator(*decorator_args, **decorator_kwargs):
    """
    Retry decorator factory that properly supports both @coba_ulang and @coba_ulang(n) syntax
    
    This function works with the RenzmcDecorator system:
    1. When used as @coba_ulang (no args), this function IS the decorator (like timing_decorator)
    2. When used as @coba_ulang(5) (with args), this function returns a decorator function
    """
    # Case 1: @coba_ulang(5) - decorator_args[0] is the max_attempts parameter
    if decorator_args:
        max_attempts = decorator_args[0]
        
        # Return a decorator function that RenzmcLang will use via RenzmcDecorator
        def parameterized_retry_decorator(func, *call_args, **call_kwargs):
            """
            Parameterized retry decorator for @coba_ulang(n) syntax
            """
            for attempt in range(max_attempts):
                try:
                    return func(*call_args, **call_kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Percobaan {attempt + 1} dari {max_attempts} gagal, mencoba lagi...")
            return None
        
        return parameterized_retry_decorator
    
    # Case 2: @coba_ulang - no arguments, this function IS the decorator itself
    # This follows the same pattern as timing_decorator(func, *args, **kwargs)
    # We expect the first argument to be the decorated function
    if decorator_args:
        # This shouldn't happen but handle gracefully
        func = decorator_args[0]
        call_args = decorator_args[1:]
    else:
        # This is an error - we need at least the function argument
        raise RenzmcRuntimeError("retry_decorator called without function argument")
    
    # Execute retry logic with default 3 attempts (same as timing_decorator pattern)
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            return func(*call_args, **decorator_kwargs)
        except Exception as e:
            if attempt == max_attempts - 1:
                raise e
            print(f"Percobaan {attempt + 1} dari {max_attempts} gagal, mencoba lagi...")
    return None


def simple_retry_decorator(func, *args, **kwargs):
    """
    Simple retry decorator for @coba_ulang syntax (default 3 attempts)
    This follows the exact same pattern as timing_decorator
    """
    max_attempts = 3  # default
    for attempt in range(max_attempts):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt == max_attempts - 1:
                raise e
            print(f"Percobaan {attempt + 1} dari {max_attempts} gagal, mencoba lagi...")
    return None


def universal_retry_decorator(*decorator_args, **decorator_kwargs):
    """
    Universal retry decorator that handles both @coba_ulang and @coba_ulang(n) syntax
    This function properly follows the RenzmcDecorator calling pattern.
    """
    # Case 1: Called with arguments (@coba_ulang(3))
    # decorator_args will contain [3] and this needs to return a decorator function
    if decorator_args and not callable(decorator_args[0]):
        max_attempts = decorator_args[0]
        
        # Return a decorator function following the timing_decorator pattern
        def parameterized_retry_decorator(func, *call_args, **call_kwargs):
            """Decorator function that executes the retry logic at runtime"""
            for attempt in range(max_attempts):
                try:
                    return func(*call_args, **call_kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Percobaan {attempt + 1} dari {max_attempts} gagal, mencoba lagi...")
            return None
        
        return parameterized_retry_decorator
    
    # Case 2: Called directly as decorator (@coba_ulang)
    # This follows the timing_decorator(func, *args, **kwargs) pattern exactly
    else:
        # This function IS the decorator and will be called with (func, *args, **kwargs)
        # The first argument is the decorated function, remaining are the call arguments
        if decorator_args and callable(decorator_args[0]):
            func = decorator_args[0]
            call_args = decorator_args[1:]
            max_attempts = 3  # default
            
            # Execute the retry logic immediately (same as timing_decorator pattern)
            for attempt in range(max_attempts):
                try:
                    return func(*call_args, **decorator_kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Percobaan {attempt + 1} dari {max_attempts} gagal, mencoba lagi...")
            return None
        else:
            # Fallback case - return the simple retry decorator
            return simple_retry_decorator


def create_parameterized_retry_decorator(max_attempts):
    """
    Create a retry decorator with specific number of attempts
    This is used internally for handling @coba_ulang(n) syntax
    """
    def parameterized_retry_decorator(func, *args, **kwargs):
        for attempt in range(max_attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == max_attempts - 1:
                    raise e
                print(f"Percobaan {attempt + 1} dari {max_attempts} gagal, mencoba lagi...")
        return None
    return parameterized_retry_decorator


def create_retry_decorator_with_attempts(attempts):
    """
    Create a retry decorator with specific number of attempts
    
    Usage: retry_3 = create_retry_decorator_with_attempts(3)
    """
    def retry_decorator_n(func, *args, **kwargs):
        for attempt in range(attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == attempts - 1:
                    raise e
                print(f"Percobaan {attempt + 1} dari {attempts} gagal, mencoba lagi...")
        return None
    return retry_decorator_n


# Global cache dictionary for all cached functions
_GLOBAL_CACHE = {}

def cache_decorator(func, *args, **kwargs):
    """
    Improved caching decorator that works with RenzmcLang decorator system
    
    This function is called when the decorated function is executed.
    """
    # Create cache key from function name and arguments
    func_name = getattr(func, '__name__', str(func))
    
    # Create a more robust cache key
    try:
        # Convert arguments to hashable types for cache key
        args_str = str(args) if args else ""
        kwargs_str = str(sorted(kwargs.items())) if kwargs else ""
        cache_key = f"{func_name}_{hash(args_str)}_{hash(kwargs_str)}"
    except (TypeError, ValueError) as e:
        # Fallback if hashing fails - use simpler key
        from renzmc.utils.logging import logger
        logger.debug(f"Cache key generation failed, using simple key: {e}")
        cache_key = f"{func_name}_{str(args)}_{str(kwargs)}"
    
    # Check if result is cached
    if cache_key in _GLOBAL_CACHE:
        print(f"Cache HIT untuk {func_name} dengan args {args}")
        return _GLOBAL_CACHE[cache_key]
    
    # Call the actual function and cache the result
    print(f"Cache MISS untuk {func_name} dengan args {args}")
    result = func(*args, **kwargs)
    _GLOBAL_CACHE[cache_key] = result
    return result


def create_custom_decorator(decorator_name, decorator_func):
    """
    Create a custom decorator that can be used in RenzmcLang
    
    Args:
        decorator_name (str): Name of the decorator
        decorator_func (callable): The decorator function
    
    Returns:
        callable: A properly wrapped decorator function
    """
    def custom_decorator_wrapper(func, *args, **kwargs):
        """Wrapper that handles the decorator logic"""
        try:
            # Call the original decorator function
            return decorator_func(func, *args, **kwargs)
        except Exception as e:
            raise RenzmcRuntimeError(f"Error dalam decorator '{decorator_name}': {str(e)}")
    
    # Set proper name for debugging
    custom_decorator_wrapper.__name__ = decorator_name
    return custom_decorator_wrapper


def web_route_decorator(path_or_func, method="GET"):
    """
    Enhanced web route decorator for RenzmcLang
    Supports both @route("/path") and @route("/path", "POST") syntax
    """
    def route_decorator(func, *args, **kwargs):
        """Route decorator implementation"""
        # Store route information in function metadata
        if not hasattr(func, '_routes'):
            func._routes = []
        
        route_info = {
            'path': path_or_func if isinstance(path_or_func, str) else args[0] if args else "/",
            'method': method,
            'handler': func
        }
        func._routes.append(route_info)
        
        # Execute the original function
        return func(*args, **kwargs)
    
    # If called directly (e.g., @route without parentheses)
    if callable(path_or_func):
        return lambda *args, **kwargs: route_decorator(path_or_func, *args, **kwargs)
    
    # Normal decorator factory case
    return route_decorator


def clear_cache():
    """Clear the global cache for all cached functions"""
    global _GLOBAL_CACHE
    _GLOBAL_CACHE.clear()
    print("Cache global telah dibersihkan")


def get_cache_stats():
    """Get statistics about the global cache"""
    global _GLOBAL_CACHE
    return {
        'cache_size': len(_GLOBAL_CACHE),
        'cached_items': list(_GLOBAL_CACHE.keys())
    }


# Export the decorators at module level for import
__all__ = [
    'AdvancedFeatureManager', 
    'RenzmcDecorator', 
    'RenzmcContextManager', 
    'RenzmcGenerator', 
    'AsyncFunction',
    'timing_decorator',
    'retry_decorator', 
    'cache_decorator',
    'create_custom_decorator',
    'web_route_decorator',
    'clear_cache',
    'get_cache_stats'
]