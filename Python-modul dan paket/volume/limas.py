import math # import modul math untuk menghitung fungsi matematika

def volume_limas(alas, tinggi, jumlah_sisi): # definisi fungsi volume limas dengan parameter alas, tinggi, dan jumlah sisi
    # deklarasi rumus yang digunakan untuk menghitung luas alas dan volume
    luas_alas = (jumlah_sisi * alas * alas) / (4 * math.tan(math.pi / jumlah_sisi))
    volume = (1/3) * luas_alas * tinggi 
    return volume # return untuk mengasilkan output
