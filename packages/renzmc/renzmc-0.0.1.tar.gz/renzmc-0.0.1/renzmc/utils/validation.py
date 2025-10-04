"""
Input validation utilities for RenzMC
Provides secure validation for file paths, strings, and other inputs
"""

from pathlib import Path
from typing import Union, Set, Optional
import re

class ValidationError(Exception):
    """Raised when validation fails"""
    pass

class PathValidator:
    """
    Secure path validation to prevent path traversal attacks
    """
    
    def __init__(
        self,
        base_dir: Optional[Path] = None,
        allowed_extensions: Optional[Set[str]] = None,
        max_file_size: int = 10_000_000  # 10MB default
    ):
        """
        Initialize path validator
        
        Args:
            base_dir: Base directory for path validation (default: cwd)
            allowed_extensions: Set of allowed file extensions
            max_file_size: Maximum file size in bytes
        """
        self.base_dir = (base_dir or Path.cwd()).resolve()
        self.allowed_extensions = allowed_extensions or {
            '.txt', '.json', '.csv', '.md', '.rmc', '.py',
            '.yaml', '.yml', '.xml', '.html', '.css', '.js'
        }
        self.max_file_size = max_file_size
        
        # Dangerous patterns to block
        self.dangerous_patterns = [
            '..',  # Parent directory traversal
            '~',   # Home directory expansion
            '$',   # Variable expansion
            '`',   # Command substitution
            '|',   # Pipe
            ';',   # Command separator
            '&',   # Background execution
            '\x00', # Null byte
        ]
    
    def validate_path(self, filepath: Union[str, Path]) -> Path:
        """
        Validate and sanitize file path
        
        Args:
            filepath: Path to validate
            
        Returns:
            Validated absolute Path object
            
        Raises:
            ValidationError: If path is invalid or dangerous
        """
        if not filepath:
            raise ValidationError("Nama file tidak boleh kosong")
        
        filepath_str = str(filepath)
        
        # Check for dangerous patterns
        for pattern in self.dangerous_patterns:
            if pattern in filepath_str:
                raise ValidationError(
                    f"Nama file mengandung karakter berbahaya: '{pattern}'"
                )
        
        # Resolve to absolute path
        try:
            abs_path = (self.base_dir / filepath).resolve()
        except (ValueError, OSError) as e:
            raise ValidationError(f"Path tidak valid: {e}")
        
        # Ensure path is within base directory
        try:
            abs_path.relative_to(self.base_dir)
        except ValueError:
            raise ValidationError(
                f"Akses ditolak: File di luar direktori yang diizinkan\n"
                f"Base: {self.base_dir}\n"
                f"Requested: {abs_path}"
            )
        
        return abs_path
    
    def validate_file_read(self, filepath: Union[str, Path]) -> Path:
        """
        Validate file for reading
        
        Args:
            filepath: Path to validate
            
        Returns:
            Validated Path object
            
        Raises:
            ValidationError: If file cannot be read
        """
        abs_path = self.validate_path(filepath)
        
        # Check file exists
        if not abs_path.exists():
            raise ValidationError(f"File tidak ditemukan: {filepath}")
        
        # Check it's a file
        if not abs_path.is_file():
            raise ValidationError(f"Bukan file: {filepath}")
        
        # Check file size
        size = abs_path.stat().st_size
        if size > self.max_file_size:
            raise ValidationError(
                f"File terlalu besar: {size:,} bytes "
                f"(maksimum: {self.max_file_size:,} bytes)"
            )
        
        # Check extension
        if abs_path.suffix.lower() not in self.allowed_extensions:
            raise ValidationError(
                f"Ekstensi file tidak diizinkan: {abs_path.suffix}\n"
                f"Ekstensi yang diizinkan: {', '.join(sorted(self.allowed_extensions))}"
            )
        
        return abs_path
    
    def validate_file_write(self, filepath: Union[str, Path]) -> Path:
        """
        Validate file for writing
        
        Args:
            filepath: Path to validate
            
        Returns:
            Validated Path object
            
        Raises:
            ValidationError: If file cannot be written
        """
        abs_path = self.validate_path(filepath)
        
        # Check extension
        if abs_path.suffix.lower() not in self.allowed_extensions:
            raise ValidationError(
                f"Ekstensi file tidak diizinkan: {abs_path.suffix}\n"
                f"Ekstensi yang diizinkan: {', '.join(sorted(self.allowed_extensions))}"
            )
        
        # Check parent directory exists
        if not abs_path.parent.exists():
            raise ValidationError(f"Direktori tidak ditemukan: {abs_path.parent}")
        
        return abs_path

class StringValidator:
    """
    String validation utilities
    """
    
    @staticmethod
    def validate_identifier(name: str) -> str:
        """
        Validate identifier name
        
        Args:
            name: Identifier to validate
            
        Returns:
            Validated identifier
            
        Raises:
            ValidationError: If identifier is invalid
        """
        if not name:
            raise ValidationError("Nama identifier tidak boleh kosong")
        
        # Check valid identifier pattern
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name):
            raise ValidationError(
                f"Identifier tidak valid: '{name}'\n"
                f"Identifier harus dimulai dengan huruf atau underscore, "
                f"dan hanya boleh mengandung huruf, angka, dan underscore"
            )
        
        # Check length
        if len(name) > 255:
            raise ValidationError(f"Identifier terlalu panjang (maksimum 255 karakter)")
        
        return name
    
    @staticmethod
    def validate_url(url: str) -> str:
        """
        Validate URL
        
        Args:
            url: URL to validate
            
        Returns:
            Validated URL
            
        Raises:
            ValidationError: If URL is invalid
        """
        if not url:
            raise ValidationError("URL tidak boleh kosong")
        
        # Basic URL validation
        url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE
        )
        
        if not url_pattern.match(url):
            raise ValidationError(f"URL tidak valid: {url}")
        
        # Block dangerous protocols
        if url.lower().startswith(('file://', 'ftp://', 'data:')):
            raise ValidationError(f"Protocol tidak diizinkan: {url}")
        
        return url

# Global validator instances
path_validator = PathValidator()
string_validator = StringValidator()