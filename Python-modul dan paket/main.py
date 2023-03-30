#lakukan import dulu untuk memendefinisikan setiap modul yang
#berisi fungsi dari perhitungan luas dan volume
from luas.lingkaran import *
from luas.jajargenjang import *
from luas.persegi import *
from luas.persegipanjang import *
from luas.segitiga import *
from luas.trapesium import *
from volume.kubus import *
from volume.balok import *
from volume.kerucut import *
from volume.tabung import *
from volume.limas import *
from volume.prisma import *


def main (): # mendefinisikan bahwa terdapat sebuah fungsi dengan judul main
        while True: # pernyataan lopping yang digunakan untun mengulang saat program sudah selesai menghitung
            print('=== PROGRAM PERHITUNGAN 2D dan 3D ===') # menampilkan judul program
            print('[1] 2D') #opsi 1
            print('[2] 3D') #opsi 2
            print('[3] Keluar') #opsi 3
            print('=====================================') #garis pemisah
            print("\n")

            pilihan = int(input("Mau menghitung luas (1) atau volume (2)? ")) # inputan untuk menghitung opsi berapa

            if pilihan == 1:
                # Pilihan bangun 2D
                print("Pilih bangun 2D:")
                print("1. Jajargenjang")
                print("2. Lingkaran")
                print("3. Persegi")
                print("4. Persegi panjang")
                print("5. Segitiga")
                print("6. Trapesium")
            # Minta input dari pengguna untuk memilih luas 2D atau volume 3D
                bangun_datar = input("Mau menghitung apa? ")
                # Minta input dari pengguna untuk ukuran bangun datar
                if bangun_datar == "1":
                    alas = float(input("Masukkan panjang alas: "))
                    tinggi = float(input("Masukkan tinggi: "))
                    print("Luas jajargenjang adalah:", luas_jajargenjang(alas, tinggi))
                    print("\n")
                elif bangun_datar == "2":
                    jari_jari = float(input("Masukkan jari-jari: "))
                    print("Luas lingkaran adalah:", luas_lingkaran(jari_jari))
                    print("\n")
                elif bangun_datar == "3":
                    sisi = float(input("Masukkan panjang sisi: "))
                    print("Luas persegi adalah:", luas_persegi(sisi))
                    print("\n")
                elif bangun_datar == "4":
                    panjang = float(input("Masukkan panjang: "))
                    lebar = float(input("Masukkan lebar: "))
                    print("Luas persegi panjang adalah:", luas_persegi_panjang(panjang, lebar))
                    print("\n")
                elif bangun_datar == "5":
                    alas = float(input("Masukkan alas: "))
                    tinggi = float(input("Masukkan tinggi: "))
                    print("Luas segitiga adalah:", luas_segitiga(alas, tinggi))
                    print("\n")
                elif bangun_datar == "6":
                    sisi_a = float(input("Masukkan panjang sisi a: "))
                    sisi_b = float(input("Masukkan panjang sisi b: "))
                    tinggi = float(input("Masukkan tinggi: "))
                    print("Luas trapesium adalah:", luas_trapesium(sisi_a, sisi_b, tinggi))
                    print("\n")
                else:
                    print("Bangun datar tidak valid")

            elif pilihan == 2:
                # Pilihan bangun 3D
                print("Pilih bangun 3D:")
                print("1. Balok")
                print("2. Kerucut")
                print("3. Kubus")
                print("4. Limas")
                print("5. Prisma")
                print("6. Tabung")
                bangun_ruang = input("Masukkan pilihan bangun ruang: ")

                # Minta input dari pengguna untuk ukuran bangun ruang
                if bangun_ruang == "1":
                    panjang = float(input("Masukkan panjang: "))
                    lebar = float(input("Masukkan lebar: "))
                    tinggi = float(input("Masukkan tinggi: "))
                    print("Volume balok adalah:", volume_balok(panjang, lebar, tinggi))
                    print("\n")
                elif bangun_ruang == "2":
                    jari_jari = float(input("Masukkan jari-jari: "))
                    tinggi = float(input("Masukkan tinggi: "))
                    print("Volume kerucut adalah:", volume_kerucut(jari_jari, tinggi))
                    print("\n")
                elif bangun_ruang == "3":
                    sisi = float(input("Masukkan panjang sisi: "))
                    print("Volume kubus adalah:", volume_kubus(sisi))
                    print("\n")
                elif bangun_ruang == "4":
                    alas = float(input("Masukkan panjang alas: "))
                    tinggi = float(input("Masukkan tinggi: "))
                    jumlah_sisi = int(input("Masukkan jumlah sisi pada alas: "))
                    print("Volume limas adalah:", volume_limas(alas, tinggi, jumlah_sisi))
                    print("\n")
                elif bangun_ruang == "5":
                    alas = float(input("Masukkan panjang alas: "))
                    tinggi = float(input("Masukkan tinggi: "))
                    jumlah_sisi = int(input("Masukkan jumlah sisi pada alas: "))
                    print("Volume prisma adalah:", volume_prisma(alas, tinggi, jumlah_sisi))
                    print("\n")
                elif bangun_ruang == "6":
                    jari_jari = float(input("Masukkan jari-jari: "))
                    tinggi = float(input("Masukkan tinggi: "))
                    print("Volume tabung adalah:", volume_tabung(jari_jari, tinggi))
                    print("\n")
                else:
                    print("Bangun ruang tidak valid")
            elif pilihan == 3:
                    exit("Terimakasih")
                    print("\n")
            else:
                    print("Pilihan tidak valid. Pilih 2D atau 3D.")
main() # memanggil fungsi main untuk dijalankan 
