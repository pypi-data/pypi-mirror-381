#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

long_description = """
RenzMcLang adalah bahasa pemrograman modern berbasis Bahasa Indonesia.
Dirancang untuk memudahkan pembelajaran pemrograman bagi penutur Bahasa Indonesia,
RenzMcLang menggabungkan fitur-fitur modern dengan sintaks yang intuitif.

Fitur Utama:
- Sintaks Bahasa Indonesia yang mudah dipahami
- Dukungan OOP lengkap (class, inheritance)
- Lambda, comprehension, ternary operator
- Async/await untuk pemrograman asynchronous
- Error handling dengan try/catch/finally
- Type hints optional

Integrasi Python:
- Akses library dan builtins Python
- Interoperabilitas penuh dengan ekosistem Python

Built-in Functions:
- Manipulasi string, math & statistics, file, JSON, HTTP, system, database, dll

Instalasi:
pip install renzmc

Quick Start:
# hello.rmc
tampilkan "Hello, World!"
tampilkan "Selamat datang di RenzMcLang!"
Jalankan: rmc hello.rmc

Dokumentasi: https://github.com/RenzMc/RenzmcLang
License: MIT License
"""

version = {}
with open(os.path.join("renzmc", "version.py"), "r", encoding="utf-8") as fh:
    exec(fh.read(), version)

setup(
    name="renzmc",
    version=version["__version__"],
    author="RenzMc",
    author_email="renzaja11@gmail.com",
    description="Bahasa pemrograman berbasis Bahasa Indonesia yang powerful dan modern",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RenzMc/RenzmcLang",
    project_urls={
        "Bug Tracker": "https://github.com/RenzMc/RenzmcLang/issues",
        "Documentation": "https://github.com/RenzMc/RenzmcLang/tree/main/docs",
        "Source Code": "https://github.com/RenzMc/RenzmcLang",
        "Examples": "https://github.com/RenzMc/RenzmcLang/tree/main/examples",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Interpreters",
        "Natural Language :: Indonesian",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "indonesian", "bahasa-indonesia", "programming-language", "interpreter",
        "education", "coding", "pemrograman", "python", "compiler", "modern-language"
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "aiohttp>=3.8.1",
        "requests>=2.27.1",
        "cryptography>=36.0.0",
        "python-dateutil>=2.8.2",
        "pytz>=2021.3",
        "pyyaml>=6.0",
        "ujson>=5.1.0",
        "regex>=2022.1.18",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.18.0",
            "black>=22.1.0",
            "isort>=5.10.1",
            "mypy>=0.931",
            "flake8>=4.0.1",
            "pylint",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "rmc=renzmc.__main__:main",
            "renzmc=renzmc.__main__:main",
        ],
    },
    include_package_data=True,
    package_data={
        "renzmc": [
            "examples/**/*.rmc",
            "docs/*.md",
            "*.png",
            "icon.png",
        ],
    },
    zip_safe=False,
    platforms=["any"],
)
