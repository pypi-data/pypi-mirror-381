"""
Scope and variable management for RenzmcLang

This module handles variable scopes and management for the interpreter.
"""

from renzmc.core.error import NameError as RenzmcNameError


class ScopeManager:
    """
    Manages variable scopes for the interpreter
    """
    
    def __init__(self):
        """Initialize scope manager"""
        self.global_scope = {}  # Global variables
        self.local_scope = {}   # Local variables (for functions)
        self.functions = {}     # User-defined functions
        self.classes = {}       # User-defined classes
        self.modules = {}       # Imported modules
        self.current_instance = None  # Current instance for method calls
        self.instance_scopes = {}  # Scopes for class instances
        self.generators = {}    # User-defined generators
        self.async_functions = {}  # User-defined async functions
        self.decorators = {}    # User-defined decorators
        self.type_registry = {} # Type registry for type checking
        self.builtin_functions = {}  # Built-in functions
    
    def get_variable(self, name):
        """
        Get a variable value
        
        Args:
            name (str): Variable name
            
        Returns:
            Any: Variable value
            
        Raises:
            NameError: If variable is not found
        """
        # Check instance scope first (for class methods)
        if self.current_instance is not None:
            instance_id = id(self.current_instance)
            if instance_id in self.instance_scopes and name in self.instance_scopes[instance_id]:
                return self.instance_scopes[instance_id][name]
        
        # Check local scope
        if name in self.local_scope:
            return self.local_scope[name]
        
        # Check global scope
        if name in self.global_scope:
            return self.global_scope[name]
        
        # Check if it's a built-in function
        if hasattr(self, 'builtin_functions') and name in self.builtin_functions:
            return self.builtin_functions[name]
        
        # Variable not found
        raise RenzmcNameError(f"Variabel '{name}' tidak terdefinisi")
    
    def set_variable(self, name, value, is_local=False):
        """
        Set a variable value
        
        Args:
            name (str): Variable name
            value: Variable value
            is_local (bool): Whether to set in local scope
        """
        # Set in instance scope if we're in a class method
        if self.current_instance is not None and not is_local:
            instance_id = id(self.current_instance)
            if instance_id not in self.instance_scopes:
                self.instance_scopes[instance_id] = {}
            self.instance_scopes[instance_id][name] = value
        elif is_local or self.local_scope:
            # Set in local scope if we're in a function or explicitly requested
            self.local_scope[name] = value
        else:
            # Set in global scope
            self.global_scope[name] = value