"""
Utility functions for RenzmcLang

This module provides utility functions for the RenzmcLang language.
"""

import os
import sys
import importlib
import inspect
import re
import json
import datetime
import time
import hashlib
import uuid
import base64
import urllib.parse
import urllib.request
import asyncio
from typing import Any, List, Dict, Set, Tuple, Optional, Union, Callable

def is_identifier(name):
    """
    Check if a name is a valid identifier
    
    Args:
        name (str): The name to check
        
    Returns:
        bool: True if the name is a valid identifier, False otherwise
    """
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name) is not None

def is_keyword(name):
    """
    Check if a name is a keyword
    
    Args:
        name (str): The name to check
        
    Returns:
        bool: True if the name is a keyword, False otherwise
    """
    keywords = [
        'jika', 'kalau', 'maka', 'tidak', 'lainnya', 'selesai', 'selama', 'ulangi',
        'kali', 'untuk', 'setiap', 'dari', 'sampai', 'lanjut', 'berhenti', 'coba',
        'tangkap', 'akhirnya', 'simpan', 'ke', 'dalam', 'itu', 'adalah', 'sebagai',
        'tampilkan', 'tulis', 'cetak', 'tunjukkan', 'tanya', 'buat', 'fungsi',
        'dengan', 'parameter', 'panggil', 'jalankan', 'kembali', 'hasil', 'kelas',
        'metode', 'konstruktor', 'warisi', 'gunakan', 'impor', 'impor_python',
        'modul', 'paket', 'lambda', 'async', 'await', 'yield', 'dekorator', 'tipe',
        'jenis_data', 'generator', 'asinkron', 'dan', 'atau', 'benar', 'salah',
        'self', 'ini'
    ]
    return name in keywords

def format_code(code):
    """
    Format code with proper indentation
    
    Args:
        code (str): The code to format
        
    Returns:
        str: The formatted code
    """
    lines = code.split('\n')
    result = []
    indent_level = 0
    
    for line in lines:
        stripped = line.strip()
        
        # Check for indentation decrease
        if stripped in ['selesai', 'kalau tidak', 'kalau tidak jika', 'akhirnya', 'tangkap']:
            indent_level = max(0, indent_level - 1)
        
        # Add the line with proper indentation
        if stripped:
            result.append('    ' * indent_level + stripped)
        else:
            result.append('')
        
        # Check for indentation increase
        if stripped.endswith(':') or any(stripped.startswith(keyword) for keyword in [
            'jika', 'kalau tidak jika', 'kalau tidak', 'selama', 'untuk setiap', 'ulangi',
            'buat fungsi', 'buat kelas', 'buat metode', 'konstruktor', 'coba', 'tangkap'
        ]):
            indent_level += 1
    
    return '\n'.join(result)

