# P1_Komnum_A1![Grafik](https://user-images.githubusercontent.com/90591077/198323546-1519589a-701e-40f8-9a0c-f5ae72ecdc59.jpg)

Kelompok 1 Komputasi Numerik-A Anggota : Wardatul Amalia Safitri ((5025211006)), Sekar Ambar Arum (5025211041), Nadya Zuhria Amana (5025211058), Dilla Wahdana (5025211060), Altriska Izzati Khairunnisa H (5025211187)

Misal dijamin bahwa f(x) adalah fungsi kontinyu pada interval [a, b] dan f(a)f(b) < 0. Ini artinya bahwa f(x) paling tidak harus memiliki akar pada interval [a, b]. Kemudian definisikan titik tengah pada interval [a, b] yaitu c = a+b /2 . Dari sini kita memperoleh dua subinterval yaitu [a, c] dan [c, b]. Setelah itu, cek apakah f(a)f(c) < 0 atau f(b)f(c) < 0 ? Jika f(a)f(c) < 0 maka b = c (artinya titik b digantikan oleh titik c yang berfungsi sebagai titik b pada iterasi berikutnya), jika tidak maka a = c. Dari iterasi pertama kita memperoleh interval [a, b] yang baru dan titik tengah c yang baru. Kemudian lakukan pengecekan lagi seperti sebelumnya sampai memperoleh error yang cukup kecil.
