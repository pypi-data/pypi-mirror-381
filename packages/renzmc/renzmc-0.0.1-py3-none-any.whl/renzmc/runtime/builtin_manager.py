"""
Built-in function manager for RenzmcLang

This module handles the setup and management of built-in functions.
"""

import renzmc.builtins as renzmc_builtins


class BuiltinManager:
    """
    Manages built-in functions for the interpreter
    """
    
    @staticmethod
    def setup_builtin_functions():
        """
        Setup and return built-in functions dictionary
        
        Returns:
            dict: Dictionary of built-in functions
        """
        builtin_functions = {
            # Basic functions
            'panjang': renzmc_builtins.panjang,
            'jenis': renzmc_builtins.jenis,
            'ke_teks': renzmc_builtins.ke_teks,
            'ke_angka': renzmc_builtins.ke_angka,
            
            # String functions
            'huruf_besar': renzmc_builtins.huruf_besar,
            'huruf_kecil': renzmc_builtins.huruf_kecil,
            'potong': renzmc_builtins.potong,
            'gabung': renzmc_builtins.gabung,
            'pisah': renzmc_builtins.pisah,
            'ganti': renzmc_builtins.ganti,
            'mulai_dengan': renzmc_builtins.mulai_dengan,
            'akhir_dengan': renzmc_builtins.akhir_dengan,
            'berisi': renzmc_builtins.berisi,
            'hapus_spasi': renzmc_builtins.hapus_spasi,
            
            # Math functions
            'bulat': renzmc_builtins.bulat,
            'desimal': renzmc_builtins.desimal,
            'akar': renzmc_builtins.akar,
            'pangkat': renzmc_builtins.pangkat,
            'absolut': renzmc_builtins.absolut,
            'pembulatan': renzmc_builtins.pembulatan,
            'pembulatan_atas': renzmc_builtins.pembulatan_atas,
            'pembulatan_bawah': renzmc_builtins.pembulatan_bawah,
            'sinus': renzmc_builtins.sinus,
            'cosinus': renzmc_builtins.cosinus,
            'tangen': renzmc_builtins.tangen,
            
            # List functions
            'tambah': renzmc_builtins.tambah,
            'hapus': renzmc_builtins.hapus,
            'hapus_pada': renzmc_builtins.hapus_pada,
            'masukkan': renzmc_builtins.masukkan,
            'urutkan': renzmc_builtins.urutkan,
            'balikkan': renzmc_builtins.balikkan,
            'hitung': renzmc_builtins.hitung,
            'indeks': renzmc_builtins.indeks,
            'extend': renzmc_builtins.extend,
            'gabung_daftar': renzmc_builtins.extend,
            'salin': renzmc_builtins.salin,
            'salin_dalam': renzmc_builtins.salin_dalam,
            'minimum': renzmc_builtins.minimum,
            'maksimum': renzmc_builtins.maksimum,
            'jumlah': renzmc_builtins.jumlah,
            'rata_rata': renzmc_builtins.rata_rata,
            
            # Iteration enhancement functions (Phase 2)
            'zip': renzmc_builtins.zip,
            'enumerate': renzmc_builtins.enumerate,
            'filter': renzmc_builtins.filter,
            'saring': renzmc_builtins.saring,
            'map': renzmc_builtins.map,
            'peta': renzmc_builtins.peta,
            'reduce': renzmc_builtins.reduce,
            'kurangi': renzmc_builtins.kurangi,
            'all': renzmc_builtins.all,
            'semua': renzmc_builtins.semua,
            'any': renzmc_builtins.any,
            'ada': renzmc_builtins.ada,
            'sorted': renzmc_builtins.sorted,
            'terurut': renzmc_builtins.terurut,
            
            # String validation functions (Phase 3)
            'is_alpha': renzmc_builtins.is_alpha,
            'adalah_huruf': renzmc_builtins.adalah_huruf,
            'is_digit': renzmc_builtins.is_digit,
            'adalah_angka': renzmc_builtins.adalah_angka,
            'is_alnum': renzmc_builtins.is_alnum,
            'adalah_alfanumerik': renzmc_builtins.adalah_alfanumerik,
            'is_lower': renzmc_builtins.is_lower,
            'adalah_huruf_kecil': renzmc_builtins.adalah_huruf_kecil,
            'is_upper': renzmc_builtins.is_upper,
            'adalah_huruf_besar': renzmc_builtins.adalah_huruf_besar,
            'is_space': renzmc_builtins.is_space,
            'adalah_spasi': renzmc_builtins.adalah_spasi,
            
            # File &amp; Path operations (Phase 4)
            'direktori_ada': renzmc_builtins.direktori_ada,
            'direktori_sekarang': renzmc_builtins.direktori_sekarang,
            'ubah_direktori': renzmc_builtins.ubah_direktori,
            'pisah_path': renzmc_builtins.pisah_path,
            'ekstensi_file': renzmc_builtins.ekstensi_file,
            'nama_file_tanpa_ekstensi': renzmc_builtins.nama_file_tanpa_ekstensi,
            'path_ada': renzmc_builtins.path_ada,
            'adalah_file': renzmc_builtins.adalah_file,
            'adalah_direktori': renzmc_builtins.adalah_direktori,
            'path_absolut': renzmc_builtins.path_absolut,
            'waktu_modifikasi_file': renzmc_builtins.waktu_modifikasi_file,
            'waktu_buat_file': renzmc_builtins.waktu_buat_file,
            'file_dapat_dibaca': renzmc_builtins.file_dapat_dibaca,
            'file_dapat_ditulis': renzmc_builtins.file_dapat_ditulis,
            
            # Statistics functions (Phase 6)
            'median': renzmc_builtins.median,
            'nilai_tengah': renzmc_builtins.nilai_tengah,
            'mode': renzmc_builtins.mode,
            'nilai_modus': renzmc_builtins.nilai_modus,
            'stdev': renzmc_builtins.stdev,
            'deviasi_standar': renzmc_builtins.deviasi_standar,
            'variance': renzmc_builtins.variance,
            'variansi': renzmc_builtins.variansi,
            'quantiles': renzmc_builtins.quantiles,
            'kuantil': renzmc_builtins.kuantil,
            
            # Dictionary functions
            'kunci': renzmc_builtins.kunci,
            'nilai': renzmc_builtins.nilai,
            'item': renzmc_builtins.item,
            'hapus_kunci': renzmc_builtins.hapus_kunci,
            
            # System functions
            'acak': renzmc_builtins.acak,
            'waktu': renzmc_builtins.waktu,
            'tidur': renzmc_builtins.tidur,
            'tanggal': renzmc_builtins.tanggal,
            'baca_file': renzmc_builtins.baca_file,
            'tulis_file': renzmc_builtins.tulis_file,
            'tambah_file': renzmc_builtins.tambah_file,
            'hapus_file': renzmc_builtins.hapus_file,
            'jalankan_perintah': renzmc_builtins.jalankan_perintah,
            'atur_sandbox': renzmc_builtins.atur_sandbox,
            'tambah_perintah_aman': renzmc_builtins.tambah_perintah_aman,
            'hapus_perintah_aman': renzmc_builtins.hapus_perintah_aman,
            
            # JSON and utility functions
            'json_ke_teks': renzmc_builtins.json_ke_teks,
            'teks_ke_json': renzmc_builtins.teks_ke_json,
            'gabung_path': renzmc_builtins.gabung_path,
            'file_exists': renzmc_builtins.file_exists,
            'buat_direktori': renzmc_builtins.buat_direktori,
            'daftar_direktori': renzmc_builtins.daftar_direktori,
            'hash_teks': renzmc_builtins.hash_teks,
            'buat_uuid': renzmc_builtins.buat_uuid,
            'url_encode': renzmc_builtins.url_encode,
            'url_decode': renzmc_builtins.url_decode,
            'base64_encode': renzmc_builtins.base64_encode,
            'base64_decode': renzmc_builtins.base64_decode,
            'regex_match': renzmc_builtins.regex_match,
            
            # HTTP functions
            'http_get': renzmc_builtins.http_get,
            'http_post': renzmc_builtins.http_post,
            'regex_replace': renzmc_builtins.regex_replace,
            'format_teks': renzmc_builtins.format_teks,
            
            # Class inheritance functions
            'super': renzmc_builtins.super,
        }
        
        return builtin_functions