def parse_type_annotation(annotation):
    """
    Parse a type annotation
    
    Args:
        annotation (str): The type annotation
        
    Returns:
        type: The parsed type
    """
    if annotation == 'int' or annotation == 'bilangan_bulat':
        return int
    elif annotation == 'float' or annotation == 'desimal':
        return float
    elif annotation == 'str' or annotation == 'teks':
        return str
    elif annotation == 'bool' or annotation == 'boolean':
        return bool
    elif annotation == 'list' or annotation == 'daftar':
        return list
    elif annotation == 'dict' or annotation == 'kamus':
        return dict
    elif annotation == 'set' or annotation == 'himpunan':
        return set
    elif annotation == 'tuple' or annotation == 'tupel':
        return tuple
    elif annotation == 'None' or annotation == 'kosong':
        return type(None)
    elif annotation == 'Any' or annotation == 'apapun':
        return Any
    elif annotation.startswith('List[') or annotation.startswith('Daftar['):
        inner = annotation[annotation.index('[') + 1:annotation.rindex(']')]
        return List[parse_type_annotation(inner)]
    elif annotation.startswith('Dict[') or annotation.startswith('Kamus['):
        inner = annotation[annotation.index('[') + 1:annotation.rindex(']')]
        key_type, value_type = inner.split(',')
        return Dict[parse_type_annotation(key_type.strip()), parse_type_annotation(value_type.strip())]
    elif annotation.startswith('Set[') or annotation.startswith('Himpunan['):
        inner = annotation[annotation.index('[') + 1:annotation.rindex(']')]
        return Set[parse_type_annotation(inner)]
    elif annotation.startswith('Tuple[') or annotation.startswith('Tupel['):
        inner = annotation[annotation.index('[') + 1:annotation.rindex(']')]
        types = [parse_type_annotation(t.strip()) for t in inner.split(',')]
        return Tuple[tuple(types)]
    elif annotation.startswith('Optional[') or annotation.startswith('Opsional['):
        inner = annotation[annotation.index('[') + 1:annotation.rindex(']')]
        return Optional[parse_type_annotation(inner)]
    elif annotation.startswith('Union[') or annotation.startswith('Gabungan['):
        inner = annotation[annotation.index('[') + 1:annotation.rindex(']')]
        types = [parse_type_annotation(t.strip()) for t in inner.split(',')]
        return Union[tuple(types)]
    elif annotation.startswith('Callable[') or annotation.startswith('Fungsi['):
        return Callable
    else:
        # Custom type
        return annotation

def check_type(value, type_annotation):
    """
    Check if a value matches a type annotation
    
    Args:
        value: The value to check
        type_annotation: The type annotation
        
    Returns:
        bool: True if the value matches the type annotation, False otherwise
    """
    if type_annotation is Any:
        return True
    
    if isinstance(type_annotation, str):
        type_annotation = parse_type_annotation(type_annotation)
    
    if isinstance(type_annotation, type):
        return isinstance(value, type_annotation)
    
    origin = getattr(type_annotation, '__origin__', None)
    args = getattr(type_annotation, '__args__', None)
    
    if origin is list or origin is List:
        return isinstance(value, list) and all(check_type(item, args[0]) for item in value)
    elif origin is dict or origin is Dict:
        return isinstance(value, dict) and all(check_type(k, args[0]) and check_type(v, args[1]) for k, v in value.items())
    elif origin is set or origin is Set:
        return isinstance(value, set) and all(check_type(item, args[0]) for item in value)
    elif origin is tuple or origin is Tuple:
        return isinstance(value, tuple) and len(value) == len(args) and all(check_type(value[i], args[i]) for i in range(len(args)))
    elif origin is Union:
        return any(check_type(value, arg) for arg in args)
    elif origin is Optional:
        return value is None or check_type(value, args[0])
    elif origin is Callable:
        return callable(value)
    
    return False

def format_error_message(error, source_code=None):
    """
    Format an error message with source code context
    
    Args:
        error: The error to format
        source_code (str, optional): The source code where the error occurred
        
    Returns:
        str: The formatted error message
    """
    if not hasattr(error, 'line') or not hasattr(error, 'column') or error.line is None or error.column is None:
        return str(error)
    
    result = f"Error: {error.message}\n"
    result += f"Pada baris {error.line}, kolom {error.column}\n"
    
    # Use the source code from the error if available, otherwise use the provided one
    code_to_use = error.source_code if hasattr(error, 'source_code') and error.source_code else source_code
    
    if code_to_use:
        lines = code_to_use.split('\n')
        if 0 <= error.line - 1 < len(lines):
            # Get the line where the error occurred
            line = lines[error.line - 1]
            result += f"\n{error.line} | {line}\n"
            
            # Add a pointer to the column
            result += " " * (len(str(error.line)) + 3 + error.column - 1) + "^\n"
            
            # Add context (lines before and after)
            context_lines = 2  # Number of lines to show before and after
            start_line = max(0, error.line - 1 - context_lines)
            end_line = min(len(lines), error.line - 1 + context_lines + 1)
            
            if start_line > 0:
                result += "...\n"
            
            for i in range(start_line, end_line):
                if i == error.line - 1:
                    continue  # Skip the error line as it's already shown
                result += f"{i+1} | {lines[i]}\n"
            
            if end_line < len(lines):
                result += "...\n"
    
    return result

