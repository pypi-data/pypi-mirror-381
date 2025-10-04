"""
Built-in functions for RenzmcLang

This module provides built-in functions for the RenzmcLang language.
"""

import math
import random
import time
import datetime
import os
import subprocess
import json
import re
import base64
import hashlib
import uuid
import urllib.parse
import urllib.request
import sys
import inspect
import asyncio
import shlex
from typing import Any, List, Dict, Set, Tuple, Optional, Union, Callable

# Import RenzmcError for proper exception integration
try:
    from renzmc.core.error import RenzmcError
except ImportError:
    # Fallback if not available
    class RenzmcError(Exception):
        pass

# Custom security exception that integrates with renzmc error system
class SecurityError(RenzmcError):
    """Exception raised for security-related errors"""
    def __init__(self, message, line=None, column=None):
        super().__init__(message, line, column)
        self.message = message

# Basic functions
def panjang(obj):
    """
    Get the length of an object
    
    Args:
        obj: The object to get the length of
        
    Returns:
        int: The length of the object
        
    Raises:
        TypeError: If the object has no length
    """
    try:
        return len(obj)
    except TypeError:
        raise TypeError(f"Objek tipe '{type(obj).__name__}' tidak memiliki panjang")

def jenis(obj):
    """
    Get the type of an object
    
    Args:
        obj: The object to get the type of
        
    Returns:
        str: The type of the object
    """
    return type(obj).__name__

def ke_teks(obj):
    """
    Convert an object to text
    
    Args:
        obj: The object to convert
        
    Returns:
        str: The text representation of the object
    """
    return str(obj)

def ke_angka(obj):
    """
    Convert an object to a number
    
    Args:
        obj: The object to convert
        
    Returns:
        int or float: The number representation of the object
        
    Raises:
        ValueError: If the object cannot be converted to a number
    """
    try:
        # Try to convert to int first
        return int(obj)
    except ValueError:
        try:
            # Then try to convert to float
            return float(obj)
        except ValueError:
            raise ValueError(f"Tidak dapat mengkonversi '{obj}' ke angka")

# String functions
def huruf_besar(text):
    """
    Convert text to uppercase
    
    Args:
        text (str): The text to convert
        
    Returns:
        str: The uppercase text
        
    Raises:
        TypeError: If the input is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.upper()

def huruf_kecil(text):
    """
    Convert text to lowercase
    
    Args:
        text (str): The text to convert
        
    Returns:
        str: The lowercase text
        
    Raises:
        TypeError: If the input is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    return text.lower()

