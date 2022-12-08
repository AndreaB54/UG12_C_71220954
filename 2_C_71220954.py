angka = str(input("Masukkan angka : "))
hitung = str(input("Masukkan angka yg dihitung : "))

def jumlah():
    nomor = " "
    for hitung in angka :
        nomor = angka.count(hitung)
    return nomor

print("Angka", hitung, "muncul sebanyak", jumlah(), "kali")