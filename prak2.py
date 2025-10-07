a = float(input("Masukkan angkan pertama:"))
b = float(input("Masukkan angkan kedua:"))
c = float(input("Masukkan angkan ketiga:"))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
elif c >= a and c >= b:
    largest = c
else:
    print("Tidak ada nilai Terbesar")

print("Angka terbesar adalah:", largest)