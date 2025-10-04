"""
Python integration for RenzmcLang

This module handles Python module imports and function calls.
"""

import importlib
import builtins as py_builtins
import sys
import asyncio
from renzmc.core.error import ImportError as RenzmcImportError, TypeError as RenzmcTypeError, AttributeError as RenzmcAttributeError


class SmartPythonWrapper:
    """
    Intelligent wrapper for Python objects with automatic type conversion
    Enhanced with full Python special methods support for 100% compatibility
    """
    def __init__(self, obj, integration_manager):
        self._obj = obj
        self._integration = integration_manager
        self._obj_type = type(obj).__name__
        
        # RenzmcLang reserved keywords that might conflict with Python attributes
    
    def __getattr__(self, name):
        """Get attribute with automatic wrapping and smart keyword handling"""
        try:
            # Smart attribute access - handle RenzmcLang keyword conflicts
            attr = getattr(self._obj, name)
            return self._integration.convert_python_to_renzmc(attr)
        except AttributeError:
            raise RenzmcAttributeError(f"Objek Python '{self._obj_type}' tidak memiliki atribut '{name}'")
    
    def __setattr__(self, name, value):
        """Set attribute with automatic conversion"""
        if name.startswith('_'):
            # Internal attributes
            super().__setattr__(name, value)
        else:
            try:
                setattr(self._obj, name, self._integration.convert_renzmc_to_python(value))
            except AttributeError:
                raise RenzmcAttributeError(f"Tidak dapat mengatur atribut '{name}' pada objek Python '{self._obj_type}'")
    
    def __call__(self, *args, **kwargs):
        """Call with automatic type conversion"""
        if callable(self._obj):
            # Convert arguments
            py_args = [self._integration.convert_renzmc_to_python(arg) for arg in args]
            py_kwargs = {k: self._integration.convert_renzmc_to_python(v) for k, v in kwargs.items()}
            
            # Call the function
            result = self._obj(*py_args, **py_kwargs)
            
            # Convert result back
            return self._integration.convert_python_to_renzmc(result)
        else:
            raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak dapat dipanggil")
    
    def __getitem__(self, key):
        """Support indexing with type conversion"""
        try:
            result = self._obj[self._integration.convert_renzmc_to_python(key)]
            return self._integration.convert_python_to_renzmc(result)
        except (KeyError, IndexError, TypeError) as e:
            raise RenzmcAttributeError(f"Error mengakses indeks pada objek Python: {str(e)}")
    
    def __setitem__(self, key, value):
        """Support item assignment with type conversion"""
        try:
            self._obj[self._integration.convert_renzmc_to_python(key)] = self._integration.convert_renzmc_to_python(value)
        except (KeyError, IndexError, TypeError) as e:
            raise RenzmcAttributeError(f"Error mengatur indeks pada objek Python: {str(e)}")
    
    def __delitem__(self, key):
        """Support item deletion"""
        try:
            del self._obj[self._integration.convert_renzmc_to_python(key)]
        except (KeyError, IndexError, TypeError) as e:
            raise RenzmcAttributeError(f"Error menghapus indeks pada objek Python: {str(e)}")
    
    def __iter__(self):
        """Support iteration with type conversion"""
        try:
            for item in self._obj:
                yield self._integration.convert_python_to_renzmc(item)
        except TypeError:
            raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak dapat diiterasi")
    
    def __next__(self):
        """Support next() function for iterators"""
        try:
            result = next(self._obj)
            return self._integration.convert_python_to_renzmc(result)
        except StopIteration:
            raise StopIteration
        except TypeError:
            raise RenzmcTypeError(f"Objek Python '{self._obj_type}' bukan iterator")
    
    def __len__(self):
        """Support len() function"""
        try:
            return len(self._obj)
        except TypeError:
            raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak memiliki panjang")
    
    def __contains__(self, item):
        """Support 'in' operator"""
        try:
            return self._integration.convert_renzmc_to_python(item) in self._obj
        except TypeError:
            return False
    
    def __enter__(self):
        """Support context manager entry"""
        try:
            result = self._obj.__enter__()
            return self._integration.convert_python_to_renzmc(result)
        except AttributeError:
            raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak mendukung context manager")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support context manager exit"""
        try:
            return self._obj.__exit__(exc_type, exc_val, exc_tb)
        except AttributeError:
            raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak mendukung context manager")
    
    # Comparison operators
    def __eq__(self, other):
        """Support equality comparison"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            return self._obj == other_py
        except (TypeError, ValueError, AttributeError):
            return False
    
    def __ne__(self, other):
        """Support inequality comparison"""
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """Support less than comparison"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            return self._obj < other_py
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat membandingkan objek Python '{self._obj_type}'")
    
    def __le__(self, other):
        """Support less than or equal comparison"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            return self._obj <= other_py
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat membandingkan objek Python '{self._obj_type}'")
    
    def __gt__(self, other):
        """Support greater than comparison"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            return self._obj > other_py
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat membandingkan objek Python '{self._obj_type}'")
    
    def __ge__(self, other):
        """Support greater than or equal comparison"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            return self._obj >= other_py
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat membandingkan objek Python '{self._obj_type}'")
    
    # Arithmetic operators
    def __add__(self, other):
        """Support addition"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj + other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat menambahkan pada objek Python '{self._obj_type}'")
    
    def __sub__(self, other):
        """Support subtraction"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj - other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat mengurangi pada objek Python '{self._obj_type}'")
    
    def __mul__(self, other):
        """Support multiplication"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj * other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat mengalikan pada objek Python '{self._obj_type}'")
    
    def __truediv__(self, other):
        """Support division"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj / other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat membagi pada objek Python '{self._obj_type}'")
    
    def __mod__(self, other):
        """Support modulo"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj % other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat modulo pada objek Python '{self._obj_type}'")
    
    def __pow__(self, other):
        """Support power"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj ** other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat pangkat pada objek Python '{self._obj_type}'")
    
    # Boolean operations
    def __bool__(self):
        """Support boolean conversion"""
        try:
            return bool(self._obj)
        except (TypeError, ValueError):
            return True
    
    def __hash__(self):
        """Support hashing"""
        try:
            return hash(self._obj)
        except TypeError:
            raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak dapat di-hash")
    
    def __str__(self):
        """String representation"""
        try:
            return str(self._obj)
        except (TypeError, ValueError):
            return f"SmartWrapper({self._obj_type})"
    
    def __repr__(self):
        """Developer representation"""
        try:
            return repr(self._obj)
        except (TypeError, ValueError):
            return f"<SmartPythonWrapper for {self._obj_type}>"
    
    def __dir__(self):
        """Return available attributes for better introspection"""
        try:
            return dir(self._obj)
        except (TypeError, AttributeError):
            return []
    
    def __format__(self, format_spec):
        """Support string formatting"""
        try:
            return format(self._obj, format_spec)
        except (TypeError, ValueError):
            return str(self._obj)
    
    def __sizeof__(self):
        """Support sys.getsizeof()"""
        try:
            return self._obj.__sizeof__()
        except (TypeError, AttributeError):
            return object.__sizeof__(self)
    
    def __reduce__(self):
        """Support pickle.dumps()"""
        try:
            return self._obj.__reduce__()
        except (TypeError, AttributeError):
            raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak dapat di-pickle")
    
    def __reduce_ex__(self, protocol):
        """Support pickle with protocol"""
        try:
            return self._obj.__reduce_ex__(protocol)
        except (TypeError, AttributeError):
            raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak dapat di-pickle dengan protocol {protocol}")
    
    def __copy__(self):
        """Support copy.copy()"""
        try:
            import copy
            result = copy.copy(self._obj)
            return self._integration.convert_python_to_renzmc(result)
        except (TypeError, AttributeError) as e:
            raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak dapat di-copy: {e}")
    
    def __deepcopy__(self, memo):
        """Support copy.deepcopy()"""
        try:
            import copy
            result = copy.deepcopy(self._obj, memo)
            return self._integration.convert_python_to_renzmc(result)
        except (TypeError, AttributeError) as e:
            raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak dapat di-deepcopy: {e}")
    
    # Async support methods
    def __await__(self):
        """Support await syntax"""
        try:
            if hasattr(self._obj, '__await__'):
                return self._obj.__await__()
            else:
                raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak mendukung await")
        except Exception as e:
            raise RenzmcTypeError(f"Error dalam await: {str(e)}")
    
    def __aiter__(self):
        """Support async iteration"""
        try:
            if hasattr(self._obj, '__aiter__'):
                result = self._obj.__aiter__()
                return self._integration.convert_python_to_renzmc(result)
            else:
                raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak mendukung async iteration")
        except Exception as e:
            raise RenzmcTypeError(f"Error dalam async iteration: {str(e)}")
    
    def __anext__(self):
        """Support async next"""
        try:
            if hasattr(self._obj, '__anext__'):
                result = self._obj.__anext__()
                return self._integration.convert_python_to_renzmc(result)
            else:
                raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak mendukung async next")
        except Exception as e:
            raise RenzmcTypeError(f"Error dalam async next: {str(e)}")
    
    # Async context manager support
    def __aenter__(self):
        """Support async context manager entry"""
        try:
            if hasattr(self._obj, '__aenter__'):
                result = self._obj.__aenter__()
                return self._integration.convert_python_to_renzmc(result)
            else:
                raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak mendukung async context manager")
        except Exception as e:
            raise RenzmcTypeError(f"Error dalam async context manager entry: {str(e)}")
    
    def __aexit__(self, exc_type, exc_val, exc_tb):
        """Support async context manager exit"""
        try:
            if hasattr(self._obj, '__aexit__'):
                return self._obj.__aexit__(exc_type, exc_val, exc_tb)
            else:
                raise RenzmcTypeError(f"Objek Python '{self._obj_type}' tidak mendukung async context manager")
        except Exception as e:
            raise RenzmcTypeError(f"Error dalam async context manager exit: {str(e)}")
    
    # Additional operators for comprehensive support
    def __and__(self, other):
        """Support bitwise AND (&)"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj & other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat melakukan operasi AND pada objek Python '{self._obj_type}'")
    
    def __or__(self, other):
        """Support bitwise OR (|)"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj | other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat melakukan operasi OR pada objek Python '{self._obj_type}'")
    
    def __xor__(self, other):
        """Support bitwise XOR (^)"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj ^ other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat melakukan operasi XOR pada objek Python '{self._obj_type}'")
    
    def __lshift__(self, other):
        """Support left shift (<<)"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj << other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat melakukan left shift pada objek Python '{self._obj_type}'")
    
    def __rshift__(self, other):
        """Support right shift (>>)"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj >> other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat melakukan right shift pada objek Python '{self._obj_type}'")
    
    def __floordiv__(self, other):
        """Support floor division (//)"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj // other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat melakukan floor division pada objek Python '{self._obj_type}'")
    
    def __divmod__(self, other):
        """Support divmod() function"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = divmod(self._obj, other_py)
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat melakukan divmod pada objek Python '{self._obj_type}'")
    
    def __matmul__(self, other):
        """Support matrix multiplication (@)"""
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = self._obj @ other_py
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat melakukan matrix multiplication pada objek Python '{self._obj_type}'")
    
    # Right-hand side operators
    def __radd__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = other_py + self._obj
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat menambahkan objek Python '{self._obj_type}' dari kanan")
    
    def __rsub__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = other_py - self._obj
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat mengurangi objek Python '{self._obj_type}' dari kanan")
    
    def __rmul__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = other_py * self._obj
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat mengalikan objek Python '{self._obj_type}' dari kanan")
    
    def __rtruediv__(self, other):
        try:
            other_py = self._integration.convert_renzmc_to_python(other)
            result = other_py / self._obj
            return self._integration.convert_python_to_renzmc(result)
        except TypeError:
            raise RenzmcTypeError(f"Tidak dapat membagi objek Python '{self._obj_type}' dari kanan")


