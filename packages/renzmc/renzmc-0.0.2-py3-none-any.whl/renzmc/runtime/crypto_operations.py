"""
Cryptography operations for RenzmcLang

This module handles encryption, decryption, and hashing operations.
"""

import hashlib
import uuid
import base64
import urllib.parse

# Safe cryptography imports
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    Fernet = None
    hashes = None
    PBKDF2HMAC = None
    CRYPTOGRAPHY_AVAILABLE = False


class CryptoOperations:
    """
    Handles cryptography operations for the interpreter
    """
    
    @staticmethod
    def encrypt(text, key):
        """Encrypt text with key"""
        if not CRYPTOGRAPHY_AVAILABLE:
            raise ImportError("Cryptography library tidak tersedia")
        
        try:
            # Convert key to bytes if it's a string
            if isinstance(key, str):
                key_bytes = key.encode('utf-8')
            else:
                key_bytes = key
            
            # Generate a key from the password
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=b'salt_',  # In production, use a random salt
                iterations=100000,
            )
            derived_key = base64.urlsafe_b64encode(kdf.derive(key_bytes))
            
            # Create Fernet cipher
            cipher = Fernet(derived_key)
            
            # Encrypt the text
            encrypted = cipher.encrypt(text.encode('utf-8'))
            
            # Return base64 encoded string
            return base64.b64encode(encrypted).decode('utf-8')
        
        except Exception as e:
            raise ValueError(f"Error dalam enkripsi: {str(e)}")
    
    @staticmethod
    def decrypt(encrypted_text, key):
        """Decrypt text with key"""
        if not CRYPTOGRAPHY_AVAILABLE:
            raise ImportError("Cryptography library tidak tersedia")
        
        try:
            # Convert key to bytes if it's a string
            if isinstance(key, str):
                key_bytes = key.encode('utf-8')
            else:
                key_bytes = key
            
            # Generate the same key from the password
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=b'salt_',  # Same salt as encryption
                iterations=100000,
            )
            derived_key = base64.urlsafe_b64encode(kdf.derive(key_bytes))
            
            # Create Fernet cipher
            cipher = Fernet(derived_key)
            
            # Decode from base64
            encrypted_bytes = base64.b64decode(encrypted_text.encode('utf-8'))
            
            # Decrypt the text
            decrypted = cipher.decrypt(encrypted_bytes)
            
            return decrypted.decode('utf-8')
        
        except Exception as e:
            raise ValueError(f"Error dalam dekripsi: {str(e)}")
    
    @staticmethod
    def hash_text(text, algorithm='sha256'):
        """Hash text with specified algorithm"""
        try:
            if algorithm == 'md5':
                return hashlib.md5(text.encode('utf-8')).hexdigest()
            elif algorithm == 'sha1':
                return hashlib.sha1(text.encode('utf-8')).hexdigest()
            elif algorithm == 'sha256':
                return hashlib.sha256(text.encode('utf-8')).hexdigest()
            elif algorithm == 'sha512':
                return hashlib.sha512(text.encode('utf-8')).hexdigest()
            else:
                raise ValueError(f"Algoritma hash tidak didukung: {algorithm}")
        except Exception as e:
            raise ValueError(f"Error dalam hashing: {str(e)}")
    
    @staticmethod
    def create_uuid():
        """Generate a new UUID"""
        return str(uuid.uuid4())
    
    @staticmethod
    def url_encode(text):
        """URL encode text"""
        return urllib.parse.quote(text)
    
    @staticmethod
    def url_decode(text):
        """URL decode text"""
        return urllib.parse.unquote(text)