def load_module(module_name):
    """
    Load a module
    
    Args:
        module_name (str): The name of the module to load
        
    Returns:
        module: The loaded module
        
    Raises:
        ImportError: If the module cannot be imported
    """
    try:
        return importlib.import_module(module_name)
    except ImportError:
        raise ImportError(f"Tidak dapat mengimpor modul '{module_name}'")

def get_module_functions(module):
    """
    Get the functions in a module
    
    Args:
        module: The module to get the functions from
        
    Returns:
        dict: The functions in the module
    """
    return {
        name: obj
        for name, obj in inspect.getmembers(module, inspect.isfunction)
        if not name.startswith('_')
    }

def get_module_classes(module):
    """
    Get the classes in a module
    
    Args:
        module: The module to get the classes from
        
    Returns:
        dict: The classes in the module
    """
    return {
        name: obj
        for name, obj in inspect.getmembers(module, inspect.isclass)
        if not name.startswith('_')
    }

def get_module_variables(module):
    """
    Get the variables in a module
    
    Args:
        module: The module to get the variables from
        
    Returns:
        dict: The variables in the module
    """
    return {
        name: obj
        for name, obj in inspect.getmembers(module)
        if not name.startswith('_') and not inspect.isfunction(obj) and not inspect.isclass(obj)
    }

def get_class_methods(cls):
    """
    Get the methods in a class
    
    Args:
        cls: The class to get the methods from
        
    Returns:
        dict: The methods in the class
    """
    return {
        name: obj
        for name, obj in inspect.getmembers(cls, inspect.isfunction)
        if not name.startswith('_')
    }

def get_class_attributes(cls):
    """
    Get the attributes in a class
    
    Args:
        cls: The class to get the attributes from
        
    Returns:
        dict: The attributes in the class
    """
    return {
        name: obj
        for name, obj in inspect.getmembers(cls)
        if not name.startswith('_') and not inspect.isfunction(obj) and not inspect.ismethod(obj)
    }

def get_function_signature(func):
    """
    Get the signature of a function
    
    Args:
        func: The function to get the signature of
        
    Returns:
        str: The signature
    """
    return str(inspect.signature(func))

def get_function_parameters(func):
    """
    Get the parameters of a function
    
    Args:
        func: The function to get the parameters of
        
    Returns:
        list: The parameters
    """
    return list(inspect.signature(func).parameters.keys())

def get_function_defaults(func):
    """
    Get the default values of a function's parameters
    
    Args:
        func: The function to get the defaults of
        
    Returns:
        dict: The default values
    """
    signature = inspect.signature(func)
    return {
        name: param.default
        for name, param in signature.parameters.items()
        if param.default is not inspect.Parameter.empty
    }

def get_function_annotations(func):
    """
    Get the annotations of a function
    
    Args:
        func: The function to get the annotations of
        
    Returns:
        dict: The annotations
    """
    return func.__annotations__

def get_function_doc(func):
    """
    Get the docstring of a function
    
    Args:
        func: The function to get the docstring of
        
    Returns:
        str: The docstring
    """
    return func.__doc__

def get_function_source(func):
    """
    Get the source code of a function
    
    Args:
        func: The function to get the source code of
        
    Returns:
        str: The source code
    """
    return inspect.getsource(func)

def is_async_function(func):
    """
    Check if a function is async
    
    Args:
        func: The function to check
        
    Returns:
        bool: True if the function is async, False otherwise
    """
    return asyncio.iscoroutinefunction(func)

