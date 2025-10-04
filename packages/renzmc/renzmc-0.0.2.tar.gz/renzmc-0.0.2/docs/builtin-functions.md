# Built-in Functions Reference

RenzMcLang provides 118+ built-in functions for common programming tasks. All functions are available without any imports.

## Table of Contents

- [Basic Functions](#basic-functions)
- [String Functions](#string-functions)
- [String Validation](#string-validation)
- [Math Functions](#math-functions)
- [Statistics](#statistics)
- [List Functions](#list-functions)
- [Iteration Functions](#iteration-functions)
- [Dictionary Functions](#dictionary-functions)
- [File Operations](#file-operations)
- [Path Operations](#path-operations)
- [System Functions](#system-functions)
- [JSON & Utility](#json-&-utility)
- [HTTP Functions](#http-functions)

---

## Basic Functions

### `panjang(obj)`

Get the length of an object

```python
// Example
data itu [1, 2, 3]
hasil itu panjang(data)
```

### `jenis(obj)`

Get the type of an object

```python
// Example
data itu [1, 2, 3]
hasil itu jenis(data)
```

### `ke_teks(obj)`

Convert an object to text

```python
// Example
hasil itu ke_teks(...)
```

### `ke_angka(obj)`

Convert an object to a number

```python
// Example
hasil itu ke_angka(...)
```

---

## String Functions

### `huruf_besar(text)`

Convert text to uppercase

```python
// Example
teks itu "Hello"
hasil itu huruf_besar(teks)
```

### `huruf_kecil(text)`

Convert text to lowercase

```python
// Example
teks itu "Hello"
hasil itu huruf_kecil(teks)
```

### `potong(text, start, end=None)`

Get a substring from a text

```python
// Example
hasil itu potong(...)
```

### `gabung(separator, *items)`

Join items with a separator

```python
// Example
hasil itu gabung(...)
```

### `pisah(text, separator=None)`

Split a text by a separator

```python
// Example
hasil itu pisah(...)
```

### `ganti(text, old, new)`

Replace occurrences of a substring in a text

```python
// Example
hasil itu ganti(...)
```

### `mulai_dengan(text, prefix)`

Check if a text starts with a prefix

```python
// Example
hasil itu mulai_dengan(...)
```

### `akhir_dengan(text, suffix)`

Check if a text ends with a suffix

```python
// Example
hasil itu akhir_dengan(...)
```

### `berisi(text, substring)`

Check if a text contains a substring

```python
// Example
hasil itu berisi(...)
```

### `hapus_spasi(text)`

Remove leading and trailing whitespace from a text

```python
// Example
hasil itu hapus_spasi(...)
```

---

## String Validation

### `is_alpha(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu is_alpha(...)
```

### `adalah_huruf(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
teks itu "Hello"
hasil itu adalah_huruf(teks)
```

### `is_digit(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu is_digit(...)
```

### `adalah_angka(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu adalah_angka(...)
```

### `is_alnum(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu is_alnum(...)
```

### `adalah_alfanumerik(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu adalah_alfanumerik(...)
```

### `is_lower(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu is_lower(...)
```

### `adalah_huruf_kecil(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
teks itu "Hello"
hasil itu adalah_huruf_kecil(teks)
```

### `is_upper(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu is_upper(...)
```

### `adalah_huruf_besar(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
teks itu "Hello"
hasil itu adalah_huruf_besar(teks)
```

### `is_space(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu is_space(...)
```

### `adalah_spasi(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu adalah_spasi(...)
```

---

## Math Functions

### `bulat(number)`

Convert a number to an integer

```python
// Example
angka itu 16
hasil itu bulat(angka)
```

### `desimal(number)`

Convert a number to a decimal

```python
// Example
angka itu 16
hasil itu desimal(angka)
```

### `akar(number)`

Calculate the square root of a number

```python
// Example
angka itu 16
hasil itu akar(angka)
```

### `pangkat(base, exponent)`

Calculate the power of a number

```python
// Example
angka itu 16
hasil itu pangkat(angka)
```

### `absolut(number)`

Calculate the absolute value of a number

```python
// Example
angka itu 16
hasil itu absolut(angka)
```

### `pembulatan(number)`

Round a number to the nearest integer

```python
// Example
angka itu 16
hasil itu pembulatan(angka)
```

### `pembulatan_atas(number)`

Round a number up to the nearest integer

```python
// Example
angka itu 16
hasil itu pembulatan_atas(angka)
```

### `pembulatan_bawah(number)`

Round a number down to the nearest integer

```python
// Example
angka itu 16
hasil itu pembulatan_bawah(angka)
```

### `sinus(angle)`

Calculate the sine of an angle in radians

```python
// Example
angka itu 16
hasil itu sinus(angka)
```

### `cosinus(angle)`

Calculate the cosine of an angle in radians

```python
// Example
angka itu 16
hasil itu cosinus(angka)
```

### `tangen(angle)`

Calculate the tangent of an angle in radians

```python
// Example
angka itu 16
hasil itu tangen(angka)
```

---

## Statistics

### `median(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu median(...)
```

### `nilai_tengah(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu nilai_tengah(...)
```

### `mode(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu mode(...)
```

### `nilai_modus(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu nilai_modus(...)
```

### `stdev(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu stdev(...)
```

### `deviasi_standar(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu deviasi_standar(...)
```

### `variance(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu variance(...)
```

### `variansi(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu variansi(...)
```

### `quantiles(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu quantiles(...)
```

### `kuantil(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu kuantil(...)
```

---

## List Functions

### `tambah(lst, item)`

Add an item to a list

```python
// Example
hasil itu tambah(...)
```

### `hapus(lst, item)`

Remove an item from a list

```python
// Example
hasil itu hapus(...)
```

### `hapus_pada(lst, index)`

Remove an item at a specific index from a list

```python
// Example
hasil itu hapus_pada(...)
```

### `masukkan(lst, index, item)`

Insert an item at a specific index in a list

```python
// Example
hasil itu masukkan(...)
```

### `urutkan(lst, terbalik=False)`

Sort a list in-place

```python
// Example
hasil itu urutkan(...)
```

### `balikkan(lst)`

Reverse a list in-place

```python
// Example
hasil itu balikkan(...)
```

### `hitung(lst, item)`

Count occurrences of an item in a list

```python
// Example
hasil itu hitung(...)
```

### `indeks(lst, item)`

Find the index of an item in a list

```python
// Example
hasil itu indeks(...)
```

### `extend(lst, iterable)`

Extend list with another iterable

```python
// Example
hasil itu extend(...)
```

### `salin(obj)`

Create a shallow copy of an object

```python
// Example
hasil itu salin(...)
```

### `salin_dalam(obj)`

Create a deep copy of an object

```python
// Example
hasil itu salin_dalam(...)
```

### `minimum(*args)`

Find the minimum value

```python
// Example
hasil itu minimum(...)
```

### `maksimum(*args)`

Find the maximum value

```python
// Example
hasil itu maksimum(...)
```

### `jumlah(*args)`

Calculate the sum of numbers

```python
// Example
hasil itu jumlah(...)
```

### `rata_rata(*args)`

Calculate the average of numbers

```python
// Example
hasil itu rata_rata(...)
```

---

## Iteration Functions

### `zip(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu zip(...)
```

### `enumerate(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu enumerate(...)
```

### `filter(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu filter(...)
```

### `saring(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu saring(...)
```

### `map(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu map(...)
```

### `peta(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu peta(...)
```

### `reduce(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu reduce(...)
```

### `kurangi(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu kurangi(...)
```

### `all(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu all(...)
```

### `semua(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu semua(...)
```

### `any(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu any(...)
```

### `ada(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu ada(...)
```

### `sorted(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu sorted(...)
```

### `terurut(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu terurut(...)
```

---

## Dictionary Functions

### `kunci(dictionary)`

Get the keys of a dictionary

```python
// Example
hasil itu kunci(...)
```

### `nilai(dictionary)`

Get the values of a dictionary

```python
// Example
hasil itu nilai(...)
```

### `item(dictionary)`

Get the items of a dictionary

```python
// Example
hasil itu item(...)
```

### `hapus_kunci(dictionary, key)`

Remove a key-value pair from a dictionary

```python
// Example
hasil itu hapus_kunci(...)
```

---

## File Operations

### `baca_file(filename)`

Read the contents of a file

```python
// Example
hasil itu baca_file(...)
```

### `tulis_file(filename, content)`

Write content to a file

```python
// Example
hasil itu tulis_file(...)
```

### `tambah_file(filename, content)`

Append content to a file

```python
// Example
hasil itu tambah_file(...)
```

### `hapus_file(filename)`

Delete a file

```python
// Example
hasil itu hapus_file(...)
```

### `file_exists(path)`

Check if a file exists

```python
// Example
hasil itu file_exists(...)
```

---

## Path Operations

### `direktori_ada(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu direktori_ada(...)
```

### `direktori_sekarang(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu direktori_sekarang(...)
```

### `ubah_direktori(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu ubah_direktori(...)
```

### `pisah_path(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu pisah_path(...)
```

### `ekstensi_file(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu ekstensi_file(...)
```

### `nama_file_tanpa_ekstensi(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu nama_file_tanpa_ekstensi(...)
```

### `path_ada(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu path_ada(...)
```

### `adalah_file(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu adalah_file(...)
```

### `adalah_direktori(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu adalah_direktori(...)
```

### `path_absolut(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu path_absolut(...)
```

### `gabung_path(*paths)`

Join path components

```python
// Example
hasil itu gabung_path(...)
```

### `buat_direktori(path)`

Create a directory

```python
// Example
hasil itu buat_direktori(...)
```

### `daftar_direktori(path='.')`

List files in a directory

```python
// Example
hasil itu daftar_direktori(...)
```

### `waktu_modifikasi_file(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu waktu_modifikasi_file(...)
```

### `waktu_buat_file(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu waktu_buat_file(...)
```

### `file_dapat_dibaca(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu file_dapat_dibaca(...)
```

### `file_dapat_ditulis(*args, **kwargs)`

Wrapper for RenzmcLang builtin functions

```python
// Example
hasil itu file_dapat_ditulis(...)
```

---

## System Functions

### `acak(min_val=0, max_val=1)`

Generate a random number

```python
// Example
hasil itu acak(...)
```

### `waktu()`

Get the current timestamp

```python
// Example
hasil itu waktu(...)
```

### `tidur(seconds)`

Sleep for a number of seconds

```python
// Example
hasil itu tidur(...)
```

### `tanggal()`

Get the current date and time

```python
// Example
hasil itu tanggal(...)
```

### `jalankan_perintah(command, sandbox=None, working_dir=None, timeout=None)`

Run a shell command safely with enhanced sandbox protection and resource limits

```python
// Example
hasil itu jalankan_perintah(...)
```

### `atur_sandbox(enabled)`

Enable or disable sandbox mode globally

```python
// Example
hasil itu atur_sandbox(...)
```

### `tambah_perintah_aman(command)`

Add a command to the safe commands whitelist

```python
// Example
hasil itu tambah_perintah_aman(...)
```

### `hapus_perintah_aman(command)`

Remove a command from the safe commands whitelist

```python
// Example
hasil itu hapus_perintah_aman(...)
```

---

## JSON & Utility

### `json_ke_teks(obj)`

Convert an object to JSON text

```python
// Example
hasil itu json_ke_teks(...)
```

### `teks_ke_json(text)`

Convert JSON text to an object

```python
// Example
hasil itu teks_ke_json(...)
```

### `hash_teks(text, algorithm='sha256')`

Hash text

```python
// Example
hasil itu hash_teks(...)
```

### `buat_uuid()`

Create a UUID

```python
// Example
hasil itu buat_uuid(...)
```

### `url_encode(text)`

URL encode text

```python
// Example
hasil itu url_encode(...)
```

### `url_decode(text)`

URL decode text

```python
// Example
hasil itu url_decode(...)
```

### `base64_encode(text)`

Base64 encode text

```python
// Example
hasil itu base64_encode(...)
```

### `base64_decode(text)`

Base64 decode text

```python
// Example
hasil itu base64_decode(...)
```

### `regex_match(pattern, text)`

Match a regex pattern against text

```python
// Example
hasil itu regex_match(...)
```

### `regex_replace(pattern, replacement, text)`

Replace text matching a regex pattern

```python
// Example
hasil itu regex_replace(...)
```

### `format_teks(template, **kwargs)`

Format a string with variables

```python
// Example
hasil itu format_teks(...)
```

---

## HTTP Functions

### `http_get(url, headers=None)`

Make an HTTP GET request

```python
// Example
hasil itu http_get(...)
```

### `http_post(url, data, headers=None)`

Make an HTTP POST request

```python
// Example
hasil itu http_post(...)
```

---


## Quick Reference

### Most Commonly Used Functions

```python
// String operations
huruf_besar("hello")  // "HELLO"
pisah("a,b,c", ",")  // ["a", "b", "c"]

// List operations
panjang([1, 2, 3])  // 3
urutkan([3, 1, 2])  // [1, 2, 3]

// Math operations
akar(16)  // 4.0
pangkat(2, 3)  // 8

// File operations
baca_file("data.txt")
tulis_file("output.txt", "content")
```

---

**Total: 118+ built-in functions available!**

For more examples, see the [examples](../examples/) directory.
