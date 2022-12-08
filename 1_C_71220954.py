def reverse (isi) :
    str = ""
    for setiap in isi :
        str = setiap + str
    return str

isi = str(input("Masukan Kata atau angka : "))

print(reverse(isi))