def run_async(coro):
    """
    Run an async function
    
    Args:
        coro: The coroutine to run
        
    Returns:
        Any: The result of the coroutine
    """
    return asyncio.run(coro)

def wait_all_async(coros):
    """
    Wait for all async functions to complete
    
    Args:
        coros: List of coroutines to wait for
        
    Returns:
        list: The results of the coroutines
    """
    return asyncio.run(asyncio.gather(*coros))

def create_async_function(func):
    """
    Create an async function from a regular function
    
    Args:
        func: The function to convert
        
    Returns:
        function: The async function
    """
    async def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def json_to_dict(json_str):
    """
    Convert JSON to a dictionary
    
    Args:
        json_str (str): The JSON string
        
    Returns:
        dict: The dictionary
        
    Raises:
        ValueError: If the JSON is invalid
    """
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON tidak valid: {str(e)}")

def dict_to_json(dictionary):
    """
    Convert a dictionary to JSON
    
    Args:
        dictionary (dict): The dictionary
        
    Returns:
        str: The JSON string
        
    Raises:
        TypeError: If the dictionary cannot be converted to JSON
    """
    try:
        return json.dumps(dictionary, ensure_ascii=False)
    except TypeError as e:
        raise TypeError(f"Tidak dapat mengkonversi kamus ke JSON: {str(e)}")

def get_current_time():
    """
    Get the current time
    
    Returns:
        datetime: The current time
    """
    return datetime.datetime.now()

def format_time(dt, format_str='%Y-%m-%d %H:%M:%S'):
    """
    Format a datetime
    
    Args:
        dt (datetime): The datetime to format
        format_str (str, optional): The format string
        
    Returns:
        str: The formatted datetime
    """
    return dt.strftime(format_str)

def parse_time(time_str, format_str='%Y-%m-%d %H:%M:%S'):
    """
    Parse a time string
    
    Args:
        time_str (str): The time string to parse
        format_str (str, optional): The format string
        
    Returns:
        datetime: The parsed datetime
        
    Raises:
        ValueError: If the time string is invalid
    """
    try:
        return datetime.datetime.strptime(time_str, format_str)
    except ValueError:
        raise ValueError(f"Format waktu tidak valid: '{time_str}' (format: '{format_str}')")

def get_timestamp():
    """
    Get the current timestamp
    
    Returns:
        float: The current timestamp
    """
    return time.time()

def timestamp_to_datetime(timestamp):
    """
    Convert a timestamp to a datetime
    
    Args:
        timestamp (float): The timestamp
        
    Returns:
        datetime: The datetime
    """
    return datetime.datetime.fromtimestamp(timestamp)

def datetime_to_timestamp(dt):
    """
    Convert a datetime to a timestamp
    
    Args:
        dt (datetime): The datetime
        
    Returns:
        float: The timestamp
    """
    return dt.timestamp()

