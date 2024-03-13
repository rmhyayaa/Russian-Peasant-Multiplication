def russianPeasantMultiplication(a,b):
    total = 0
    while a > 0:
        if a % 2 == 1:
            total += b
        a //= 2 #bagi nilai pertama dengan 2
        b *= 2 #gandakan nilai kedua
    return total

#fungsi utama
def main():
    #meminta pengguna memasukkan dua bilangan
    a =  int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua:"))

    #memanggil fungsi russianPeasantMultiplication dan mencetak hasil
    result = russianPeasantMultiplication(a, b)
    print("Hasil perkalian dari", a, "dan", b, "adalah: ", result )
if __name__ == "__main__":
    main()