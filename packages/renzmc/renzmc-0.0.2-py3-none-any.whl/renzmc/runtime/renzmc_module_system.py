"""
Enhanced module system for RenzmcLang

This module provides advanced import functionality for RenzmcLang classes and modules.
"""

import os
import sys
import importlib.util
from pathlib import Path
from renzmc.core.error import ImportError as RenzmcImportError, NameError as RenzmcNameError
from renzmc.core.token import TokenType


class RenzmcModule:
    """
    Wrapper for RenzmcLang modules to enable proper import functionality
    """
    def __init__(self, module_path, module_name, module_dict):
        self.module_path = module_path
        self.module_name = module_name
        self._module_dict = module_dict
        self._classes = {}
        self._functions = {}
        self._variables = {}
        
        # Categorize module contents
        for name, value in module_dict.items():
            if hasattr(value, '__class__') and value.__class__.__name__ == 'RenzmcClass':
                self._classes[name] = value
            elif callable(value):
                self._functions[name] = value
            else:
                self._variables[name] = value
    
    def __getattr__(self, name):
        """Get attribute from the module"""
        if name in self._module_dict:
            return self._module_dict[name]
        raise RenzmcNameError(f"Modul '{self.module_name}' tidak memiliki atribut '{name}'")
    
    def get_classes(self):
        """Get all classes from this module"""
        return self._classes
    
    def get_functions(self):
        """Get all functions from this module"""
        return self._functions
    
    def get_variables(self):
        """Get all variables from this module"""
        return self._variables
    
    def list_contents(self):
        """List all contents of the module"""
        return {
            'classes': list(self._classes.keys()),
            'functions': list(self._functions.keys()),
            'variables': list(self._variables.keys())
        }


class RenzmcModuleManager:
    """
    Enhanced module manager for RenzmcLang with advanced import capabilities
    """
    
    def __init__(self, interpreter_instance):
        self.interpreter = interpreter_instance
        self.loaded_modules = {}
        self.module_search_paths = []
        self.module_cache = {}
        
        # Add default search paths
        self.add_search_path('.')  # Current directory
        self.add_search_path('./lib')  # Local lib directory
        self.add_search_path('./modules')  # Local modules directory
    
    def add_search_path(self, path):
        """Add a path to search for modules"""
        abs_path = os.path.abspath(path)
        if abs_path not in self.module_search_paths:
            self.module_search_paths.append(abs_path)
    
    def find_module(self, module_name):
        """
        Find a RenzmcLang module file
        
        Args:
            module_name (str): Name of the module to find
            
        Returns:
            str or None: Path to the module file or None if not found
        """
        # Try different file extensions
        extensions = ['.rmc', '.renzmc']
        
        for search_path in self.module_search_paths:
            for ext in extensions:
                module_file = os.path.join(search_path, f"{module_name}{ext}")
                if os.path.isfile(module_file):
                    return module_file
        
        return None
    
    def load_module(self, module_name, alias=None):
        """
        Load a RenzmcLang module
        
        Args:
            module_name (str): Name of the module to load
            alias (str, optional): Alias for the module
            
        Returns:
            RenzmcModule: The loaded module
            
        Raises:
            ImportError: If the module cannot be loaded
        """
        # Check if already loaded
        cache_key = alias or module_name
        if cache_key in self.loaded_modules:
            return self.loaded_modules[cache_key]
        
        # Find the module file
        module_path = self.find_module(module_name)
        if not module_path:
            raise RenzmcImportError(f"Tidak dapat menemukan modul RenzmcLang '{module_name}'")
        
        try:
            # Read and execute the module file
            with open(module_path, 'r', encoding='utf-8') as f:
                module_code = f.read()
            
            # Create a new scope for the module
            module_scope = {}
            
            # Save current state
            old_global_scope = self.interpreter.global_scope.copy()
            old_local_scope = self.interpreter.local_scope.copy()
            
            # Execute module in isolated scope
            self.interpreter.local_scope = module_scope
            
            # Parse and execute the module
            from renzmc.core.lexer import Lexer
            from renzmc.core.parser import Parser
            
            lexer = Lexer(module_code)
            # Collect all tokens using get_next_token()
            tokens = []
            while True:
                token = lexer.get_next_token()
                tokens.append(token)
                if token and token.type == TokenType.EOF:
                    break
            parser = Parser(lexer)
            ast = parser.parse()
            
            # Execute the AST
            self.interpreter.visit(ast)
            
            # Create module object
            module_obj = RenzmcModule(module_path, module_name, module_scope)
            
            # Cache the module
            self.loaded_modules[cache_key] = module_obj
            
            # Restore original state
            self.interpreter.global_scope = old_global_scope
            self.interpreter.local_scope = old_local_scope
            
            return module_obj
            
        except Exception as e:
            raise RenzmcImportError(f"Error memuat modul '{module_name}': {str(e)}")
    
    def import_from_module(self, module_name, items):
        """
        Import specific items from a module
        
        Args:
            module_name (str): Name of the module
            items (list): List of items to import
            
        Returns:
            dict: Dictionary of imported items
        """
        module = self.load_module(module_name)
        imported_items = {}
        
        for item in items:
            if hasattr(module, item):
                imported_items[item] = getattr(module, item)
            else:
                raise RenzmcImportError(f"Tidak dapat mengimpor '{item}' dari modul '{module_name}'")
        
        return imported_items
    
    def import_all_from_module(self, module_name):
        """
        Import all items from a module
        
        Args:
            module_name (str): Name of the module
            
        Returns:
            dict: Dictionary of all module items
        """
        module = self.load_module(module_name)
        return module._module_dict.copy()
    
    def get_module_info(self, module_name):
        """
        Get information about a module
        
        Args:
            module_name (str): Name of the module
            
        Returns:
            dict: Module information
        """
        if module_name in self.loaded_modules:
            module = self.loaded_modules[module_name]
            return {
                'name': module.module_name,
                'path': module.module_path,
                'contents': module.list_contents(),
                'loaded': True
            }
        
        module_path = self.find_module(module_name)
        if module_path:
            return {
                'name': module_name,
                'path': module_path,
                'contents': None,
                'loaded': False
            }
        
        return None
    
    def reload_module(self, module_name):
        """
        Reload a module (useful for development)
        
        Args:
            module_name (str): Name of the module to reload
            
        Returns:
            RenzmcModule: The reloaded module
        """
        # Remove from cache
        if module_name in self.loaded_modules:
            del self.loaded_modules[module_name]
        
        # Load again
        return self.load_module(module_name)
    
    def list_available_modules(self):
        """
        List all available RenzmcLang modules
        
        Returns:
            list: List of available module names
        """
        modules = []
        extensions = ['.rmc', '.renzmc']
        
        for search_path in self.module_search_paths:
            if os.path.isdir(search_path):
                for file in os.listdir(search_path):
                    for ext in extensions:
                        if file.endswith(ext):
                            module_name = file[:-len(ext)]
                            if module_name not in modules:
                                modules.append(module_name)
        
        return modules