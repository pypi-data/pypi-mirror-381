# Quick Reference

## 🚀 RenzMcLang Cheat Sheet

A quick reference guide for RenzMcLang syntax and features.

---

## 📝 Comments

```renzmc
// Single line comment
```

---

## 🔢 Variables

```renzmc
nama itu "Budi"              // String
umur itu 25                  // Integer
tinggi itu 175.5             // Float
aktif itu benar              // Boolean
```

---

## 📤 Output

```renzmc
tampilkan "Hello"            // Display
cetak "Hello"                // Print
tulis "Hello"                // Write
tunjukkan "Hello"            // Show
```

---

## 🔤 String Formatting

```renzmc
nama itu "Budi"
tampilkan f"Halo, {nama}!"   // F-string
```

---

## ➕ Operators

### Arithmetic
```renzmc
a + b        // Addition
a - b        // Subtraction
a * b        // Multiplication
a / b        // Division
a % b        // Modulo
a ** b       // Power
a // b       // Floor division
```

### Comparison
```renzmc
a == b       // Equal
a != b       // Not equal
a > b        // Greater than
a < b        // Less than
a >= b       // Greater or equal
a <= b       // Less or equal
```

### Logical
```renzmc
a dan b      // AND
a atau b     // OR
tidak a      // NOT
```

### Compound Assignment
```renzmc
x += 5       // x = x + 5
x -= 3       // x = x - 3
x *= 2       // x = x * 2
x /= 4       // x = x / 4
```

### Bitwise
```renzmc
a & b        // AND
a | b        // OR
a ^ b        // XOR
~a           // NOT
a << 1       // Left shift
a >> 1       // Right shift
```

---

## 🔀 Control Flow

### If-Else
```renzmc
jika kondisi
    // code
kalau tidak jika kondisi2
    // code
kalau tidak
    // code
selesai
```

### Ternary
```renzmc
hasil itu "A" jika x > 5 kalau tidak "B"
```

### Switch-Case
```renzmc
cocok nilai
    kasus 1:
        // code
    kasus 2:
        // code
    bawaan:
        // code
selesai
```

---

## 🔁 Loops

### For Loop
```renzmc
untuk i dari 1 sampai 10
    tampilkan i
selesai
```

### For Each
```renzmc
untuk setiap item dari daftar
    tampilkan item
selesai
```

### While Loop
```renzmc
selama kondisi
    // code
selesai
```

### Loop Control
```renzmc
lanjut       // Continue
berhenti     // Break
```

---

## 📦 Functions

### Basic Function
```renzmc
fungsi nama(param1, param2):
    // code
    kembali hasil
selesai
```

### Lambda Function
```renzmc
kuadrat itu lambda x: x * x
```

### Function Call
```renzmc
hasil itu nama(arg1, arg2)
```

---

## 📊 Data Structures

### List
```renzmc
daftar itu [1, 2, 3, 4, 5]
daftar[0]                    // Access
daftar[0:2]                  // Slice
```

### Dictionary
```renzmc
data itu {
    "key1": "value1",
    "key2": "value2"
}
data["key1"]                 // Access
```

### Set
```renzmc
himpunan itu {1, 2, 3, 4, 5}
```

### Tuple
```renzmc
tuple itu (1, 2, 3)
```

---

## 🎨 Comprehensions

### List Comprehension
```renzmc
kuadrat itu [x * x untuk x dari [1, 2, 3, 4, 5]]
genap itu [x untuk x dari [1, 2, 3, 4, 5, 6] jika x % 2 == 0]
```

### Dict Comprehension
```renzmc
dict itu {x: x * x untuk x dari [1, 2, 3, 4, 5]}
```

---

## 🛡️ Error Handling

```renzmc
coba
    // code
tangkap ErrorType sebagai e:
    // handle error
akhirnya
    // cleanup
selesai
```

---

## 🔌 Python Integration

### Import Module
```renzmc
impor_python "requests"
impor_python "json"
```

### Call Python Function
```renzmc
hasil itu panggil_python math.sqrt(16)
```