def hash_string(string, algorithm='sha256'):
    """
    Hash a string
    
    Args:
        string (str): The string to hash
        algorithm (str, optional): The hash algorithm
        
    Returns:
        str: The hash
        
    Raises:
        ValueError: If the algorithm is invalid
    """
    if algorithm == 'md5':
        return hashlib.md5(string.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(string.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(string.encode()).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(string.encode()).hexdigest()
    else:
        raise ValueError(f"Algoritma hash tidak valid: '{algorithm}'")

def generate_uuid():
    """
    Generate a UUID
    
    Returns:
        str: The UUID
    """
    return str(uuid.uuid4())

def base64_encode(string):
    """
    Base64 encode a string
    
    Args:
        string (str): The string to encode
        
    Returns:
        str: The encoded string
    """
    return base64.b64encode(string.encode()).decode()

def base64_decode(string):
    """
    Base64 decode a string
    
    Args:
        string (str): The string to decode
        
    Returns:
        str: The decoded string
        
    Raises:
        ValueError: If the string is not valid Base64
    """
    try:
        return base64.b64decode(string.encode()).decode()
    except Exception:
        raise ValueError(f"String Base64 tidak valid: '{string}'")

def url_encode(string):
    """
    URL encode a string
    
    Args:
        string (str): The string to encode
        
    Returns:
        str: The encoded string
    """
    return urllib.parse.quote(string)

def url_decode(string):
    """
    URL decode a string
    
    Args:
        string (str): The string to decode
        
    Returns:
        str: The decoded string
    """
    return urllib.parse.unquote(string)

def http_get(url, headers=None):
    """
    Make an HTTP GET request
    
    Args:
        url (str): The URL to request
        headers (dict, optional): The headers to send
        
    Returns:
        dict: The response
        
    Raises:
        urllib.error.URLError: If there is an error making the request
    """
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req) as response:
        return {
            'status': response.status,
            'headers': dict(response.headers),
            'content': response.read().decode('utf-8')
        }

def http_post(url, data, headers=None):
    """
    Make an HTTP POST request
    
    Args:
        url (str): The URL to request
        data (dict): The data to send
        headers (dict, optional): The headers to send
        
    Returns:
        dict: The response
        
    Raises:
        urllib.error.URLError: If there is an error making the request
    """
    data_bytes = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=data_bytes, headers=headers or {}, method='POST')
    with urllib.request.urlopen(req) as response:
        return {
            'status': response.status,
            'headers': dict(response.headers),
            'content': response.read().decode('utf-8')
        }

def file_exists(path):
    """
    Check if a file exists
    
    Args:
        path (str): The path to check
        
    Returns:
        bool: True if the file exists, False otherwise
    """
    return os.path.exists(path)

def is_file(path):
    """
    Check if a path is a file
    
    Args:
        path (str): The path to check
        
    Returns:
        bool: True if the path is a file, False otherwise
    """
    return os.path.isfile(path)

def is_directory(path):
    """
    Check if a path is a directory
    
    Args:
        path (str): The path to check
        
    Returns:
        bool: True if the path is a directory, False otherwise
    """
    return os.path.isdir(path)

def get_file_size(path):
    """
    Get the size of a file
    
    Args:
        path (str): The path to the file
        
    Returns:
        int: The size of the file in bytes
        
    Raises:
        FileNotFoundError: If the file does not exist
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File tidak ditemukan: '{path}'")
    
    return os.path.getsize(path)

def get_file_modification_time(path):
    """
    Get the modification time of a file
    
    Args:
        path (str): The path to the file
        
    Returns:
        float: The modification time as a timestamp
        
    Raises:
        FileNotFoundError: If the file does not exist
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File tidak ditemukan: '{path}'")
    
    return os.path.getmtime(path)

def list_directory(path='.'):
    """
    List the contents of a directory
    
    Args:
        path (str, optional): The path to the directory
        
    Returns:
        list: The contents of the directory
        
    Raises:
        FileNotFoundError: If the directory does not exist
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Direktori tidak ditemukan: '{path}'")
    
    if not os.path.isdir(path):
        raise NotADirectoryError(f"Bukan direktori: '{path}'")
    
    return os.listdir(path)

def create_directory(path):
    """
    Create a directory
    
    Args:
        path (str): The path to the directory
        
    Raises:
        FileExistsError: If the directory already exists
    """
    if os.path.exists(path):
        if os.path.isdir(path):
            raise FileExistsError(f"Direktori sudah ada: '{path}'")
        else:
            raise FileExistsError(f"File sudah ada dengan nama yang sama: '{path}'")
    
    os.makedirs(path)

def remove_file(path):
    """
    Remove a file
    
    Args:
        path (str): The path to the file
        
    Raises:
        FileNotFoundError: If the file does not exist
        IsADirectoryError: If the path is a directory
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File tidak ditemukan: '{path}'")
    
    if os.path.isdir(path):
        raise IsADirectoryError(f"Tidak dapat menghapus direktori dengan fungsi ini: '{path}'")
    
    os.remove(path)