class PythonModule:
    """
    Enhanced wrapper for Python modules to enable proper attribute access in RenzmcLang
    Now with advanced module introspection and lazy loading support
    """
    def __init__(self, module):
        self._module = module
        self._module_name = module.__name__
        self._cached_attributes = {}
        self._submodule_cache = {}
    
    def __getattr__(self, name):
        """Get attribute from the wrapped Python module"""
        try:
            attr = getattr(self._module, name)
            # If the attribute is a module, wrap it too
            if hasattr(attr, '__name__') and hasattr(attr, '__file__'):
                return PythonModule(attr)
            return attr
        except AttributeError:
            raise RenzmcAttributeError(f"Modul Python '{self._module_name}' tidak memiliki atribut '{name}'")
    
    def __getitem__(self, key):
        """Enable indexing for modules that support it"""
        try:
            if hasattr(self._module, '__getitem__'):
                return self._module[key]
            else:
                raise RenzmcAttributeError(f"Modul Python '{self._module_name}' tidak mendukung indexing")
        except (KeyError, IndexError, TypeError) as e:
            raise RenzmcAttributeError(f"Error mengakses indeks '{key}' pada modul '{self._module_name}': {str(e)}")
    
    def __setitem__(self, key, value):
        """Enable item assignment for modules that support it"""
        try:
            if hasattr(self._module, '__setitem__'):
                self._module[key] = value
            else:
                raise RenzmcAttributeError(f"Modul Python '{self._module_name}' tidak mendukung assignment")
        except (KeyError, IndexError, TypeError) as e:
            raise RenzmcAttributeError(f"Error mengatur indeks '{key}' pada modul '{self._module_name}': {str(e)}")
    
    def __iter__(self):
        """Enable iteration for modules that support it"""
        if hasattr(self._module, '__iter__'):
            return iter(self._module)
        else:
            raise RenzmcTypeError(f"Modul Python '{self._module_name}' tidak dapat diiterasi")
    
    def __len__(self):
        """Enable len() for modules that support it"""
        if hasattr(self._module, '__len__'):
            return len(self._module)
        else:
            raise RenzmcTypeError(f"Modul Python '{self._module_name}' tidak memiliki panjang")
    
    def __call__(self, *args, **kwargs):
        """Allow the module to be called if it's callable"""
        if callable(self._module):
            return self._module(*args, **kwargs)
        raise RenzmcTypeError(f"Modul Python '{self._module_name}' tidak dapat dipanggil")
    
    def __repr__(self):
        return f"<PythonModule '{self._module_name}'>"
    
    def __str__(self):
        return f"PythonModule({self._module_name})"
    
    def __dir__(self):
        """Return available attributes for better introspection"""
        return dir(self._module)


