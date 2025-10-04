"""
Secure file operations module for RenzMC
Provides safe file I/O with validation and error handling
"""

from pathlib import Path
from typing import Optional, List, Union
from renzmc.utils.logging import logger
from renzmc.utils.validation import PathValidator, ValidationError
from renzmc.utils.rate_limiter import file_rate_limiter

class FileOperations:
    """
    Secure file operations with validation and rate limiting
    """
    
    def __init__(self):
        """Initialize file operations with validator"""
        self.validator = PathValidator()
        logger.info("FileOperations initialized")
    
    @file_rate_limiter
    def read_file(self, filename: str, encoding: str = 'utf-8') -> str:
        """
        Safely read file with validation
        
        Args:
            filename: Path to file
            encoding: File encoding (default: utf-8)
            
        Returns:
            File contents as string
            
        Raises:
            ValidationError: If file path is invalid
            FileNotFoundError: If file doesn't exist
            PermissionError: If no permission to read
            UnicodeDecodeError: If file encoding is invalid
        """
        try:
            filepath = self.validator.validate_file_read(filename)
            logger.debug(f"Reading file: {filepath}")
            
            with open(filepath, 'r', encoding=encoding) as f:
                content = f.read()
            
            logger.info(f"Successfully read file: {filename} ({len(content)} bytes)")
            return content
            
        except ValidationError as e:
            logger.error(f"Validation error reading file '{filename}': {e}")
            raise
        except FileNotFoundError:
            logger.error(f"File not found: {filename}")
            raise FileNotFoundError(f"File tidak ditemukan: {filename}")
        except PermissionError:
            logger.error(f"Permission denied reading file: {filename}")
            raise PermissionError(f"Tidak ada izin untuk membaca file: {filename}")
        except UnicodeDecodeError as e:
            logger.error(f"Encoding error reading file '{filename}': {e}")
            raise UnicodeDecodeError(
                e.encoding, e.object, e.start, e.end,
                f"File bukan {encoding} yang valid: {filename}"
            )
        except Exception as e:
            logger.error(f"Unexpected error reading file '{filename}': {e}", exc_info=True)
            raise RuntimeError(f"Error membaca file: {e}")
    
    @file_rate_limiter
    def write_file(
        self,
        filename: str,
        content: str,
        encoding: str = 'utf-8',
        mode: str = 'w'
    ) -> None:
        """
        Safely write file with validation
        
        Args:
            filename: Path to file
            content: Content to write
            encoding: File encoding (default: utf-8)
            mode: Write mode ('w' or 'a')
            
        Raises:
            ValidationError: If file path is invalid
            PermissionError: If no permission to write
        """
        if mode not in ('w', 'a'):
            raise ValueError(f"Mode tidak valid: {mode} (harus 'w' atau 'a')")
        
        try:
            filepath = self.validator.validate_file_write(filename)
            logger.debug(f"Writing file: {filepath} (mode: {mode})")
            
            filepath.parent.mkdir(parents=True, exist_ok=True)
            
            with open(filepath, mode, encoding=encoding) as f:
                f.write(content)
            
            logger.info(f"Successfully wrote file: {filename} ({len(content)} bytes)")
            
        except ValidationError as e:
            logger.error(f"Validation error writing file '{filename}': {e}")
            raise
        except PermissionError:
            logger.error(f"Permission denied writing file: {filename}")
            raise PermissionError(f"Tidak ada izin untuk menulis file: {filename}")
        except Exception as e:
            logger.error(f"Unexpected error writing file '{filename}': {e}", exc_info=True)
            raise RuntimeError(f"Error menulis file: {e}")
    
    @file_rate_limiter
    def append_file(self, filename: str, content: str, encoding: str = 'utf-8') -> None:
        """Append content to file"""
        self.write_file(filename, content, encoding=encoding, mode='a')
    
    @file_rate_limiter
    def delete_file(self, filename: str) -> None:
        """Safely delete file with validation"""
        try:
            filepath = self.validator.validate_path(filename)
            logger.debug(f"Deleting file: {filepath}")
            
            if not filepath.exists():
                raise FileNotFoundError(f"File tidak ditemukan: {filename}")
            
            if not filepath.is_file():
                raise ValueError(f"Bukan file: {filename}")
            
            filepath.unlink()
            logger.info(f"Successfully deleted file: {filename}")
            
        except ValidationError as e:
            logger.error(f"Validation error deleting file '{filename}': {e}")
            raise
        except FileNotFoundError:
            logger.error(f"File not found for deletion: {filename}")
            raise
        except PermissionError:
            logger.error(f"Permission denied deleting file: {filename}")
            raise PermissionError(f"Tidak ada izin untuk menghapus file: {filename}")
        except Exception as e:
            logger.error(f"Unexpected error deleting file '{filename}': {e}", exc_info=True)
            raise RuntimeError(f"Error menghapus file: {e}")
    
    @file_rate_limiter
    def file_exists(self, filename: str) -> bool:
        """Check if file exists"""
        try:
            filepath = self.validator.validate_path(filename)
            exists = filepath.exists() and filepath.is_file()
            logger.debug(f"File exists check: {filename} = {exists}")
            return exists
        except ValidationError as e:
            logger.warning(f"Validation error checking file existence '{filename}': {e}")
            return False
        except Exception as e:
            logger.error(f"Error checking file existence '{filename}': {e}")
            return False