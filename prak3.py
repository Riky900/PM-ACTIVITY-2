n = int(("Masukkan nilai n untuk batas deret Fibonnaci"))

a, b = 0, 1

print("Deret Fibonnaci hingga", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b