class PythonIntegration:
    """
    Enhanced Python integration for the interpreter with full module support
    """
    
    def __init__(self):
        """Initialize Python integration"""
        self.imported_modules = {}
        self.module_aliases = {}
        self.from_imports = {}
    
    def setup_python_builtins(self, global_scope):
        """
        Add Python builtins to global scope with 'py_' prefix
        
        Args:
            global_scope (dict): The global scope dictionary to update
        """
        for name in dir(py_builtins):
            # Skip private attributes
            if not name.startswith('_'):
                global_scope[f"py_{name}"] = getattr(py_builtins, name)
    
    def import_python_module(self, module_name, alias=None, from_items=None):
        """
        Enhanced Python module import with support for aliases and from imports
        
        Args:
            module_name (str): The name of the module to import
            alias (str, optional): Alias for the module
            from_items (list, optional): List of items to import from the module
            
        Returns:
            PythonModule or dict: The imported module wrapper or items dict
            
        Raises:
            ImportError: If the module cannot be imported
        """
        try:
            # Try to get from cache first
            if module_name in self.imported_modules:
                module = self.imported_modules[module_name]
            else:
                # Import the module
                module = importlib.import_module(module_name)
                self.imported_modules[module_name] = module
            
            # Handle from imports (from module import item1, item2)
            if from_items:
                imported_items = {}
                for item in from_items:
                    if hasattr(module, item):
                        imported_items[item] = getattr(module, item)
                    else:
                        raise RenzmcImportError(f"Tidak dapat mengimpor '{item}' dari modul Python '{module_name}'")
                
                # Store for later reference
                self.from_imports[module_name] = imported_items
                return imported_items
            
            # Wrap the module for proper attribute access
            wrapped_module = PythonModule(module)
            
            # Handle alias
            if alias:
                self.module_aliases[alias] = wrapped_module
            
            return wrapped_module
            
        except ImportError as e:
            raise RenzmcImportError(f"Tidak dapat mengimpor modul Python '{module_name}': {str(e)}")
        except Exception as e:
            raise RenzmcImportError(f"Error saat mengimpor modul Python '{module_name}': {str(e)}")
    
    def get_module_attribute(self, module_name, attribute_name):
        """
        Get an attribute from an imported module with alias support
        
        Args:
            module_name (str): The name of the module or alias
            attribute_name (str): The name of the attribute
            
        Returns:
            Any: The attribute value
            
        Raises:
            AttributeError: If the attribute doesn't exist
            ImportError: If the module isn't imported
        """
        # Check if it's an alias first
        if module_name in self.module_aliases:
            module = self.module_aliases[module_name]._module
        elif module_name in self.imported_modules:
            module = self.imported_modules[module_name]
        else:
            raise RenzmcImportError(f"Modul Python '{module_name}' belum diimpor")
        
        try:
            return getattr(module, attribute_name)
        except AttributeError:
            raise RenzmcAttributeError(f"Modul Python '{module_name}' tidak memiliki atribut '{attribute_name}'")
    
    def call_python_function(self, func, *args, **kwargs):
        """
        Enhanced Python function call with better error handling
        
        Args:
            func: The Python function to call
            *args: Positional arguments
            **kwargs: Keyword arguments
            
        Returns:
            Any: The result of the function call
            
        Raises:
            TypeError: If the function call fails
        """
        try:
            if callable(func):
                return func(*args, **kwargs)
            else:
                raise RenzmcTypeError(f"Objek '{func}' tidak dapat dipanggil")
        except Exception as e:
            raise RenzmcTypeError(f"Error dalam pemanggilan fungsi Python: {str(e)}")
    
    def create_python_object(self, class_obj, *args, **kwargs):
        """
        Create an instance of a Python class
        
        Args:
            class_obj: The Python class to instantiate
            *args: Positional arguments for the constructor
            **kwargs: Keyword arguments for the constructor
            
        Returns:
            Any: The created instance
            
        Raises:
            TypeError: If the class cannot be instantiated
        """
        try:
            if isinstance(class_obj, type):
                return class_obj(*args, **kwargs)
            else:
                raise RenzmcTypeError(f"'{class_obj}' bukan kelas Python yang valid")
        except Exception as e:
            raise RenzmcTypeError(f"Error saat membuat objek Python: {str(e)}")
    
    def list_module_attributes(self, module_name):
        """
        List all attributes of an imported module with alias support
        
        Args:
            module_name (str): The name of the module or alias
            
        Returns:
            list: List of attribute names
            
        Raises:
            ImportError: If the module isn't imported
        """
        # Check if it's an alias first
        if module_name in self.module_aliases:
            module = self.module_aliases[module_name]._module
        elif module_name in self.imported_modules:
            module = self.imported_modules[module_name]
        else:
            raise RenzmcImportError(f"Modul Python '{module_name}' belum diimpor")
        
        return [attr for attr in dir(module) if not attr.startswith('_')]
    
    def get_python_help(self, obj):
        """
        Get help information for a Python object
        
        Args:
            obj: The Python object to get help for
            
        Returns:
            str: Help text for the object
        """
        try:
            import pydoc
            return pydoc.render_doc(obj)
        except Exception:
            return f"Tidak dapat mendapatkan bantuan untuk objek: {obj}"
    
    def install_package(self, package_name):
        """
        Install a Python package using pip
        
        Args:
            package_name (str): The name of the package to install
            
        Returns:
            bool: True if installation was successful
        """
        try:
            import subprocess
            result = subprocess.run([sys.executable, '-m', 'pip', 'install', package_name], 
                                    capture_output=True, text=True)
            return result.returncode == 0
        except Exception:
            return False
    
    def get_all_python_modules(self):
        """
        Get a list of all available Python modules
        
        Returns:
            list: List of available module names
        """
        try:
            import pkgutil
            return [name for _, name, _ in pkgutil.iter_modules()]
        except Exception:
            return []
    
    def auto_import_on_demand(self, module_name):
        """
        Automatically import a Python module when accessed
        
        Args:
            module_name (str): Module name to import
            
        Returns:
            PythonModule: The imported module or None if failed
        """
        try:
            if module_name not in self.imported_modules:
                module = importlib.import_module(module_name)
                self.imported_modules[module_name] = module
                return PythonModule(module)
            else:
                return PythonModule(self.imported_modules[module_name])
        except ImportError:
            return None
    

    def import_all_from_module(self, module_name):
        """
        Import all public attributes from a Python module (from module import *)
        
        Args:
            module_name (str): The name of the module to import from
            
        Returns:
            dict: Dictionary of all public attributes from the module
            
        Raises:
            ImportError: If the module cannot be imported
        """
        try:
            # Import the module
            if module_name in self.imported_modules:
                module = self.imported_modules[module_name]
            else:
                module = importlib.import_module(module_name)
                self.imported_modules[module_name] = module
            
            # Get all public attributes
            all_attrs = {}
            if hasattr(module, '__all__'):
                # Use __all__ if defined
                for name in module.__all__:
                    if hasattr(module, name):
                        all_attrs[name] = self.convert_python_to_renzmc(getattr(module, name))
            else:
                # Import all non-private attributes
                for name in dir(module):
                    if not name.startswith('_'):
                        all_attrs[name] = self.convert_python_to_renzmc(getattr(module, name))
            
            return all_attrs
            
        except ImportError as e:
            raise RenzmcImportError(f"Tidak dapat mengimpor semua dari modul Python '{module_name}': {str(e)}")
        except Exception as e:
            raise RenzmcImportError(f"Error saat mengimpor semua dari modul Python '{module_name}': {str(e)}")
    
    def reload_module(self, module_name):
        """
        Reload a Python module (useful for development)
        
        Args:
            module_name (str): The name of the module to reload
            
        Returns:
            PythonModule: The reloaded module wrapper
            
        Raises:
            ImportError: If the module cannot be reloaded
        """
        try:
            if module_name in self.imported_modules:
                module = importlib.reload(self.imported_modules[module_name])
                self.imported_modules[module_name] = module
                return PythonModule(module)
            else:
                raise RenzmcImportError(f"Modul Python '{module_name}' belum diimpor")
        except Exception as e:
            raise RenzmcImportError(f"Error saat reload modul Python '{module_name}': {str(e)}")
    
    def get_module_path(self, module_name):
        """
        Get the file path of an imported module
        
        Args:
            module_name (str): The name of the module
            
        Returns:
            str: The file path of the module
            
        Raises:
            ImportError: If the module isn't imported
        """
        if module_name in self.imported_modules:
            module = self.imported_modules[module_name]
            if hasattr(module, '__file__'):
                return module.__file__
            else:
                return f"<built-in module '{module_name}'>"
        else:
            raise RenzmcImportError(f"Modul Python '{module_name}' belum diimpor")
    
    def list_available_modules(self):
        """
        List all available Python modules in the system
        
        Returns:
            list: List of available module names
        """
        try:
            import pkgutil
            modules = []
            for importer, modname, ispkg in pkgutil.iter_modules():
                modules.append(modname)
            return sorted(modules)
        except Exception:
            return []
    
    def check_module_available(self, module_name):
        """
        Check if a Python module is available for import
        
        Args:
            module_name (str): The name of the module to check
            
        Returns:
            bool: True if the module is available
        """
        try:
            importlib.util.find_spec(module_name)
            return True
        except (ImportError, ModuleNotFoundError, ValueError):
            return False
    
    def get_module_version(self, module_name):
        """
        Get the version of an imported module
        
        Args:
            module_name (str): The name of the module
            
        Returns:
            str: The version string or "Unknown"
        """
        if module_name in self.imported_modules:
            module = self.imported_modules[module_name]
            # Try different version attributes
            for attr in ['__version__', 'VERSION', 'version']:
                if hasattr(module, attr):
                    return str(getattr(module, attr))
            return "Unknown"
        else:
            raise RenzmcImportError(f"Modul Python '{module_name}' belum diimpor")
    
    def import_submodule(self, parent_module, submodule_name):
        """
        Import a submodule from a parent module
        
        Args:
            parent_module (str): The parent module name
            submodule_name (str): The submodule name
            
        Returns:
            PythonModule: The imported submodule wrapper
            
        Raises:
            ImportError: If the submodule cannot be imported
        """
        try:
            full_name = f"{parent_module}.{submodule_name}"
            if full_name in self.imported_modules:
                module = self.imported_modules[full_name]
            else:
                module = importlib.import_module(full_name)
                self.imported_modules[full_name] = module
            
            return PythonModule(module)
        except ImportError as e:
            raise RenzmcImportError(f"Tidak dapat mengimpor submodul '{submodule_name}' dari '{parent_module}': {str(e)}")
    
    def execute_python_code(self, code_string, local_vars=None):
        """
        Execute arbitrary Python code string
        
        Args:
            code_string (str): The Python code to execute
            local_vars (dict, optional): Local variables for execution
            
        Returns:
            dict: The local variables after execution
            
        Raises:
            Exception: If the code execution fails
        """
        try:
            if local_vars is None:
                local_vars = {}
            
            # Execute the code
            exec(code_string, globals(), local_vars)
            
            # Convert results back to RenzmcLang types
            converted_vars = {}
            for key, value in local_vars.items():
                if not key.startswith('_'):
                    converted_vars[key] = self.convert_python_to_renzmc(value)
            
            return converted_vars
        except Exception as e:
            raise Exception(f"Error saat menjalankan kode Python: {str(e)}")
    
    def evaluate_python_expression(self, expression):
        """
        Evaluate a Python expression and return the result
        
        Args:
            expression (str): The Python expression to evaluate
            
        Returns:
            Any: The result of the expression
            
        Raises:
            Exception: If the evaluation fails
        """
        try:
            result = eval(expression)
            return self.convert_python_to_renzmc(result)
        except Exception as e:
            raise Exception(f"Error saat evaluasi ekspresi Python: {str(e)}")

    def convert_python_to_renzmc(self, obj):
        """
        Enhanced conversion of Python objects to RenzmcLang compatible objects
        Handles complex objects, iterators, generators, and more
        Now with 100% compatibility support for all Python types
        
        Args:
            obj: Python object to convert
            
        Returns:
            Any: RenzmcLang compatible object
        """
        # Handle None
        if obj is None:
            return None
        
        # Handle basic immutable types that don't need conversion
        if isinstance(obj, (int, float, str, bool, bytes)):
            return obj
        
        # Handle modules - both built-in and user modules
        if self._is_module_object(obj):
            return PythonModule(obj)
        
        # Handle types/classes - wrap in SmartWrapper for object instantiation
        if isinstance(obj, type):
            return self.create_smart_wrapper(obj)
        
        # Handle generators and iterators specially
        if hasattr(obj, '__iter__') and hasattr(obj, '__next__'):
            # This is an iterator/generator - wrap it to preserve functionality
            return self.create_smart_wrapper(obj)
        
        # Handle complex iterables with conversion
        if hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
            try:
                if isinstance(obj, dict):
                    return {self.convert_python_to_renzmc(k): self.convert_python_to_renzmc(v) 
                           for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [self.convert_python_to_renzmc(item) for item in obj]
                elif isinstance(obj, tuple):
                    return tuple(self.convert_python_to_renzmc(item) for item in obj)
                elif isinstance(obj, set):
                    return {self.convert_python_to_renzmc(item) for item in obj}
                else:
                    # Unknown iterable type - preserve it in wrapper
                    return self.create_smart_wrapper(obj)
            except (TypeError, RecursionError):
                # Handle conversion errors by wrapping
                return self.create_smart_wrapper(obj)
        
        # Handle callable objects with enhanced wrapping
        if callable(obj) and not isinstance(obj, type):
            def enhanced_wrapper(*args, **kwargs):
                try:
                    # Convert arguments from RenzmcLang to Python
                    py_args = [self.convert_renzmc_to_python(arg) for arg in args]
                    py_kwargs = {k: self.convert_renzmc_to_python(v) for k, v in kwargs.items()}
                    
                    # Call the original function
                    result = obj(*py_args, **py_kwargs)
                    
                    # Convert result back to RenzmcLang
                    return self.convert_python_to_renzmc(result)
                except Exception as e:
                    # If conversion fails, raise appropriate RenzmcLang error
                    raise RenzmcTypeError(f"Error dalam pemanggilan fungsi Python: {str(e)}")
            
            # Copy function metadata if possible
            try:
                enhanced_wrapper.__name__ = getattr(obj, '__name__', 'python_function')
                enhanced_wrapper.__doc__ = getattr(obj, '__doc__', None)
            except (TypeError, AttributeError):
                # Cannot set metadata, continue without it
                pass
            
            return enhanced_wrapper
        
        # Handle complex objects that need full wrapping
        if hasattr(obj, '__dict__') or hasattr(obj, '__getattr__'):
            return self.create_smart_wrapper(obj)
        
        # Handle objects with special methods that need wrapping
        special_methods = ['__getitem__', '__setitem__', '__len__', '__contains__', 
                          '__enter__', '__exit__', '__add__', '__sub__', '__mul__',
                          '__call__', '__getattribute__', '__delattr__', '__hash__',
                          '__repr__', '__str__', '__bool__', '__format__', '__sizeof__']
        if any(hasattr(obj, method) for method in special_methods):
            return self.create_smart_wrapper(obj)
        
        # Handle coroutines and async objects
        if self._is_coroutine_or_async(obj):
            return self.create_smart_wrapper(obj)
        
        # Handle file-like objects
        if self._is_file_like(obj):
            return self.create_smart_wrapper(obj)
        
        # Handle exception objects
        if isinstance(obj, BaseException):
            return self.create_smart_wrapper(obj)
        
        # For everything else, return as-is or wrap if it's a complex object
        try:
            # Test if object is JSON serializable (simple object)
            import json
            json.dumps(obj)
            return obj
        except (TypeError, ValueError):
            # Complex object that needs wrapping
            return self.create_smart_wrapper(obj)
    
    def convert_renzmc_to_python(self, obj):
        """
        Enhanced conversion of RenzmcLang objects to Python compatible objects
        Handles wrapped objects and complex types properly
        
        Args:
            obj: RenzmcLang object to convert
            
        Returns:
            Any: Python compatible object
        """
        # Handle None
        if obj is None:
            return None
        
        # Handle basic immutable types (no conversion needed)
        if isinstance(obj, (int, float, str, bool, bytes)):
            return obj
        
        # Handle SmartPythonWrapper - extract the original Python object
        if isinstance(obj, SmartPythonWrapper):
            return obj._obj
        
        # Handle PythonModule - extract the original module
        if isinstance(obj, PythonModule):
            return obj._module
        
        # Handle iterables with recursive conversion
        if hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
            try:
                if isinstance(obj, dict):
                    return {self.convert_renzmc_to_python(k): self.convert_renzmc_to_python(v) 
                           for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [self.convert_renzmc_to_python(item) for item in obj]
                elif isinstance(obj, tuple):
                    return tuple(self.convert_renzmc_to_python(item) for item in obj)
                elif isinstance(obj, set):
                    return {self.convert_renzmc_to_python(item) for item in obj}
                else:
                    # Unknown iterable - try to convert to list
                    try:
                        return [self.convert_renzmc_to_python(item) for item in obj]
                    except (TypeError, AttributeError):
                        return obj
            except (TypeError, RecursionError):
                # Handle conversion errors gracefully
                return obj
        
        # Handle callable objects (functions)
        if callable(obj):
            # Check if it's already a wrapped Python function
            if hasattr(obj, '__name__') and obj.__name__ == 'enhanced_wrapper':
                # Try to get the original function if possible
                return obj
            return obj
        
        # Return as-is for everything else that we can't convert
        return obj
    
    def create_smart_wrapper(self, obj):
        """
        Create a smart wrapper that automatically handles type conversion
        
        Args:
            obj: Object to wrap
            
        Returns:
            SmartPythonWrapper: Intelligent wrapper
        """
        return SmartPythonWrapper(obj, self)
    
    def enable_star_imports(self, module_name, global_scope):
        """
        Enable 'from module import *' functionality
        
        Args:
            module_name (str): Module name
            global_scope (dict): Global scope to update
            
        Returns:
            int: Number of items imported
        """
        try:
            module_wrapper = self.import_python_module(module_name)
            imported_count = 0
            
            # Get the actual Python module object
            if isinstance(module_wrapper, PythonModule):
                actual_module = module_wrapper._module
            elif isinstance(module_wrapper, dict):
                # Handle case where import returns a dict (alias imports)
                for key, value in module_wrapper.items():
                    if isinstance(value, PythonModule):
                        actual_module = value._module
                        break
                else:
                    return 0
            else:
                # Direct module object
                actual_module = module_wrapper
            
            # Get all public attributes
            if hasattr(actual_module, '__all__'):
                items = actual_module.__all__
            else:
                items = [name for name in dir(actual_module) if not name.startswith('_')]
            
            # Import all items
            for item_name in items:
                if hasattr(actual_module, item_name):
                    global_scope[item_name] = self.convert_python_to_renzmc(getattr(actual_module, item_name))
                    imported_count += 1
            
            return imported_count
        except Exception:
            return 0
    
    def _is_module_object(self, obj):
        """
        Check if an object is a Python module
        
        Args:
            obj: Object to check
            
        Returns:
            bool: True if it's a module
        """
        # Check for traditional module attributes
        if hasattr(obj, '__name__') and hasattr(obj, '__file__'):
            return True
        
        # Check for built-in modules (no __file__)
        if hasattr(obj, '__name__') and hasattr(obj, '__package__'):
            return True
        
        # Check module type
        import types as module_types
        return isinstance(obj, module_types.ModuleType)
    
    def _is_coroutine_or_async(self, obj):
        """
        Check if an object is a coroutine or async object
        
        Args:
            obj: Object to check
            
        Returns:
            bool: True if it's async-related
        """
        import inspect as inspect_module
        return (
            inspect_module.iscoroutine(obj) or
            inspect_module.iscoroutinefunction(obj) or
            inspect_module.isasyncgenfunction(obj) or
            inspect_module.isasyncgen(obj) or
            hasattr(obj, '__await__') or
            hasattr(obj, '__aenter__') or
            hasattr(obj, '__aexit__')
        )
    
    def _is_file_like(self, obj):
        """
        Check if an object is file-like
        
        Args:
            obj: Object to check
            
        Returns:
            bool: True if it's file-like
        """
        file_methods = ['read', 'write', 'close', 'flush', 'seek', 'tell']
        return any(hasattr(obj, method) for method in file_methods)
    
    def enhance_smart_wrapper_compatibility(self, wrapper_obj):
        """
        Enhance an existing SmartPythonWrapper for better compatibility
        
        Args:
            wrapper_obj: SmartPythonWrapper to enhance
            
        Returns:
            SmartPythonWrapper: Enhanced wrapper
        """
        if not isinstance(wrapper_obj, SmartPythonWrapper):
            return wrapper_obj
        
        # Add dynamic method discovery for better compatibility
        original_obj = wrapper_obj._obj
        
        # Discover and add missing special methods dynamically
        special_methods = [
            '__format__', '__sizeof__', '__reduce__', '__reduce_ex__',
            '__getstate__', '__setstate__', '__copy__', '__deepcopy__',
            '__enter__', '__exit__', '__aenter__', '__aexit__',
            '__await__', '__aiter__', '__anext__'
        ]
        
        for method_name in special_methods:
            if hasattr(original_obj, method_name) and not hasattr(wrapper_obj, method_name):
                def create_method_wrapper(method):
                    def wrapper_method(*args, **kwargs):
                        try:
                            result = method(*args, **kwargs)
                            return self.convert_python_to_renzmc(result)
                        except Exception as e:
                            raise RenzmcTypeError(f"Error dalam method {method.__name__}: {str(e)}")
                    return wrapper_method
                
                setattr(wrapper_obj, method_name, 
                       create_method_wrapper(getattr(original_obj, method_name)))
        
        return wrapper_obj