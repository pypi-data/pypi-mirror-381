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

def run_code(source_code, filename="<stdin>", interpreter=None):
    """
    Run RenzmcLang code
    
    Args:
        source_code (str): The source code to run
        filename (str, optional): The name of the file (for error reporting)
        interpreter (Interpreter, optional): Existing interpreter instance to reuse
    """
    try:
        lexer = Lexer(source_code)
        if interpreter is None:
            interpreter = Interpreter()
        
        # Create parser and parse the code
        parser = Parser(lexer)
        ast = parser.parse()
        
        # Interpret the AST
        result = interpreter.visit(ast)
        
        return interpreter
        
    except Exception as e:
        print(format_error(e, source_code))
        if not filename == "<stdin>":
            sys.exit(1)
        return interpreter

def run_interactive():
    """
    Run the RenzmcLang interpreter in interactive mode with multi-line support
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
    print("Untuk kode multi-baris, akhiri dengan baris kosong.")
    print()
    
    interpreter = Interpreter()
    
    # Keywords that indicate a block is starting
    block_keywords = [
        'jika', 'kalau', 'selama', 'untuk', 'ulangi', 'fungsi', 'kelas',
        'coba', 'tangkap', 'akhirnya', 'dengan', 'async', 'def'
    ]
    
    while True:
        try:
            # Read first line
            line = input(">>> ")
            if line.strip().lower() == "keluar":
                break
            
            # Check if this is a multi-line statement
            needs_continuation = False
            
            # Check for block keywords
            first_word = line.strip().split()[0] if line.strip() else ""
            if first_word in block_keywords:
                needs_continuation = True
            
            # Check for unclosed brackets, parentheses, or quotes
            open_parens = line.count('(') - line.count(')')
            open_brackets = line.count('[') - line.count(']')
            open_braces = line.count('{') - line.count('}')
            
            # Simple quote counting (not perfect but works for most cases)
            single_quotes = line.count("'") - line.count("\\'")
            double_quotes = line.count('"') - line.count('\&quot;')
            
            if (open_parens > 0 or open_brackets > 0 or open_braces > 0 or 
                single_quotes % 2 != 0 or double_quotes % 2 != 0):
                needs_continuation = True
            
            # Check if line ends with colon (block start)
            if line.rstrip().endswith(':'):
                needs_continuation = True
            
            # If multi-line is needed, collect additional lines
            if needs_continuation:
                lines = [line]
                while True:
                    try:
                        continuation = input("... ")
                        
                        # Empty line ends multi-line input
                        if not continuation.strip():
                            break
                        
                        lines.append(continuation)
                        
                        # Update bracket/paren counts
                        open_parens += continuation.count('(') - continuation.count(')')
                        open_brackets += continuation.count('[') - continuation.count(']')
                        open_braces += continuation.count('{') - continuation.count('}')
                        
                        # If all brackets are closed and line doesn't end with colon, we might be done
                        if (open_parens <= 0 and open_brackets <= 0 and open_braces <= 0 and
                            not continuation.rstrip().endswith(':')):
                            # Check if next line would be at same or lower indentation
                            # For now, continue until empty line
                            pass
                            
                    except EOFError:
                        break
                
                code = '\n'.join(lines)
            else:
                code = line
            
            # Execute the code
            if code.strip():
                interpreter = run_code(code, interpreter=interpreter)
                
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
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