def remove_directory(path):
    """
    Remove a directory
    
    Args:
        path (str): The path to the directory
        
    Raises:
        FileNotFoundError: If the directory does not exist
        NotADirectoryError: If the path is not a directory
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Direktori tidak ditemukan: '{path}'")
    
    if not os.path.isdir(path):
        raise NotADirectoryError(f"Bukan direktori: '{path}'")
    
    os.rmdir(path)

def join_path(*paths):
    """
    Join path components
    
    Args:
        *paths: Path components
        
    Returns:
        str: The joined path
    """
    return os.path.join(*paths)

def get_absolute_path(path):
    """
    Get the absolute path
    
    Args:
        path (str): The path
        
    Returns:
        str: The absolute path
    """
    return os.path.abspath(path)

def get_basename(path):
    """
    Get the basename of a path
    
    Args:
        path (str): The path
        
    Returns:
        str: The basename
    """
    return os.path.basename(path)

def get_dirname(path):
    """
    Get the directory name of a path
    
    Args:
        path (str): The path
        
    Returns:
        str: The directory name
    """
    return os.path.dirname(path)

def get_extension(path):
    """
    Get the extension of a file
    
    Args:
        path (str): The path
        
    Returns:
        str: The extension
    """
    return os.path.splitext(path)[1]

def change_extension(path, extension):
    """
    Change the extension of a file
    
    Args:
        path (str): The path
        extension (str): The new extension
        
    Returns:
        str: The path with the new extension
    """
    return os.path.splitext(path)[0] + extension

def normalize_path(path):
    """
    Normalize a path
    
    Args:
        path (str): The path
        
    Returns:
        str: The normalized path
    """
    return os.path.normpath(path)

def get_current_directory():
    """
    Get the current directory
    
    Returns:
        str: The current directory
    """
    return os.getcwd()

def change_directory(path):
    """
    Change the current directory
    
    Args:
        path (str): The path to change to
        
    Raises:
        FileNotFoundError: If the directory does not exist
        NotADirectoryError: If the path is not a directory
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Direktori tidak ditemukan: '{path}'")
    
    if not os.path.isdir(path):
        raise NotADirectoryError(f"Bukan direktori: '{path}'")
    
    os.chdir(path)

def get_environment_variable(name):
    """
    Get an environment variable
    
    Args:
        name (str): The name of the environment variable
        
    Returns:
        str: The value of the environment variable
        
    Raises:
        KeyError: If the environment variable does not exist
    """
    if name not in os.environ:
        raise KeyError(f"Variabel lingkungan tidak ditemukan: '{name}'")
    
    return os.environ[name]

def set_environment_variable(name, value):
    """
    Set an environment variable
    
    Args:
        name (str): The name of the environment variable
        value (str): The value of the environment variable
    """
    os.environ[name] = value

def get_python_version():
    """
    Get the Python version
    
    Returns:
        str: The Python version
    """
    return sys.version

def get_platform():
    """
    Get the platform
    
    Returns:
        str: The platform
    """
    return sys.platform

def get_executable():
    """
    Get the Python executable
    
    Returns:
        str: The Python executable
    """
    return sys.executable

def get_path():
    """
    Get the Python path
    
    Returns:
        list: The Python path
    """
    return sys.path

def add_to_path(path):
    """
    Add a path to the Python path
    
    Args:
        path (str): The path to add
    """
    sys.path.append(path)

def get_modules():
    """
    Get the loaded modules
    
    Returns:
        dict: The loaded modules
    """
    return sys.modules

def get_arguments():
    """
    Get the command line arguments
    
    Returns:
        list: The command line arguments
    """
    return sys.argv

def exit(code=0):
    """
    Exit the program
    
    Args:
        code (int, optional): The exit code
    """
    sys.exit(code)