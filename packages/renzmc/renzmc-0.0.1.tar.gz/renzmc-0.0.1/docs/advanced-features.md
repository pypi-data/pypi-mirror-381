# Advanced Features

## 🚀 Introduction

RenzMcLang supports advanced programming features including Object-Oriented Programming (OOP), asynchronous programming, decorators, and more. This guide covers all advanced features with working examples.

## 📑 Table of Contents

- [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
- [Lambda Functions](#lambda-functions)
- [List & Dictionary Comprehensions](#list--dictionary-comprehensions)
- [Async/Await](#asyncawait)
- [Decorators](#decorators)
- [Error Handling](#error-handling)
- [Context Managers (With Statement)](#context-managers-with-statement)
- [Generators](#generators)
- [Advanced Operators](#advanced-operators)

---

## Object-Oriented Programming (OOP)

### Basic Class Structure

RenzMcLang uses a function-based approach for OOP:

```python
// Constructor function
buat fungsi buat_orang dengan nama, umur
    orang itu {
        "nama": nama,
        "umur": umur
    }
    hasil orang
selesai

// Method function
buat fungsi perkenalan dengan orang
    hasil f"Halo, nama saya {orang['nama']}, umur {orang['umur']} tahun"
selesai

// Create object
orang1 itu panggil buat_orang dengan "Alice", 25

// Call method
pesan itu panggil perkenalan dengan orang1
tampilkan pesan
```

### Class with Properties

```python
// Bank Account class
buat fungsi buat_bank_account dengan pemilik, saldo_awal
    account itu {
        "pemilik": pemilik,
        "saldo": saldo_awal,
        "transaksi": []
    }
    hasil account
selesai

// Deposit method
buat fungsi deposit dengan account, jumlah
    account["saldo"] itu account["saldo"] + jumlah
    tambah(account["transaksi"], f"Deposit: +Rp {jumlah}")
    tampilkan f"✓ Deposit Rp {jumlah} berhasil"
selesai

// Withdraw method
buat fungsi withdraw dengan account, jumlah
    jika jumlah > account["saldo"]
        tampilkan "✗ Saldo tidak cukup"
        hasil salah
    selesai
    
    account["saldo"] itu account["saldo"] - jumlah
    tambah(account["transaksi"], f"Withdraw: -Rp {jumlah}")
    tampilkan f"✓ Withdraw Rp {jumlah} berhasil"
    hasil benar
selesai

// Usage
akun itu panggil buat_bank_account dengan "Budi", 1000000
panggil deposit dengan akun, 500000
panggil withdraw dengan akun, 200000
```

### Inheritance Pattern

```python
// Base class: Animal
buat fungsi buat_animal dengan nama, jenis
    animal itu {
        "nama": nama,
        "jenis": jenis
    }
    hasil animal
selesai

// Derived class: Dog (extends Animal)
buat fungsi buat_dog dengan nama, ras
    // Call parent constructor
    dog itu panggil buat_animal dengan nama, "Anjing"
    // Add specific properties
    dog["ras"] itu ras
    hasil dog
selesai

// Method for Dog
buat fungsi gonggong dengan dog
    tampilkan f"{dog['nama']} berkata: Woof! Woof!"
selesai

// Usage
anjing itu panggil buat_dog dengan "Buddy", "Golden Retriever"
panggil gonggong dengan anjing
```

---

## Lambda Functions

Lambda functions are anonymous functions for quick operations:

```python
// Simple lambda
kuadrat itu lambda x: x * x
tampilkan kuadrat(5)  // Output: 25

// Lambda with multiple parameters
tambah itu lambda x, y: x + y
tampilkan tambah(3, 4)  // Output: 7

// Lambda with condition
is_genap itu lambda x: x % 2 == 0
tampilkan is_genap(4)  // Output: benar

// Using lambda with map
angka itu [1, 2, 3, 4, 5]
kuadrat_list itu map(lambda x: x * x, angka)
tampilkan kuadrat_list  // Output: [1, 4, 9, 16, 25]
```

---

## List & Dictionary Comprehensions

### List Comprehension

```python
// Basic list comprehension
kuadrat itu [x * x untuk x dari [1, 2, 3, 4, 5]]
// Output: [1, 4, 9, 16, 25]

// With condition
genap itu [x untuk x dari [1, 2, 3, 4, 5, 6] jika x % 2 == 0]
// Output: [2, 4, 6]

// Nested comprehension
matrix itu [[i * j untuk j dari [1, 2, 3]] untuk i dari [1, 2, 3]]
// Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

### Dictionary Comprehension

```python
// Basic dict comprehension
kuadrat_dict itu {x: x * x untuk x dari [1, 2, 3, 4, 5]}
// Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

// With condition
genap_dict itu {x: x * x untuk x dari [1, 2, 3, 4, 5, 6] jika x % 2 == 0}
// Output: {2: 4, 4: 16, 6: 36}
```

---

## Async/Await

Asynchronous programming for concurrent operations:

```python
// Import async library
impor_python "asyncio"

// Async function
async fungsi fetch_data(url):
    tampilkan f"Fetching {url}..."
    await panggil_python asyncio.sleep(1)
    hasil f"Data from {url}"
selesai

// Main async function
async fungsi main():
    data1 itu await fetch_data("https://api1.com")
    data2 itu await fetch_data("https://api2.com")
    tampilkan data1
    tampilkan data2
selesai

// Run async function
panggil_python asyncio.run(main())
```

---

## Decorators

Decorators modify function behavior:

```python
// Timer decorator
buat fungsi timer_decorator dengan func
    buat fungsi wrapper(*args):
        start itu waktu()
        result itu panggil func dengan *args
        end itu waktu()
        tampilkan f"Execution time: {end - start} seconds"
        hasil result
    selesai
    hasil wrapper
selesai

// Apply decorator
@timer_decorator
fungsi slow_function():
    tidur(2)
    tampilkan "Function completed"
selesai
```

---

## Error Handling

Comprehensive error handling with try-catch-finally:

```python
// Basic try-catch
coba
    hasil itu 10 / 0
tangkap ZeroDivisionError sebagai e:
    tampilkan "Error: Tidak bisa membagi dengan nol!"
selesai

// Try-catch-finally
coba
    file itu baca_file("data.txt")
    tampilkan file
tangkap FileNotFoundError:
    tampilkan "File tidak ditemukan"
tangkap Exception sebagai e:
    tampilkan f"Error: {e}"
akhirnya
    tampilkan "Cleanup completed"
selesai
```

---

## Context Managers (With Statement)

Automatic resource management:

```python
// File handling with context manager
dengan buka("data.txt", "r") sebagai f:
    content itu f.read()
    tampilkan content
selesai
// File automatically closed

// Multiple context managers
dengan buka("input.txt", "r") sebagai f_in, buka("output.txt", "w") sebagai f_out:
    data itu f_in.read()
    f_out.write(data)
selesai
```

---

## Generators

Memory-efficient iteration:

```python
// Generator function
fungsi countdown(n):
    selama n > 0
        yield n
        n -= 1
    selesai
selesai

// Use generator
untuk setiap num dari countdown(5)
    tampilkan num
selesai
```

---

## Advanced Operators

### Walrus Operator (:=)

```python
// Assignment expression
jika (n := panjang(data)) > 10
    tampilkan f"Data has {n} items"
selesai
```

### Bitwise Operators

```python
a itu 5   // 0101 in binary
b itu 3   // 0011 in binary

tampilkan a & b    // AND: 1 (0001)
tampilkan a | b    // OR: 7 (0111)
tampilkan a ^ b    // XOR: 6 (0110)
tampilkan ~a       // NOT: -6
tampilkan a << 1   // Left shift: 10 (1010)
tampilkan a >> 1  // Right shift: 2 (0010)
```

---

## Summary

RenzMcLang supports all modern programming features:

- ✅ Object-Oriented Programming (function-based)
- ✅ Lambda functions and functional programming
- ✅ List and dictionary comprehensions
- ✅ Async/await for concurrent programming
- ✅ Decorators for function modification
- ✅ Comprehensive error handling
- ✅ Context managers for resource management
- ✅ Generators for memory efficiency
- ✅ Advanced operators (walrus, bitwise)

For more examples, see the [examples](../examples/) directory.

---

**Happy Advanced Coding with RenzMcLang! 🚀**