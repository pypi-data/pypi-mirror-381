# Python Integration

## 🔌 Introduction

One of RenzMcLang's most powerful features is seamless integration with Python. You can import and use any Python library, access Python objects, and call Python functions directly from RenzMcLang code.

## 📑 Table of Contents

- [Importing Python Modules](#importing-python-modules)
- [Calling Python Functions](#calling-python-functions)
- [Accessing Python Objects](#accessing-python-objects)
- [Using Python Libraries](#using-python-libraries)
- [Web Scraping Example](#web-scraping-example)
- [Data Analysis Example](#data-analysis-example)
- [Database Integration](#database-integration)
- [Best Practices](#best-practices)

---

## Importing Python Modules

Use `impor_python` to import Python modules:

```python
// Import single module
impor_python "math"
impor_python "os"
impor_python "sys"

// Import popular libraries
impor_python "requests"
impor_python "json"
impor_python "datetime"
impor_python "sqlite3"
```

---

## Calling Python Functions

Use `panggil_python` to call Python functions:

```python
impor_python "math"

// Call Python function
hasil itu panggil_python math.sqrt(16)
tampilkan hasil  // Output: 4.0

// Call with multiple arguments
power itu panggil_python math.pow(2, 3)
tampilkan power  // Output: 8.0

// Access constants
pi itu math.pi
tampilkan pi  // Output: 3.141592653589793
```

---

## Accessing Python Objects

Access Python object properties and methods:

```python
impor_python "datetime"

// Create Python object
sekarang itu panggil_python datetime.datetime.now()

// Access properties
tahun itu sekarang.year
bulan itu sekarang.month
hari itu sekarang.day

tampilkan f"Tanggal: {hari}/{bulan}/{tahun}"

// Call methods
formatted itu panggil_python sekarang.strftime("%Y-%m-%d %H:%M:%S")
tampilkan formatted
```

---

## Using Python Libraries

### Example 1: HTTP Requests

```python
impor_python "requests"

// Make GET request
response itu panggil_python requests.get("https://api.github.com")

// Access response properties
status itu response.status_code
text itu response.text

tampilkan f"Status: {status}"
tampilkan f"Response length: {panjang(text)} characters"

// Parse JSON response
data itu panggil_python response.json()
tampilkan data
```

### Example 2: File Operations

```python
impor_python "os"

// Get current directory
cwd itu panggil_python os.getcwd()
tampilkan f"Current directory: {cwd}"

// List files
files itu panggil_python os.listdir(".")
tampilkan "Files:"
untuk setiap file dari files
    tampilkan f"  - {file}"
selesai

// Check if path exists
exists itu panggil_python os.path.exists("data.txt")
tampilkan f"File exists: {exists}"
```

### Example 3: JSON Processing

```python
impor_python "json"

// Create data
data itu {
    "nama": "Budi",
    "umur": 25,
    "hobi": ["coding", "gaming"]
}

// Convert to JSON string
json_str itu panggil_python json.dumps(data)
tampilkan json_str

// Parse JSON string
parsed itu panggil_python json.loads(json_str)
tampilkan parsed["nama"]
```

---

## Web Scraping Example

Complete web scraping example using requests:

```python
// Import libraries
impor_python "requests"

tampilkan "=== Web Scraping Example ==="
tampilkan ""

// Make HTTP request
tampilkan "Making request to example.com..."
response itu panggil_python requests.get("https://example.com")

// Get status code
status itu response.status_code
tampilkan f"✓ Status Code: {status}"

// Get response text
text itu response.text
text_length itu panjang(text)
tampilkan f"✓ Response Length: {text_length} characters"

// Get headers
headers itu response.headers
tampilkan "✓ Headers received"

tampilkan ""
tampilkan "✓ Web scraping completed successfully!"
```

---

## Data Analysis Example

Using Python for data analysis:

```python
// Import libraries
impor_python "statistics"

tampilkan "=== Data Analysis Example ==="
tampilkan ""

// Sample data
data itu [23, 45, 67, 89, 12, 34, 56, 78, 90]

// Calculate statistics
mean itu panggil_python statistics.mean(data)
median itu panggil_python statistics.median(data)
stdev itu panggil_python statistics.stdev(data)

tampilkan f"Mean: {mean}"
tampilkan f"Median: {median}"
tampilkan f"Standard Deviation: {stdev}"
```

---

## Database Integration

### SQLite Example

```python
impor_python "sqlite3"

// Connect to database
conn itu panggil_python sqlite3.connect("database.db")
cursor itu panggil_python conn.cursor()

// Create table
panggil_python cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")

// Insert data
panggil_python cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Budi", 25))
panggil_python conn.commit()

// Query data
panggil_python cursor.execute("SELECT * FROM users")
results itu panggil_python cursor.fetchall()

untuk setiap row dari results
    tampilkan f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}"
selesai

// Close connection
panggil_python conn.close()
```

---

## Best Practices

### 1. Import at the Top

```python
// ✓ Good: Import at the top
impor_python "requests"
impor_python "json"
impor_python "os"

// Your code here...
```

### 2. Error Handling

```python
impor_python "requests"

coba
    response itu panggil_python requests.get("https://api.example.com")
    tampilkan response.status_code
tangkap Exception sebagai e:
    tampilkan f"Error: {e}"
selesai
```

### 3. Check Module Availability

```python
coba
    impor_python "pandas"
    tampilkan "✓ Pandas available"
tangkap ImportError:
    tampilkan "✗ Pandas not installed"
    tampilkan "Install with: pip install pandas"
selesai
```

### 4. Use Built-in Functions When Possible

```python
// ✓ Good: Use RenzMcLang built-in
data itu baca_file("data.txt")

// ✗ Less efficient: Use Python
impor_python "builtins"
file itu panggil_python builtins.open("data.txt", "r")
data itu panggil_python file.read()
```

---

## Available Python Libraries

RenzMcLang can use ANY Python library installed on your system:

### Popular Libraries

- **Web**: `requests`, `urllib`, `beautifulsoup4`, `selenium`
- **Data**: `pandas`, `numpy`, `scipy`
- **Database**: `sqlite3`, `pymongo`, `psycopg2`, `mysql-connector`
- **API**: `flask`, `fastapi`, `django`
- **ML/AI**: `tensorflow`, `pytorch`, `scikit-learn`
- **Image**: `pillow`, `opencv-python`
- **And many more!**

### Installing Libraries

```python
# Install via pip
pip install requests
pip install pandas
pip install beautifulsoup4
```

---

## Summary

RenzMcLang's Python integration provides:

- ✅ Full access to Python ecosystem
- ✅ Import any Python module
- ✅ Call Python functions seamlessly
- ✅ Access Python objects and properties
- ✅ Use popular libraries (requests, pandas, etc.)
- ✅ Database integration (SQLite, MySQL, MongoDB)
- ✅ Web scraping and API calls
- ✅ Data analysis and processing

**The entire Python ecosystem is at your fingertips!** 🐍

---

For more examples, see the [examples/python_integration](../examples/python_integration/) directory.

**Happy Coding with Python + RenzMcLang! 🚀**