import math # import modul math untuk menghitung fungsi matematika

def volume_prisma(alas, tinggi, jumlah_sisi): # definisi fungsi volume prisma dengan parameteralas, tinggi, dan jumlah sisi
    # deklarasi rumus luas alas dan volume
    luas_alas = (jumlah_sisi * (alas ** 2)) / (4 * math.tan(math.pi / jumlah_sisi))
    volume = luas_alas * tinggi
    return volume # return untuk mengasilkan output
