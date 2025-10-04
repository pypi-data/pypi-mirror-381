# Installation Guide

## 📦 Installing RenzMcLang

RenzMcLang is a Python-based programming language with Indonesian syntax. Follow these steps to install it on your system.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Methods

#### Method 1: Install from PyPI (Recommended)

```bash
pip install renzmc
```

#### Method 2: Install from Source

```bash
# Clone the repository
git clone https://github.com/yourusername/RenzMcLang.git
cd RenzMcLang

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### Verifying Installation

After installation, verify that RenzMcLang is installed correctly:

```bash
rmc --version
```

You should see output similar to:
```
RenzmcLang 1.0.0
```

### Running Your First Program

Create a file named `hello.rmc`:

```python
tampilkan "Hello, World!"
```

Run it:

```bash
rmc hello.rmc
```

Output:
```
Hello, World!
```

### Interactive Mode (REPL)

Start the interactive interpreter:

```bash
rmc
```

You'll see:

```
RenzmcLang 1.0.0 - Bahasa pemrograman berbasis Bahasa Indonesia
Ketik 'keluar' untuk keluar dari interpreter.

>>> 
```

Try some commands:

```python
>>> tampilkan "Halo!"
Halo!
>>> angka itu 42
>>> tampilkan angka
42
>>> keluar
```

### Command Line Options

RenzMcLang supports several command-line options:

```bash
# Run a file
rmc script.rmc

# Run code directly
rmc -c "tampilkan 'Hello'"

# Show version
rmc --version

# Interactive mode (default when no arguments)
rmc
```

### Dependencies

RenzMcLang requires the following Python packages:

- `aiohttp>=3.8.1` - For async HTTP operations
- `requests>=2.27.1` - For HTTP requests
- `cryptography>=36.0.0` - For encryption features
- `python-dateutil>=2.8.2` - For date/time operations
- `pytz>=2021.3` - For timezone support
- `pyyaml>=6.0` - For YAML parsing
- `ujson>=5.1.0` - For fast JSON operations
- `regex>=2022.1.18` - For advanced regex support

These are automatically installed when you install RenzMcLang via pip.

### Troubleshooting

#### "rmc: command not found"

If you get this error, make sure Python's scripts directory is in your PATH:

**Linux/macOS:**
```bash
export PATH="$HOME/.local/bin:$PATH"
```

**Windows:**
Add `%APPDATA%\Python\Scripts` to your PATH environment variable.

#### Import Errors

If you encounter import errors, reinstall the dependencies:

```bash
pip install --upgrade -r requirements.txt
```

#### Permission Errors

On Linux/macOS, you might need to use `pip install --user`:

```bash
pip install --user renzmc
```

### Uninstallation

To uninstall RenzMcLang:

```bash
pip uninstall renzmc
```

### Next Steps

- Read the [Syntax Basics](syntax-basics.md) guide
- Explore [Built-in Functions](builtin-functions.md)
- Check out [Examples](examples.md)
- Learn about [Python Integration](python-integration.md)

---

**Need Help?** Visit our [GitHub repository](https://github.com/yourusername/RenzMcLang) or open an issue.