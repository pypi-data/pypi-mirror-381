#!/usr/bin/env python3

"""
Main entry point for RenzmcLang

This module provides the main entry point for the RenzmcLang interpreter.
It handles command-line arguments and runs the interpreter.
"""

import os
import sys
import argparse
import readline
import atexit
from pathlib import Path

from renzmc.core.lexer import Lexer
from renzmc.core.parser import Parser  # Import the Parser
from renzmc.core.interpreter import Interpreter
from renzmc.core.error import format_error
from renzmc.version import __version__

# Set up history file for interactive mode
HISTORY_FILE = os.path.join(os.path.expanduser("~"), ".renzmc_history")

def run_file(filename):
    """
    Run a RenzmcLang file
    
    Args:
        filename (str): The name of the file to run
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        run_code(source_code, filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def run_code(source_code, filename="<stdin>"):
    """
    Run RenzmcLang code
    
    Args:
        source_code (str): The source code to run
        filename (str, optional): The name of the file (for error reporting)
    """
    try:
        lexer = Lexer(source_code)
        interpreter = Interpreter()
        
        # Create parser and parse the code
        parser = Parser(lexer)
        ast = parser.parse()
        
        # Interpret the AST
        result = interpreter.visit(ast)
        
    except Exception as e:
        print(format_error(e, source_code))
        if not filename == "<stdin>":
            sys.exit(1)

def run_interactive():
    """
    Run the RenzmcLang interpreter in interactive mode
    """
    # Set up readline with history
    try:
        readline.parse_and_bind("tab: complete")
        
        # Create history file if it doesn't exist
        if not os.path.exists(HISTORY_FILE):
            open(HISTORY_FILE, 'a').close()
        
        readline.read_history_file(HISTORY_FILE)
        atexit.register(readline.write_history_file, HISTORY_FILE)
    except (ImportError, IOError):
        pass
    
    print(f"RenzmcLang {__version__} - Bahasa pemrograman berbasis Bahasa Indonesia")
    print("Ketik 'keluar' untuk keluar dari interpreter.")
    print()
    
    interpreter = Interpreter()
    
    while True:
        try:
            line = input(">>> ")
            if line.strip().lower() == "keluar":
                break
            
            run_code(line)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print("\nKeyboardInterrupt")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

def main():
    """
    Main entry point for the RenzmcLang interpreter
    """
    parser = argparse.ArgumentParser(description="RenzmcLang - Bahasa pemrograman berbasis Bahasa Indonesia")
    parser.add_argument("file", nargs="?", help="File RenzmcLang untuk dijalankan")
    parser.add_argument("-v", "--version", action="store_true", help="Tampilkan versi RenzmcLang")
    parser.add_argument("-c", "--code", help="Jalankan kode RenzmcLang")
    
    args = parser.parse_args()
    
    if args.version:
        print(f"RenzmcLang {__version__}")
        return
    
    if args.code:
        run_code(args.code)
    elif args.file:
        run_file(args.file)
    else:
        run_interactive()

if __name__ == "__main__":
    main()