def potong(text, start, end=None):
    """
    Get a substring from a text
    
    Args:
        text (str): The text to get a substring from
        start (int): The start index
        end (int, optional): The end index
        
    Returns:
        str: The substring
        
    Raises:
        TypeError: If the input is not a string
        IndexError: If the indices are out of range
    """
    if not isinstance(text, str):
        raise TypeError(f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'")
    
    try:
        if end is None:
            return text[start:]
        else:
            return text[start:end]
    except IndexError:
        raise IndexError(f"Indeks di luar jangkauan untuk teks '{text}'")

def gabung(separator, *items):
    """
    Join items with a separator
    
    Args:
        separator (str): The separator to use
        *items: The items to join
        
    Returns:
        str: The joined string
        
    Raises:
        TypeError: If the separator is not a string
    """
    if not isinstance(separator, str):
        raise TypeError(f"Pemisah harus berupa teks, bukan '{type(separator).__name__}'")
    
    return separator.join(str(item) for item in items)

def pisah(text, separator=None):
    """
    Split a text by a separator
    
    Args:
        text (str): The text to split
        separator (str, optional): The separator to use
        
    Returns:
        list: The split text
        
    Raises:
        TypeError: If the input is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'")
    
    return text.split(separator)

def ganti(text, old, new):
    """
    Replace occurrences of a substring in a text
    
    Args:
        text (str): The text to replace in
        old (str): The substring to replace
        new (str): The replacement
        
    Returns:
        str: The text with replacements
        
    Raises:
        TypeError: If any input is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'")
    if not isinstance(old, str):
        raise TypeError(f"Argumen kedua harus berupa teks, bukan '{type(old).__name__}'")
    if not isinstance(new, str):
        raise TypeError(f"Argumen ketiga harus berupa teks, bukan '{type(new).__name__}'")
    
    return text.replace(old, new)

def mulai_dengan(text, prefix):
    """
    Check if a text starts with a prefix
    
    Args:
        text (str): The text to check
        prefix (str): The prefix to check for
        
    Returns:
        bool: True if the text starts with the prefix, False otherwise
        
    Raises:
        TypeError: If any input is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'")
    if not isinstance(prefix, str):
        raise TypeError(f"Argumen kedua harus berupa teks, bukan '{type(prefix).__name__}'")
    
    return text.startswith(prefix)

def akhir_dengan(text, suffix):
    """
    Check if a text ends with a suffix
    
    Args:
        text (str): The text to check
        suffix (str): The suffix to check for
        
    Returns:
        bool: True if the text ends with the suffix, False otherwise
        
    Raises:
        TypeError: If any input is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'")
    if not isinstance(suffix, str):
        raise TypeError(f"Argumen kedua harus berupa teks, bukan '{type(suffix).__name__}'")
    
    return text.endswith(suffix)

def berisi(text, substring):
    """
    Check if a text contains a substring
    
    Args:
        text (str): The text to check
        substring (str): The substring to check for
        
    Returns:
        bool: True if the text contains the substring, False otherwise
        
    Raises:
        TypeError: If any input is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argumen pertama harus berupa teks, bukan '{type(text).__name__}'")
    if not isinstance(substring, str):
        raise TypeError(f"Argumen kedua harus berupa teks, bukan '{type(substring).__name__}'")
    
    return substring in text

def hapus_spasi(text):
    """
    Remove leading and trailing whitespace from a text
    
    Args:
        text (str): The text to strip
        
    Returns:
        str: The stripped text
        
    Raises:
        TypeError: If the input is not a string
    """
    if not isinstance(text, str):
        raise TypeError(f"Argumen harus berupa teks, bukan '{type(text).__name__}'")
    
    return text.strip()

# Math functions
def bulat(number):
    """
    Convert a number to an integer
    
    Args:
        number: The number to convert
        
    Returns:
        int: The integer value
        
    Raises:
        ValueError: If the input cannot be converted to an integer
    """
    try:
        return int(number)
    except (ValueError, TypeError):
        raise ValueError(f"Tidak dapat mengkonversi '{number}' ke bilangan bulat")

def desimal(number):
    """
    Convert a number to a decimal
    
    Args:
        number: The number to convert
        
    Returns:
        float: The decimal value
        
    Raises:
        ValueError: If the input cannot be converted to a decimal
    """
    try:
        return float(number)
    except (ValueError, TypeError):
        raise ValueError(f"Tidak dapat mengkonversi '{number}' ke bilangan desimal")

def akar(number):
    """
    Calculate the square root of a number
    
    Args:
        number (int or float): The number to calculate the square root of
        
    Returns:
        float: The square root
        
    Raises:
        ValueError: If the input is negative
    """
    if number < 0:
        raise ValueError("Tidak dapat menghitung akar kuadrat dari bilangan negatif")
    
    return math.sqrt(number)

def pangkat(base, exponent):
    """
    Calculate the power of a number
    
    Args:
        base (int or float): The base
        exponent (int or float): The exponent
        
    Returns:
        int or float: The result
    """
    return base ** exponent

def absolut(number):
    """
    Calculate the absolute value of a number
    
    Args:
        number (int or float): The number
        
    Returns:
        int or float: The absolute value
    """
    return abs(number)

def pembulatan(number):
    """
    Round a number to the nearest integer
    
    Args:
        number (float): The number to round
        
    Returns:
        int: The rounded number
    """
    return round(number)

def pembulatan_atas(number):
    """
    Round a number up to the nearest integer
    
    Args:
        number (float): The number to round
        
    Returns:
        int: The rounded number
    """
    return math.ceil(number)

def pembulatan_bawah(number):
    """
    Round a number down to the nearest integer
    
    Args:
        number (float): The number to round
        
    Returns:
        int: The rounded number
    """
    return math.floor(number)

def sinus(angle):
    """
    Calculate the sine of an angle in radians
    
    Args:
        angle (float): The angle in radians
        
    Returns:
        float: The sine value
    """
    return math.sin(angle)

def cosinus(angle):
    """
    Calculate the cosine of an angle in radians
    
    Args:
        angle (float): The angle in radians
        
    Returns:
        float: The cosine value
    """
    return math.cos(angle)

def tangen(angle):
    """
    Calculate the tangent of an angle in radians
    
    Args:
        angle (float): The angle in radians
        
    Returns:
        float: The tangent value
    """
    return math.tan(angle)

# List functions
def tambah(lst, item):
    """
    Add an item to a list
    
    Args:
        lst (list): The list to add to
        item: The item to add
        
    Returns:
        list: The list with the item added
        
    Raises:
        TypeError: If the first argument is not a list
    """
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'")
    
    lst.append(item)
    return lst

def hapus(lst, item):
    """
    Remove an item from a list
    
    Args:
        lst (list): The list to remove from
        item: The item to remove
        
    Returns:
        list: The list with the item removed
        
    Raises:
        TypeError: If the first argument is not a list
        ValueError: If the item is not in the list
    """
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'")
    
    try:
        lst.remove(item)
        return lst
    except ValueError:
        raise ValueError(f"Item '{item}' tidak ditemukan dalam daftar")

def hapus_pada(lst, index):
    """
    Remove an item at a specific index from a list
    
    Args:
        lst (list): The list to remove from
        index (int): The index to remove at
        
    Returns:
        list: The list with the item removed
        
    Raises:
        TypeError: If the first argument is not a list
        IndexError: If the index is out of range
    """
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'")
    
    try:
        del lst[index]
        return lst
    except IndexError:
        raise IndexError(f"Indeks {index} di luar jangkauan untuk daftar dengan panjang {len(lst)}")

def masukkan(lst, index, item):
    """
    Insert an item at a specific index in a list
    
    Args:
        lst (list): The list to insert into
        index (int): The index to insert at
        item: The item to insert
        
    Returns:
        list: The list with the item inserted
        
    Raises:
        TypeError: If the first argument is not a list
        IndexError: If the index is out of range
    """
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'")
    
    try:
        lst.insert(index, item)
        return lst
    except IndexError:
        raise IndexError(f"Indeks {index} di luar jangkauan untuk daftar dengan panjang {len(lst)}")

def urutkan(lst, terbalik=False):
    """
    Sort a list in-place
    
    Args:
        lst (list): The list to sort
        terbalik (bool, optional): Whether to sort in reverse order
        
    Returns:
        None: Modifies the list in-place
        
    Raises:
        TypeError: If the first argument is not a list
    """
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'")
    
    try:
        lst.sort(reverse=terbalik)
        return None
    except TypeError:
        raise TypeError("Tidak dapat mengurutkan daftar dengan tipe item yang berbeda")

def balikkan(lst):
    """
    Reverse a list in-place
    
    Args:
        lst (list): The list to reverse
        
    Returns:
        None: Modifies the list in-place
        
    Raises:
        TypeError: If the argument is not a list
    """
    if not isinstance(lst, list):
        raise TypeError(f"Argumen harus berupa daftar, bukan '{type(lst).__name__}'")
    
    lst.reverse()
    return None

def hitung(lst, item):
    """
    Count occurrences of an item in a list
    
    Args:
        lst (list): The list to count in
        item: The item to count
        
    Returns:
        int: The number of occurrences
        
    Raises:
        TypeError: If the first argument is not a list
    """
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'")
    
    return lst.count(item)

def indeks(lst, item):
    """
    Find the index of an item in a list
    
    Args:
        lst (list): The list to search in
        item: The item to find
        
    Returns:
        int: The index of the item
        
    Raises:
        TypeError: If the first argument is not a list
        ValueError: If the item is not in the list
    """
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'")
    
    try:
        return lst.index(item)
    except ValueError:
        raise ValueError(f"Item '{item}' tidak ditemukan dalam daftar")

def extend(lst, iterable):
    """
    Extend list with another iterable
    
    Args:
        lst (list): The list to extend
        iterable: The iterable to extend with
        
    Returns:
        list: The extended list
        
    Raises:
        TypeError: If the first argument is not a list
    """
    if not isinstance(lst, list):
        raise TypeError(f"Argumen pertama harus berupa daftar, bukan '{type(lst).__name__}'")
    
    lst.extend(iterable)
    return lst

def salin(obj):
    """
    Create a shallow copy of an object
    
    Args:
        obj: The object to copy (list, dict, set, etc.)
        
    Returns:
        A shallow copy of the object
    """
    import copy
    return copy.copy(obj)

def salin_dalam(obj):
    """
    Create a deep copy of an object
    
    Args:
        obj: The object to copy
        
    Returns:
        A deep copy of the object
    """
    import copy
    return copy.deepcopy(obj)

def minimum(*args):
    """
    Find the minimum value
    
    Args:
        *args: Numbers or a single iterable
        
    Returns:
        The minimum value
        
    Raises:
        ValueError: If no arguments provided
    """
    if len(args) == 0:
        raise ValueError("minimum() memerlukan setidaknya satu argumen")
    
    if len(args) == 1 and hasattr(args[0], '__iter__') and not isinstance(args[0], str):
        return min(args[0])
    else:
        return min(args)

def maksimum(*args):
    """
    Find the maximum value
    
    Args:
        *args: Numbers or a single iterable
        
    Returns:
        The maximum value
        
    Raises:
        ValueError: If no arguments provided
    """
    if len(args) == 0:
        raise ValueError("maksimum() memerlukan setidaknya satu argumen")
    
    if len(args) == 1 and hasattr(args[0], '__iter__') and not isinstance(args[0], str):
        return max(args[0])
    else:
        return max(args)

def jumlah(*args):
    """
    Calculate the sum of numbers
    
    Args:
        *args: Numbers or a single iterable
        
    Returns:
        The sum of all numbers
        
    Raises:
        TypeError: If arguments are not numbers
    """
    if len(args) == 0:
        return 0
    
    if len(args) == 1 and hasattr(args[0], '__iter__') and not isinstance(args[0], str):
        return sum(args[0])
    else:
        return sum(args)

def rata_rata(*args):
    """
    Calculate the average of numbers
    
    Args:
        *args: Numbers or a single iterable
        
    Returns:
        The average of all numbers
        
    Raises:
        ValueError: If no arguments provided
        TypeError: If arguments are not numbers
    """
    if len(args) == 0:
        raise ValueError("rata_rata() memerlukan setidaknya satu argumen")
    
    if len(args) == 1 and hasattr(args[0], '__iter__') and not isinstance(args[0], str):
        items = list(args[0])
        return sum(items) / len(items) if len(items) > 0 else 0
    else:
        return sum(args) / len(args)

# Dictionary functions
def kunci(dictionary):
    """
    Get the keys of a dictionary
    
    Args:
        dictionary (dict): The dictionary to get the keys of
        
    Returns:
        list: The keys of the dictionary
        
    Raises:
        TypeError: If the argument is not a dictionary
    """
    if not isinstance(dictionary, dict):
        raise TypeError(f"Argumen harus berupa kamus, bukan '{type(dictionary).__name__}'")
    
    return list(dictionary.keys())

def nilai(dictionary):
    """
    Get the values of a dictionary
    
    Args:
        dictionary (dict): The dictionary to get the values of
        
    Returns:
        list: The values of the dictionary
        
    Raises:
        TypeError: If the argument is not a dictionary
    """
    if not isinstance(dictionary, dict):
        raise TypeError(f"Argumen harus berupa kamus, bukan '{type(dictionary).__name__}'")
    
    return list(dictionary.values())

def item(dictionary):
    """
    Get the items of a dictionary
    
    Args:
        dictionary (dict): The dictionary to get the items of
        
    Returns:
        list: The items of the dictionary as (key, value) tuples
        
    Raises:
        TypeError: If the argument is not a dictionary
    """
    if not isinstance(dictionary, dict):
        raise TypeError(f"Argumen harus berupa kamus, bukan '{type(dictionary).__name__}'")
    
    return list(dictionary.items())

def hapus_kunci(dictionary, key):
    """
    Remove a key-value pair from a dictionary
    
    Args:
        dictionary (dict): The dictionary to remove from
        key: The key to remove
        
    Returns:
        dict: The dictionary with the key-value pair removed
        
    Raises:
        TypeError: If the first argument is not a dictionary
        KeyError: If the key is not in the dictionary
    """
    if not isinstance(dictionary, dict):
        raise TypeError(f"Argumen pertama harus berupa kamus, bukan '{type(dictionary).__name__}'")
    
    try:
        del dictionary[key]
        return dictionary
    except KeyError:
        raise KeyError(f"Kunci '{key}' tidak ditemukan dalam kamus")

# System functions
def acak(min_val=0, max_val=1):
    """
    Generate a random number
    
    Args:
        min_val (int or float, optional): The minimum value
        max_val (int or float, optional): The maximum value
        
    Returns:
        int or float: The random number
    """
    if isinstance(min_val, int) and isinstance(max_val, int):
        return random.randint(min_val, max_val)
    else:
        return random.uniform(min_val, max_val)

def waktu():
    """
    Get the current timestamp
    
    Returns:
        float: The current timestamp
    """
    return time.time()

def tidur(seconds):
    """
    Sleep for a number of seconds
    
    Args:
        seconds (int or float): The number of seconds to sleep
    """
    time.sleep(seconds)

def tanggal():
    """
    Get the current date and time
    
    Returns:
        datetime: The current date and time
    """
    return datetime.datetime.now()

def baca_file(filename):
    """
    Read the contents of a file
    
    Args:
        filename (str): The name of the file to read
        
    Returns:
        str: The contents of the file
        
    Raises:
        FileNotFoundError: If the file does not exist
        IOError: If there is an error reading the file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' tidak ditemukan")
    except IOError as e:
        raise IOError(f"Error membaca file '{filename}': {str(e)}")

def tulis_file(filename, content):
    """
    Write content to a file
    
    Args:
        filename (str): The name of the file to write to
        content (str): The content to write
        
    Raises:
        IOError: If there is an error writing to the file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    except IOError as e:
        raise IOError(f"Error menulis ke file '{filename}': {str(e)}")

def tambah_file(filename, content):
    """
    Append content to a file
    
    Args:
        filename (str): The name of the file to append to
        content (str): The content to append
        
    Raises:
        IOError: If there is an error appending to the file
    """
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(content)
    except IOError as e:
        raise IOError(f"Error menambahkan ke file '{filename}': {str(e)}")

def hapus_file(filename):
    """
    Delete a file
    
    Args:
        filename (str): The name of the file to delete
        
    Raises:
        FileNotFoundError: If the file does not exist
        IOError: If there is an error deleting the file
    """
    try:
        os.remove(filename)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' tidak ditemukan")
    except IOError as e:
        raise IOError(f"Error menghapus file '{filename}': {str(e)}")

# Security configuration for command execution
SANDBOX_MODE = True  # Enable sandbox mode by default for security

# Minimal safe command set - read-only operations only
ALLOWED_COMMANDS = {
    # Basic safe commands
    'echo', 'ls', 'pwd', 'cat', 'head', 'tail', 'wc', 'date', 'whoami', 'which',
    # Text processing (read-only)
    'sort', 'uniq', 'cut', 'grep',
}

# Safe compound commands with argument restrictions
COMPOUND_COMMANDS = {
    'git status': [],  # No dangerous flags
    'git log': ['--oneline', '--graph', '--decorate'],  # Safe read-only flags
    'git show': ['--stat', '--name-only'],  # Safe flags
    'git diff': ['--stat', '--name-only'],  # Safe flags
    'git branch': ['-r', '--list'],  # Safe flags
    'pip list': [],
    'pip show': [],
}

# Allowed executable directories (prevent PATH hijacking) 
ALLOWED_PATHS = {'/bin', '/usr/bin', '/usr/local/bin'}

# Maximum limits for security
MAX_OUTPUT_SIZE = 1024 * 1024  # 1MB max output
MAX_COMMAND_TIMEOUT = 10  # 10 seconds max

DANGEROUS_PATTERNS = [
    # Shell metacharacters that can be dangerous
    r'[;&|`$()]',
    # Redirection operators
    r'[<>]',
    # Command substitution
    r'\$\(',
    r'`',
    # Dangerous commands
    r'\b(rm|del|format|fdisk|mkfs|dd|sudo|su|chmod\s+777|chown\s+root)\b',
]

def validate_executable_path(cmd_path):
    """
    Validate if executable path is safe (prevent PATH hijacking)
    
    Args:
        cmd_path (str): Path to executable
        
    Returns:
        bool: True if path is safe
    """
    import shutil
    import os.path
    from pathlib import Path
    
    if not cmd_path:
        return False
        
    # Find actual executable path
    real_path = shutil.which(cmd_path)
    if not real_path:
        return False
        
    # Resolve to absolute path to handle symlinks
    try:
        resolved_path = Path(real_path).resolve()
        real_dir = str(resolved_path.parent)
        
        # Use proper path comparison instead of startswith
        for allowed_dir in ALLOWED_PATHS:
            try:
                # Check if real_dir is within or equal to allowed_dir
                Path(allowed_dir).resolve()
                common_path = os.path.commonpath([real_dir, allowed_dir])
                if common_path == allowed_dir:
                    return True
            except (ValueError, OSError):
                continue
                
        return False
    except (OSError, RuntimeError):
        # Handle path resolution errors
        return False

def validate_command_safety(command, use_sandbox=None):
    """
    Validate if a command is safe to execute with enhanced security checks
    
    Args:
        command (str): The command to validate
        use_sandbox (bool): Whether to use sandbox mode (overrides global)
        
    Returns:
        tuple: (is_safe, reason)
    """
    if not isinstance(command, str):
        return False, "Perintah harus berupa teks"
    
    command = command.strip()
    if not command:
        return False, "Perintah tidak boleh kosong"
    
    # Use provided sandbox setting or global default
    sandbox_enabled = SANDBOX_MODE if use_sandbox is None else use_sandbox
    
    # Tokenize command properly using shlex
    try:
        cmd_tokens = shlex.split(command)
    except ValueError as e:
        return False, f"Format perintah tidak valid: {str(e)}"
    
    if not cmd_tokens:
        return False, "Perintah kosong setelah parsing"
    
    base_command = cmd_tokens[0].lower()
    
    # Check for absolute paths (security risk)
    if os.path.isabs(cmd_tokens[0]):
        if sandbox_enabled:
            return False, "Path absolut tidak diizinkan dalam mode sandbox"
    
    # In sandbox mode, check whitelist and validate executable path
    if sandbox_enabled:
        # Check if base command is in simple whitelist
        if base_command in ALLOWED_COMMANDS:
            # Validate executable path to prevent PATH hijacking
            if not validate_executable_path(base_command):
                return False, f"Perintah '{base_command}' tidak ditemukan di direktori aman"
                
            # Check arguments for security risks
            for token in cmd_tokens[1:]:
                # Block shell metacharacters
                if re.search(r'[;&|`$<>()]', token):
                    return False, f"Argumen '{token}' mengandung karakter berbahaya"
                # Block absolute paths in arguments (prevent reading sensitive files)
                if os.path.isabs(token):
                    return False, f"Path absolut '{token}' tidak diizinkan dalam argumen"
            
            return True, "Perintah aman"
        
        # Check compound commands and validate their base executable too
        for compound_cmd, allowed_flags in COMPOUND_COMMANDS.items():
            if command.lower().startswith(compound_cmd.lower()):
                # Validate the base executable of compound command
                compound_base = compound_cmd.split()[0]
                if not validate_executable_path(compound_base):
                    return False, f"Perintah compound '{compound_base}' tidak ditemukan di direktori aman"
                
                # Validate compound command arguments
                remaining_args = cmd_tokens[len(compound_cmd.split()):]
                for arg in remaining_args:
                    if allowed_flags and arg not in allowed_flags:
                        return False, f"Argumen '{arg}' tidak diizinkan untuk perintah '{compound_cmd}'"
                    if re.search(r'[;&|`$<>()]', arg):
                        return False, f"Argumen '{arg}' mengandung karakter berbahaya"
                    # Block absolute paths
                    if os.path.isabs(arg) and not arg.startswith(('-', '--')):
                        return False, f"Path absolut '{arg}' tidak diizinkan dalam argumen"
                        
                return True, "Perintah compound aman"
        
        return False, f"Perintah '{base_command}' tidak diizinkan dalam mode sandbox. Perintah yang diizinkan: {sorted(list(ALLOWED_COMMANDS))}"
    
    return True, "Sandbox dinonaktifkan - perintah diizinkan"

def jalankan_perintah(command, sandbox=None, working_dir=None, timeout=None):
    """
    Run a shell command safely with enhanced sandbox protection and resource limits
    
    Args:
        command (str): The command to run
        sandbox (bool, optional): Override global sandbox mode
        working_dir (str, optional): Working directory for command execution
        timeout (int, optional): Custom timeout in seconds
        
    Returns:
        tuple: (return_code, stdout, stderr)
        
    Raises:
        SecurityError: If the command is not safe to run
        subprocess.SubprocessError: If there is an error running the command
    """
    # Use global sandbox setting if not overridden
    use_sandbox = SANDBOX_MODE if sandbox is None else sandbox
    
    # Use default timeout if not specified
    command_timeout = timeout if timeout is not None else MAX_COMMAND_TIMEOUT
    
    # Validate command safety with the effective sandbox setting
    if use_sandbox:
        is_safe, reason = validate_command_safety(command, use_sandbox)
        if not is_safe:
            raise SecurityError(f"Keamanan: {reason}")
    
    # Validate working directory if provided
    if working_dir is not None:
        if not os.path.isdir(working_dir):
            raise SecurityError(f"Direktori kerja '{working_dir}' tidak valid")
        
        # Prevent directory traversal attacks
        try:
            real_path = os.path.realpath(working_dir)
            if not real_path.startswith(os.getcwd()):
                raise SecurityError(f"Direktori kerja '{working_dir}' berada di luar direktori yang diizinkan")
        except (OSError, RuntimeError):
            raise SecurityError(f"Tidak dapat memvalidasi direktori kerja '{working_dir}'")
    else:
        working_dir = os.getcwd()
    
    cmd_args = []  # Initialize to avoid unbound variable
    process = None  # Initialize to avoid unbound variable
    
    try:
        # Tokenize command using shlex for security
        cmd_args = shlex.split(command)
        if not cmd_args:
            raise SecurityError("Perintah kosong")
        
        # Additional security: Check for suspicious command patterns
        command_str = " ".join(cmd_args).lower()
        suspicious_patterns = [
            r'(^|\s)(wget|curl)(\s|$)',  # Network download tools
            r'(^|\s)(nc|netcat|ncat)(\s|$)',  # Network tools
            r'(^|\s)(telnet|ssh|ftp)(\s|$)',  # Remote access
            r'(^|\s)(chmod\s+[0-7]*7[0-7]*|chmod\s+.*\+x)(\s|$)',  # Suspicious chmod
            r'(^|\s)(eval|exec)(\s|$)',  # Code execution
            r'(^|\s)(base64\s+-d)(\s|$)',  # Base64 decode (often used in obfuscation)
            r'(^|\s)(mkfifo|mknod)(\s|$)',  # Special file creation
        ]
        
        for pattern in suspicious_patterns:
            if re.search(pattern, command_str):
                raise SecurityError(f"Perintah mencurigakan terdeteksi: '{command}'")
        
        # Additional security: limit environment variables
        safe_env = {
            'PATH': '/usr/local/bin:/usr/bin:/bin',  # Restrict PATH to standard directories
            'HOME': os.environ.get('HOME', ''),
            'USER': os.environ.get('USER', ''),
            'PWD': working_dir,
            'LANG': os.environ.get('LANG', 'en_US.UTF-8'),
            'LC_ALL': os.environ.get('LC_ALL', 'en_US.UTF-8'),
            'TMPDIR': '/tmp',
            'TZ': 'UTC',  # Use consistent timezone
        }
        
        # Remove potentially dangerous environment variables
        for dangerous_var in ['LD_PRELOAD', 'LD_LIBRARY_PATH', 'PYTHONPATH', 'PERL5LIB']:
            if dangerous_var in safe_env:
                del safe_env[dangerous_var]
        
        # Set resource limits
        def set_limits():
            """Set resource limits for the subprocess"""
            import resource
            # Limit CPU time (seconds)
            resource.setrlimit(resource.RLIMIT_CPU, (command_timeout, command_timeout + 1))
            # Limit file size creation (bytes)
            resource.setrlimit(resource.RLIMIT_FSIZE, (10 * 1024 * 1024, 10 * 1024 * 1024))  # 10MB
            # Limit number of processes
            try:
                resource.setrlimit(resource.RLIMIT_NPROC, (10, 10))  # Limit to 10 processes
            except (ValueError, AttributeError):
                pass  # Not all systems support this
            # Limit memory usage (bytes)
            try:
                resource.setrlimit(resource.RLIMIT_AS, (500 * 1024 * 1024, 500 * 1024 * 1024))  # 500MB
            except (ValueError, AttributeError):
                pass  # Not all systems support this
        
        # Execute with enhanced security
        process = subprocess.Popen(
            cmd_args,
            shell=False,  # SECURITY: Never use shell=True
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.DEVNULL,  # No stdin access
            universal_newlines=True,
            cwd=working_dir,  # Use validated working directory
            env=safe_env,  # Restricted environment
            close_fds=True,  # Close unused file descriptors
            start_new_session=True,  # Create new process group for better cleanup
            preexec_fn=set_limits if os.name != 'nt' else None,  # Set resource limits on Unix
        )
        
        # Communicate with timeout and size limits
        try:
            stdout, stderr = process.communicate(timeout=command_timeout)
            
            # Check output size limits
            if len(stdout) > MAX_OUTPUT_SIZE:
                stdout = stdout[:MAX_OUTPUT_SIZE] + "\n[OUTPUT TRUNCATED - EXCEEDED SIZE LIMIT]"
            if len(stderr) > MAX_OUTPUT_SIZE:
                stderr = stderr[:MAX_OUTPUT_SIZE] + "\n[ERROR TRUNCATED - EXCEEDED SIZE LIMIT]"
            
            # Scan output for sensitive information patterns
            sensitive_patterns = [
                r'password\s*=\s*[\'"][^\'"]+[\'"]',
                r'api[_-]?key\s*=\s*[\'"][^\'"]+[\'"]',
                r'secret\s*=\s*[\'"][^\'"]+[\'"]',
                r'token\s*=\s*[\'"][^\'"]+[\'"]',
            ]
            
            for pattern in sensitive_patterns:
                stdout = re.sub(pattern, r'\1=*****', stdout, flags=re.IGNORECASE)
                stderr = re.sub(pattern, r'\1=*****', stderr, flags=re.IGNORECASE)
                
            return (process.returncode, stdout, stderr)
            
        except subprocess.TimeoutExpired:
            # Terminate entire process group for better cleanup
            try:
                import signal
                os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                process.wait(timeout=2)
            except (ProcessLookupError, PermissionError, subprocess.TimeoutExpired):
                # Fallback to individual process termination
                process.kill()
                try:
                    process.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    pass  # Process is really stuck
            
            # Also try to kill any child processes
            try:
                import psutil
                parent = psutil.Process(process.pid)
                for child in parent.children(recursive=True):
                    child.kill()
            except (ImportError, psutil.NoSuchProcess, psutil.AccessDenied):
                pass  # psutil not available or process already gone
                
            raise SecurityError(f"Perintah '{command}' melebihi batas waktu ({command_timeout} detik)")
            
    except SecurityError:
        # Re-raise security errors as-is
        raise
    except FileNotFoundError:
        cmd_name = cmd_args[0] if cmd_args else "unknown"
        raise SecurityError(f"Perintah '{cmd_name}' tidak ditemukan atau tidak diizinkan")
    except PermissionError:
        cmd_name = cmd_args[0] if cmd_args else "unknown"
        raise SecurityError(f"Tidak ada izin untuk menjalankan perintah '{cmd_name}'")
    except subprocess.SubprocessError as e:
        raise SecurityError(f"Error menjalankan perintah '{command}': {str(e)}")
    except Exception as e:
        raise SecurityError(f"Error tidak terduga saat menjalankan perintah '{command}': {str(e)}")

def atur_sandbox(enabled):
    """
    Enable or disable sandbox mode globally
    
    Args:
        enabled (bool): Whether to enable sandbox mode
    """
    global SANDBOX_MODE
    SANDBOX_MODE = enabled
    return f"Mode sandbox {'diaktifkan' if enabled else 'dinonaktifkan'}"

def tambah_perintah_aman(command):
    """
    Add a command to the safe commands whitelist
    
    Args:
        command (str): Command to add to whitelist
    """
    if isinstance(command, str) and command.strip():
        ALLOWED_COMMANDS.add(command.strip().lower())
        return f"Perintah '{command}' ditambahkan ke daftar aman"
    else:
        raise ValueError("Perintah harus berupa teks yang tidak kosong")

def hapus_perintah_aman(command):
    """
    Remove a command from the safe commands whitelist
    
    Args:
        command (str): Command to remove from whitelist
    """
    if isinstance(command, str) and command.strip():
        cmd = command.strip().lower()
        if cmd in ALLOWED_COMMANDS:
            ALLOWED_COMMANDS.remove(cmd)
            return f"Perintah '{command}' dihapus dari daftar aman"
        else:
            return f"Perintah '{command}' tidak ada dalam daftar aman"
    else:
        raise ValueError("Perintah harus berupa teks yang tidak kosong")

# Enhanced built-in functions

def format_teks(template, **kwargs):
    """
    Format a string with variables
    
    Args:
        template (str): The string template
        **kwargs: Variables to format the string with
        
    Returns:
        str: The formatted string
    """
    return template.format(**kwargs)

def gabung_path(*paths):
    """
    Join path components
    
    Args:
        *paths: Path components
        
    Returns:
        str: The joined path
    """
    return os.path.join(*paths)

def file_exists(path):
    """
    Check if a file exists
    
    Args:
        path (str): The path to check
        
    Returns:
        bool: True if the file exists, False otherwise
    """
    return os.path.exists(path)

def buat_direktori(path):
    """
    Create a directory
    
    Args:
        path (str): The path to create
    """
    os.makedirs(path, exist_ok=True)

def daftar_direktori(path='.'):
    """
    List files in a directory
    
    Args:
        path (str, optional): The path to list
        
    Returns:
        list: The files in the directory
    """
    return os.listdir(path)

def json_ke_teks(obj):
    """
    Convert an object to JSON text
    
    Args:
        obj: The object to convert
        
    Returns:
        str: The JSON text
    """
    return json.dumps(obj, ensure_ascii=False)

def teks_ke_json(text):
    """
    Convert JSON text to an object
    
    Args:
        text (str): The JSON text
        
    Returns:
        Any: The object
    """
    return json.loads(text)

def hash_teks(text, algorithm='sha256'):
    """
    Hash text
    
    Args:
        text (str): The text to hash
        algorithm (str, optional): The hash algorithm to use
        
    Returns:
        str: The hash
    """
    if algorithm == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(text.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(text.encode()).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(text.encode()).hexdigest()
    else:
        raise ValueError(f"Algoritma hash '{algorithm}' tidak didukung")

def buat_uuid():
    """
    Create a UUID
    
    Returns:
        str: The UUID
    """
    return str(uuid.uuid4())

def url_encode(text):
    """
    URL encode text
    
    Args:
        text (str): The text to encode
        
    Returns:
        str: The encoded text
    """
    return urllib.parse.quote(text)

def url_decode(text):
    """
    URL decode text
    
    Args:
        text (str): The text to decode
        
    Returns:
        str: The decoded text
    """
    return urllib.parse.unquote(text)

def http_get(url, headers=None):
    """
    Make an HTTP GET request
    
    Args:
        url (str): The URL to request
        headers (dict, optional): The headers to send
        
    Returns:
        dict: The response
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
    """
    data_bytes = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=data_bytes, headers=headers or {}, method='POST')
    with urllib.request.urlopen(req) as response:
        return {
            'status': response.status,
            'headers': dict(response.headers),
            'content': response.read().decode('utf-8')
        }

def regex_match(pattern, text):
    """
    Match a regex pattern against text
    
    Args:
        pattern (str): The regex pattern
        text (str): The text to match against
        
    Returns:
        list: The matches
    """
    return re.findall(pattern, text)

def regex_replace(pattern, replacement, text):
    """
    Replace text matching a regex pattern
    
    Args:
        pattern (str): The regex pattern
        replacement (str): The replacement text
        text (str): The text to replace in
        
    Returns:
        str: The text with replacements
    """
    return re.sub(pattern, replacement, text)

def base64_encode(text):
    """
    Base64 encode text
    
    Args:
        text (str): The text to encode
        
    Returns:
        str: The encoded text
    """
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    """
    Base64 decode text
    
    Args:
        text (str): The text to decode
        
    Returns:
        str: The decoded text
    """
    return base64.b64decode(text.encode()).decode()

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
    async def gather_coros():
        return await asyncio.gather(*coros)
    
    return asyncio.run(gather_coros())

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

def get_function_module(func):
    """
    Get the module of a function
    
    Args:
        func: The function to get the module of
        
    Returns:
        str: The module name
    """
    return func.__module__

def get_function_name(func):
    """
    Get the name of a function
    
    Args:
        func: The function to get the name of
        
    Returns:
        str: The name
    """
    return func.__name__

def get_function_qualname(func):
    """
    Get the qualified name of a function
    
    Args:
        func: The function to get the qualified name of
        
    Returns:
        str: The qualified name
    """
    return func.__qualname__

def get_function_globals(func):
    """
    Get the globals of a function
    
    Args:
        func: The function to get the globals of
        
    Returns:
        dict: The globals
    """
    return func.__globals__

def get_function_closure(func):
    """
    Get the closure of a function
    
    Args:
        func: The function to get the closure of
        
    Returns:
        tuple: The closure
    """
    return func.__closure__

def get_function_code(func):
    """
    Get the code object of a function
    
    Args:
        func: The function to get the code object of
        
    Returns:
        code: The code object
    """
    return func.__code__

# Super function for class inheritance
def super_impl(*args, **kwargs):
    """Implementation of super() function for class inheritance"""
    class SuperProxy:
        def __call__(self, *args, **kwargs):
            # Constructor call - will be handled by interpreter
            return None
            
        def __getattr__(self, name):
            # Method call - will be handled by interpreter  
            def method_proxy(*method_args, **method_kwargs):
                return f"super().{name}() called"
            return method_proxy
    
    return SuperProxy()

# Create the builtin function wrapper
class RenzmcBuiltinFunction:
    """Wrapper for RenzmcLang builtin functions"""
    def __init__(self, func, name):
        self.func = func
        self.name = name
        self.__name__ = name
    
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
    
    def __repr__(self):
        return f"<builtin function '{self.name}'>"

super = RenzmcBuiltinFunction(super_impl, 'super')


# Enhanced Python Integration Functions
def impor_semua_python(module_name):
    """
    Import all public attributes from a Python module (from module import *)
    
    Args:
        module_name (str): The name of the module to import from
        
    Returns:
        dict: Dictionary of all public attributes from the module
    """
    # This will be connected to the interpreter's python_integration
    # The actual implementation is in python_integration.py
    pass

def reload_python(module_name):
    """
    Reload a Python module (useful for development)
    
    Args:
        module_name (str): The name of the module to reload
        
    Returns:
        module: The reloaded module
    """
    pass

def cek_modul_python(module_name):
    """
    Check if a Python module is available for import
    
    Args:
        module_name (str): The name of the module to check
        
    Returns:
        bool: True if the module is available
    """
    pass

def daftar_modul_python():
    """
    List all available Python modules in the system
    
    Returns:
        list: List of available module names
    """
    pass

def versi_modul_python(module_name):
    """
    Get the version of an imported Python module
    
    Args:
        module_name (str): The name of the module
        
    Returns:
        str: The version string
    """
    pass

def path_modul_python(module_name):
    """
    Get the file path of an imported Python module
    
    Args:
        module_name (str): The name of the module
        
    Returns:
        str: The file path of the module
    """
    pass

def jalankan_python(code_string):
    """
    Execute arbitrary Python code string
    
    Args:
        code_string (str): The Python code to execute
        
    Returns:
        dict: The local variables after execution
    """
    pass

def evaluasi_python(expression):
    """
    Evaluate a Python expression and return the result
    
    Args:
        expression (str): The Python expression to evaluate
        
    Returns:
        Any: The result of the expression
    """
    pass


# ===== Phase 2: Iteration Enhancement Functions =====

# Save Python's built-in functions before overriding
_builtin_zip = zip
_builtin_enumerate = enumerate
_builtin_filter = filter
_builtin_map = map
_builtin_all = all
_builtin_any = any
_builtin_sorted = sorted

def zip_impl(*iterables):
    """
    Zip multiple iterables together
    
    Args:
        *iterables: Variable number of iterables to zip
        
    Returns:
        list: List of tuples containing elements from each iterable
        
    Example:
        zip([1, 2, 3], ['a', 'b', 'c']) -> [(1, 'a'), (2, 'b'), (3, 'c')]
    """
    return list(_builtin_zip(*iterables))

zip = RenzmcBuiltinFunction(zip_impl, 'zip')


def enumerate_impl(iterable, start=0):
    """
    Enumerate an iterable with index
    
    Args:
        iterable: The iterable to enumerate
        start (int): Starting index (default: 0)
        
    Returns:
        list: List of tuples (index, element)
        
    Example:
        enumerate(['a', 'b', 'c']) -> [(0, 'a'), (1, 'b'), (2, 'c')]
        enumerate(['a', 'b', 'c'], mulai=1) -> [(1, 'a'), (2, 'b'), (3, 'c')]
    """
    return list(_builtin_enumerate(iterable, start))

enumerate = RenzmcBuiltinFunction(enumerate_impl, 'enumerate')


def filter_impl(function, iterable):
    """
    Filter elements from iterable based on function
    
    Args:
        function: Function that returns True/False for each element
        iterable: The iterable to filter
        
    Returns:
        list: List of elements where function returned True
        
    Example:
        filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) -> [2, 4]
    """
    return list(_builtin_filter(function, iterable))

filter = RenzmcBuiltinFunction(filter_impl, 'filter')
saring = filter  # Indonesian alias


def map_impl(function, *iterables):
    """
    Apply function to every item of iterable
    
    Args:
        function: Function to apply to each element
        *iterables: One or more iterables
        
    Returns:
        list: List of results after applying function
        
    Example:
        map(lambda x: x * 2, [1, 2, 3]) -> [2, 4, 6]
        map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]) -> [5, 7, 9]
    """
    return list(_builtin_map(function, *iterables))

map = RenzmcBuiltinFunction(map_impl, 'map')
peta = map  # Indonesian alias


def reduce_impl(function, iterable, initial=None):
    """
    Reduce iterable to single value using function
    
    Args:
        function: Function that takes two arguments
        iterable: The iterable to reduce
        initial: Initial value (optional)
        
    Returns:
        Any: The reduced value
        
    Example:
        reduce(lambda x, y: x + y, [1, 2, 3, 4]) -> 10
        reduce(lambda x, y: x * y, [1, 2, 3, 4], 10) -> 240
    """
    from functools import reduce as _builtin_reduce
    if initial is None:
        return _builtin_reduce(function, iterable)
    else:
        return _builtin_reduce(function, iterable, initial)

reduce = RenzmcBuiltinFunction(reduce_impl, 'reduce')
kurangi = reduce  # Indonesian alias


def all_impl(iterable):
    """
    Check if all elements in iterable are True
    
    Args:
        iterable: The iterable to check
        
    Returns:
        bool: True if all elements are True, False otherwise
        
    Example:
        all([True, True, True]) -> True
        all([True, False, True]) -> False
    """
    return _builtin_all(iterable)

all = RenzmcBuiltinFunction(all_impl, 'all')
semua = all  # Indonesian alias


def any_impl(iterable):
    """
    Check if any element in iterable is True
    
    Args:
        iterable: The iterable to check
        
    Returns:
        bool: True if any element is True, False otherwise
        
    Example:
        any([False, False, True]) -> True
        any([False, False, False]) -> False
    """
    return _builtin_any(iterable)

any = RenzmcBuiltinFunction(any_impl, 'any')
ada = any  # Indonesian alias


def sorted_impl(iterable, key=None, reverse=False):
    """
    Return sorted list from iterable (non-mutating)
    
    Args:
        iterable: The iterable to sort
        key: Function to extract comparison key (optional)
        reverse (bool): Sort in descending order if True
        
    Returns:
        list: New sorted list
        
    Example:
        sorted([3, 1, 4, 1, 5]) -> [1, 1, 3, 4, 5]
        sorted([3, 1, 4, 1, 5], terbalik=True) -> [5, 4, 3, 1, 1]
        sorted(['apel', 'jeruk', 'mangga'], kunci=lambda x: len(x)) -> ['apel', 'jeruk', 'mangga']
    """
    if key is None:
        return _builtin_sorted(iterable, reverse=reverse)
    else:
        return _builtin_sorted(iterable, key=key, reverse=reverse)

sorted = RenzmcBuiltinFunction(sorted_impl, 'sorted')
terurut = sorted  # Indonesian alias



# ============================================================================
# PHASE 3: STRING VALIDATION FUNCTIONS
# ============================================================================

def is_alpha_impl(text):
    """
    Check if string contains only alphabetic characters
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if all characters are alphabetic, False otherwise
        
    Example:
        is_alpha("Hello") -> True
        is_alpha("Hello123") -> False
        is_alpha("") -> False
    """
    if not isinstance(text, str):
        return False
    if len(text) == 0:
        return False
    return text.isalpha()

is_alpha = RenzmcBuiltinFunction(is_alpha_impl, 'is_alpha')
adalah_huruf = is_alpha  # Indonesian alias


def is_digit_impl(text):
    """
    Check if string contains only digit characters
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if all characters are digits, False otherwise
        
    Example:
        is_digit("12345") -> True
        is_digit("123.45") -> False
        is_digit("") -> False
    """
    if not isinstance(text, str):
        return False
    if len(text) == 0:
        return False
    return text.isdigit()

is_digit = RenzmcBuiltinFunction(is_digit_impl, 'is_digit')
adalah_angka = is_digit  # Indonesian alias


def is_alnum_impl(text):
    """
    Check if string contains only alphanumeric characters
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if all characters are alphanumeric, False otherwise
        
    Example:
        is_alnum("Hello123") -> True
        is_alnum("Hello 123") -> False
        is_alnum("") -> False
    """
    if not isinstance(text, str):
        return False
    if len(text) == 0:
        return False
    return text.isalnum()

is_alnum = RenzmcBuiltinFunction(is_alnum_impl, 'is_alnum')
adalah_alfanumerik = is_alnum  # Indonesian alias


def is_lower_impl(text):
    """
    Check if all cased characters in string are lowercase
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if all cased characters are lowercase, False otherwise
        
    Example:
        is_lower("hello") -> True
        is_lower("Hello") -> False
        is_lower("hello123") -> True
        is_lower("") -> False
    """
    if not isinstance(text, str):
        return False
    if len(text) == 0:
        return False
    return text.islower()

is_lower = RenzmcBuiltinFunction(is_lower_impl, 'is_lower')
adalah_huruf_kecil = is_lower  # Indonesian alias


def is_upper_impl(text):
    """
    Check if all cased characters in string are uppercase
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if all cased characters are uppercase, False otherwise
        
    Example:
        is_upper("HELLO") -> True
        is_upper("Hello") -> False
        is_upper("HELLO123") -> True
        is_upper("") -> False
    """
    if not isinstance(text, str):
        return False
    if len(text) == 0:
        return False
    return text.isupper()

is_upper = RenzmcBuiltinFunction(is_upper_impl, 'is_upper')
adalah_huruf_besar = is_upper  # Indonesian alias


def is_space_impl(text):
    """
    Check if string contains only whitespace characters
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if all characters are whitespace, False otherwise
        
    Example:
        is_space("   ") -> True
        is_space(" a ") -> False
        is_space("") -> False
    """
    if not isinstance(text, str):
        return False
    if len(text) == 0:
        return False
    return text.isspace()

is_space = RenzmcBuiltinFunction(is_space_impl, 'is_space')
adalah_spasi = is_space  # Indonesian alias


# ============================================================================
# PHASE 4: FILE & PATH OPERATIONS
# ============================================================================

import os
import shutil
from pathlib import Path

# 4.1 Directory Operations

def direktori_ada_impl(path):
    """
    Check if directory exists
    
    Args:
        path (str): Directory path to check
        
    Returns:
        bool: True if directory exists, False otherwise
        
    Example:
        direktori_ada("my_folder") -> True/False
    """
    return os.path.isdir(path)

direktori_ada = RenzmcBuiltinFunction(direktori_ada_impl, 'direktori_ada')


def direktori_sekarang_impl():
    """
    Get current working directory
    
    Returns:
        str: Current working directory path
        
    Example:
        direktori_sekarang() -> "/home/user/project"
    """
    return os.getcwd()

direktori_sekarang = RenzmcBuiltinFunction(direktori_sekarang_impl, 'direktori_sekarang')


def ubah_direktori_impl(path):
    """
    Change current working directory
    
    Args:
        path (str): Directory path to change to
        
    Example:
        ubah_direktori("my_folder")
    """
    os.chdir(path)
    return None

ubah_direktori = RenzmcBuiltinFunction(ubah_direktori_impl, 'ubah_direktori')


# 4.2 Path Operations

def pisah_path_impl(path):
    """
    Split path into directory and filename
    
    Args:
        path (str): Path to split
        
    Returns:
        tuple: (directory, filename)
        
    Example:
        pisah_path("folder/file.txt") -> ("folder", "file.txt")
    """
    return os.path.split(path)

pisah_path = RenzmcBuiltinFunction(pisah_path_impl, 'pisah_path')


def ekstensi_file_impl(path):
    """
    Get file extension
    
    Args:
        path (str): File path
        
    Returns:
        str: File extension including dot
        
    Example:
        ekstensi_file("document.pdf") -> ".pdf"
    """
    return os.path.splitext(path)[1]

ekstensi_file = RenzmcBuiltinFunction(ekstensi_file_impl, 'ekstensi_file')


def nama_file_tanpa_ekstensi_impl(path):
    """
    Get filename without extension
    
    Args:
        path (str): File path
        
    Returns:
        str: Filename without extension
        
    Example:
        nama_file_tanpa_ekstensi("document.pdf") -> "document"
    """
    return os.path.splitext(os.path.basename(path))[0]

nama_file_tanpa_ekstensi = RenzmcBuiltinFunction(nama_file_tanpa_ekstensi_impl, 'nama_file_tanpa_ekstensi')


def path_ada_impl(path):
    """
    Check if path exists (file or directory)
    
    Args:
        path (str): Path to check
        
    Returns:
        bool: True if path exists, False otherwise
        
    Example:
        path_ada("file.txt") -> True/False
    """
    return os.path.exists(path)

path_ada = RenzmcBuiltinFunction(path_ada_impl, 'path_ada')


def adalah_file_impl(path):
    """
    Check if path is a file
    
    Args:
        path (str): Path to check
        
    Returns:
        bool: True if path is a file, False otherwise
        
    Example:
        adalah_file("file.txt") -> True/False
    """
    return os.path.isfile(path)

adalah_file = RenzmcBuiltinFunction(adalah_file_impl, 'adalah_file')


def adalah_direktori_impl(path):
    """
    Check if path is a directory
    
    Args:
        path (str): Path to check
        
    Returns:
        bool: True if path is a directory, False otherwise
        
    Example:
        adalah_direktori("folder") -> True/False
    """
    return os.path.isdir(path)

adalah_direktori = RenzmcBuiltinFunction(adalah_direktori_impl, 'adalah_direktori')


def path_absolut_impl(path):
    """
    Get absolute path
    
    Args:
        path (str): Relative or absolute path
        
    Returns:
        str: Absolute path
        
    Example:
        path_absolut("file.txt") -> "/home/user/project/file.txt"
    """
    return os.path.abspath(path)

path_absolut = RenzmcBuiltinFunction(path_absolut_impl, 'path_absolut')


# 4.3 File Metadata

def waktu_modifikasi_file_impl(path):
    """
    Get file modification time
    
    Args:
        path (str): File path
        
    Returns:
        float: Modification time as timestamp
        
    Example:
        waktu_modifikasi_file("file.txt") -> 1234567890.123
    """
    return os.path.getmtime(path)

waktu_modifikasi_file = RenzmcBuiltinFunction(waktu_modifikasi_file_impl, 'waktu_modifikasi_file')


def waktu_buat_file_impl(path):
    """
    Get file creation time
    
    Args:
        path (str): File path
        
    Returns:
        float: Creation time as timestamp
        
    Example:
        waktu_buat_file("file.txt") -> 1234567890.123
    """
    return os.path.getctime(path)

waktu_buat_file = RenzmcBuiltinFunction(waktu_buat_file_impl, 'waktu_buat_file')


def file_dapat_dibaca_impl(path):
    """
    Check if file is readable
    
    Args:
        path (str): File path
        
    Returns:
        bool: True if file is readable, False otherwise
        
    Example:
        file_dapat_dibaca("file.txt") -> True/False
    """
    return os.access(path, os.R_OK)

file_dapat_dibaca = RenzmcBuiltinFunction(file_dapat_dibaca_impl, 'file_dapat_dibaca')


def file_dapat_ditulis_impl(path):
    """
    Check if file is writable
    
    Args:
        path (str): File path
        
    Returns:
        bool: True if file is writable, False otherwise
        
    Example:
        file_dapat_ditulis("file.txt") -> True/False
    """
    return os.access(path, os.W_OK)

file_dapat_ditulis = RenzmcBuiltinFunction(file_dapat_ditulis_impl, 'file_dapat_ditulis')


# ============================================================================
# PHASE 6: MATH & STATISTICS FUNCTIONS
# ============================================================================

import statistics

def median_impl(data):
    """
    Calculate median of data
    
    Args:
        data: Iterable of numbers
        
    Returns:
        float: Median value
        
    Example:
        median([1, 2, 3, 4, 5]) -> 3
        median([1, 2, 3, 4]) -> 2.5
    """
    return statistics.median(data)

median = RenzmcBuiltinFunction(median_impl, 'median')
nilai_tengah = median  # Indonesian alias


def mode_impl(data):
    """
    Calculate mode of data (most common value)
    
    Args:
        data: Iterable of values
        
    Returns:
        Any: Most common value
        
    Example:
        mode([1, 2, 2, 3, 3, 3, 4]) -> 3
    """
    return statistics.mode(data)

mode = RenzmcBuiltinFunction(mode_impl, 'mode')
nilai_modus = mode  # Indonesian alias


def stdev_impl(data):
    """
    Calculate standard deviation of data
    
    Args:
        data: Iterable of numbers
        
    Returns:
        float: Standard deviation
        
    Example:
        stdev([2, 4, 4, 4, 5, 5, 7, 9]) -> 2.0
    """
    return statistics.stdev(data)

stdev = RenzmcBuiltinFunction(stdev_impl, 'stdev')
deviasi_standar = stdev  # Indonesian alias


def variance_impl(data):
    """
    Calculate variance of data
    
    Args:
        data: Iterable of numbers
        
    Returns:
        float: Variance
        
    Example:
        variance([2, 4, 4, 4, 5, 5, 7, 9]) -> 4.0
    """
    return statistics.variance(data)

variance = RenzmcBuiltinFunction(variance_impl, 'variance')
variansi = variance  # Indonesian alias


def quantiles_impl(data, n=4):
    """
    Calculate quantiles of data
    
    Args:
        data: Iterable of numbers
        n (int): Number of quantiles (default 4 for quartiles)
        
    Returns:
        list: List of quantile values
        
    Example:
        quantiles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) -> [2.75, 5.5, 8.25]
    """
    return statistics.quantiles(data, n=n)

quantiles = RenzmcBuiltinFunction(quantiles_impl, 'quantiles')
kuantil = quantiles  # Indonesian alias