### Access Python Object
```renzmc
status itu response.status_code
```

---

## 📚 Built-in Functions

### String Functions
```renzmc
panjang(text)                // Length
huruf_besar(text)            // Uppercase
huruf_kecil(text)            // Lowercase
pisah(text, sep)             // Split
gabung(sep, items)           // Join
ganti(text, old, new)        // Replace
```

### Math Functions
```renzmc
akar(x)                      // Square root
pangkat(x, y)                // Power
absolut(x)                   // Absolute
bulat(x)                     // Round
```

### List Functions
```renzmc
tambah(list, item)           // Append
hapus(list, item)            // Remove
urutkan(list)                // Sort
balikkan(list)               // Reverse
minimum(list)                // Min
maksimum(list)               // Max
jumlah(list)                 // Sum
rata_rata(list)              // Average
```

### Iteration Functions
```renzmc
map(func, list)              // Map
filter(func, list)           // Filter
zip(list1, list2)            // Zip
enumerate(list)              // Enumerate
```

### File Functions
```renzmc
baca_file(path)              // Read file
tulis_file(path, content)    // Write file
hapus_file(path)             // Delete file
```

### System Functions
```renzmc
waktu()                      // Current time
tidur(seconds)               // Sleep
acak()                       // Random
```

---

## 🎯 OOP (Function-Based)

### Constructor
```renzmc
buat fungsi buat_orang dengan nama, umur
    orang itu {
        "nama": nama,
        "umur": umur
    }
    hasil orang
selesai
```

### Method
```renzmc
buat fungsi perkenalan dengan orang
    hasil f"Halo, {orang['nama']}"
selesai
```

### Usage
```renzmc
orang1 itu panggil buat_orang dengan "Budi", 25
pesan itu panggil perkenalan dengan orang1
```

---

## ⚡ Async/Await

```renzmc
impor_python "asyncio"

async fungsi fetch_data(url):
    await panggil_python asyncio.sleep(1)
    hasil f"Data from {url}"
selesai

async fungsi main():
    data itu await fetch_data("https://api.com")
    tampilkan data
selesai

panggil_python asyncio.run(main())
```

---

## 🎨 Context Manager

```renzmc
dengan buka("file.txt", "r") sebagai f:
    content itu f.read()
    tampilkan content
selesai
```

---

## 🔑 Keywords

### Control Flow
- `jika` / `kalau` - if
- `kalau tidak` - else
- `kalau tidak jika` - elif
- `selesai` - end
- `selama` - while
- `untuk` - for
- `dari` - from
- `sampai` - to
- `lanjut` - continue
- `berhenti` - break

### Functions
- `fungsi` - function
- `kembali` - return
- `lambda` - lambda
- `async` - async
- `await` - await

### OOP
- `buat fungsi` - create function
- `dengan` - with
- `panggil` - call

### Error Handling
- `coba` - try
- `tangkap` - catch
- `akhirnya` - finally
- `sebagai` - as

### Python Integration
- `impor_python` - import Python module
- `panggil_python` - call Python function

### Values
- `benar` - true
- `salah` - false
- `itu` - is/equals

### Operators
- `dan` - and
- `atau` - or
- `tidak` - not
- `dalam` - in

---

## 📖 File Extensions

- `.rmc` - RenzMcLang source files

---

## 🚀 Command Line

```bash
# Run file
rmc script.rmc

# Run code directly
rmc -c "tampilkan 'Hello'"

# Show version
rmc --version

# Interactive mode
rmc
```

---

## 💡 Tips

1. **Use f-strings** for string formatting
2. **Use comprehensions** for concise code
3. **Use built-in functions** when available
4. **Handle errors** with try-catch
5. **Import Python libraries** for extended functionality

---

## 📚 More Resources

- [Installation Guide](installation.md)
- [Syntax Basics](syntax-basics.md)
- [Built-in Functions](builtin-functions.md)
- [Advanced Features](advanced-features.md)
- [Python Integration](python-integration.md)
- [Examples](examples.md)

---

**Quick Reference v1.0 - RenzMcLang**

**Happy Coding! 🚀**