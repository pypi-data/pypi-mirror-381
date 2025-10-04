# Syntax Basics

## 🎯 Introduction

RenzMcLang is a programming language with Indonesian syntax that compiles to Python. This guide covers the fundamental syntax and features.

## 📝 Comments

Comments are lines that are ignored by the interpreter:

```python
// This is a single-line comment

tampilkan "Hello"  // Comment after code
```

## 🔢 Variables and Data Types

### Variable Declaration

Variables are declared using the `itu` keyword (meaning "is"):

```python
nama itu "Budi"
umur itu 25
tinggi itu 175.5
aktif itu benar
```

### Data Types

```python
// Numbers (integers and floats)
angka_bulat itu 42
angka_desimal itu 3.14

// Strings
teks itu "Hello, World!"
teks2 itu 'Single quotes work too'

// Booleans
benar_value itu benar  // true
salah_value itu salah  // false

// Lists
daftar itu [1, 2, 3, 4, 5]
nama_list itu ["Ali", "Budi", "Citra"]

// Dictionaries
data itu {
    "nama": "Budi",
    "umur": 25,
    "kota": "Jakarta"
}
```

### String Formatting (F-Strings)

```python
nama itu "Budi"
umur itu 25

tampilkan f"Nama saya {nama} dan umur saya {umur} tahun"
// Output: Nama saya Budi dan umur saya 25 tahun

// With expressions
tampilkan f"Tahun depan saya akan berumur {umur + 1} tahun"
```

## 📤 Output

### Print Statements

Multiple keywords for printing:

```python
tampilkan "Hello"  // display
cetak "Hello"     // print
tulis "Hello"     // write
tunjukkan "Hello" // show
```

## ➕ Operators

### Arithmetic Operators

```python
a itu 10
b itu 3

tambah itu a + b      // 13
kurang itu a - b      // 7
kali itu a * b        // 30
bagi itu a / b        // 3.333...
sisa itu a % b        // 1 (modulo)
pangkat itu a ** b     // 1000 (power)
bagi_bulat itu a // b  // 3 (floor division)
```

### Comparison Operators

```python
a itu 10
b itu 5

a == b  // Equal to (salah)
a != b  // Not equal to (benar)
a > b   // Greater than (benar)
a < b   // Less than (salah)
a >= b  // Greater than or equal (benar)
a <= b  // Less than or equal (salah)
```

### Logical Operators

```python
a itu benar
b itu salah

a dan b   // AND (salah)
a atau b  // OR (benar)
tidak a   // NOT (salah)
```

### Compound Assignment Operators

```python
x itu 10

x += 5   // x = x + 5 (15)
x -= 3   // x = x - 3 (12)
x *= 2   // x = x * 2 (24)
x /= 4   // x = x / 4 (6.0)
```

### Bitwise Operators

```python
a itu 5   // 0101 in binary
b itu 3   // 0011 in binary

a & b    // Bitwise AND (1)
a | b    // Bitwise OR (7)
a ^ b    // Bitwise XOR (6)
~a       // Bitwise NOT (-6)
a << 1   // Left shift (10)
a >> 1  // Right shift (2)
```

## 🔀 Control Flow

### If-Else Statements

```python
angka itu 10

jika angka > 0
    tampilkan "Positif"
kalau tidak jika angka < 0
    tampilkan "Negatif"
kalau tidak
    tampilkan "Nol"
selesai
```

Alternative `kalau` keyword:

```python
kalau angka % 2 == 0
    tampilkan "Genap"
kalau tidak
    tampilkan "Ganjil"
selesai
```

### Ternary Operator

```python
umur itu 20
status itu "Dewasa" jika umur >= 18 kalau tidak "Anak-anak"
tampilkan status  // Output: Dewasa
```

### Switch-Case (Match)

```python
hari itu 3

cocok hari
    kasus 1:
        tampilkan "Senin"
    kasus 2:
        tampilkan "Selasa"
    kasus 3:
        tampilkan "Rabu"
    bawaan:
        tampilkan "Hari lain"
selesai
```

## 🔁 Loops

### For Loop (Range)

```python
// Loop from 1 to 10
untuk i dari 1 sampai 10
    tampilkan i
selesai
```

### For Each Loop

```python
buah itu ["Apel", "Jeruk", "Mangga"]

untuk setiap item dari buah
    tampilkan item
selesai
```

### While Loop

```python
counter itu 0

selama counter < 5
    tampilkan counter
    counter += 1
selesai
```

### Loop Control

```python
untuk i dari 1 sampai 10
    jika i == 3
        lanjut  // Skip to next iteration (continue)
    selesai
    
    jika i == 8
        berhenti  // Exit loop (break)
    selesai
    
    tampilkan i
selesai
```

## 📦 Functions

### Function Definition

```python
fungsi sapa(nama):
    tampilkan f"Halo, {nama}!"
selesai

// Call the function
sapa("Budi")
```

### Function with Return Value

```python
fungsi tambah(a, b):
    kembali a + b
selesai

hasil itu tambah(5, 3)
tampilkan hasil  // Output: 8
```

### Function with Default Parameters

```python
fungsi sapa_dengan_gelar(nama, gelar="Bapak"):
    tampilkan f"{gelar} {nama}"
selesai

sapa_dengan_gelar("Budi")              // Output: Bapak Budi
sapa_dengan_gelar("Ani", "Ibu")      // Output: Ibu Ani
```

### Lambda Functions

```python
kuadrat itu lambda x: x * x
tampilkan kuadrat(5)  // Output: 25

// Lambda with multiple parameters
tambah itu lambda x, y: x + y
tampilkan tambah(3, 4)  // Output: 7
```

## 🎨 List and Dictionary Operations

### List Operations

```python
angka itu [1, 2, 3]

// Access elements
tampilkan angka[0]  // Output: 1

// Slicing
tampilkan angka[0:2]  // Output: [1, 2]

// Modify
angka[0] itu 10
tampilkan angka  // Output: [10, 2, 3]
```

### Dictionary Operations

```python
mahasiswa itu {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

// Access values
tampilkan mahasiswa["nama"]  // Output: Budi

// Add/modify
mahasiswa["ipk"] itu 3.8
```

### List Comprehension

```python
// Create list of squares
kuadrat itu [x * x untuk x dari [1, 2, 3, 4, 5]]
tampilkan kuadrat  // Output: [1, 4, 9, 16, 25]

// With condition
genap itu [x untuk x dari [1, 2, 3, 4, 5, 6] jika x % 2 == 0]
tampilkan genap  // Output: [2, 4, 6]
```

## 🛡️ Error Handling

```python
coba
    angka itu 10 / 0
tangkap ZeroDivisionError sebagai e:
    tampilkan "Error: Tidak bisa membagi dengan nol!"
akhirnya
    tampilkan "Selesai"
selesai
```

## 📚 Next Steps

- Learn about [Built-in Functions](builtin-functions.md)
- Explore [Advanced Features](advanced-features.md)
- Check out [Python Integration](python-integration.md)
- See [Examples](examples.md) for practical code

---

**Happy Coding with RenzMcLang! 🚀**