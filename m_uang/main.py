print("\nKonversi Mata Uang")
print("=-=-=-=-=-=-=-=-=-=-=-=-=\n")

def konv():
    pilih = input("Pilih Konversi [USD -> IDR, IDR -> USD]\n")
    if pilih == "USD -> IDR":
        num1 = input("Masukan Jumlah Uang Dollar:\n")
        print(f'{int(num1)} USD di konversikan menjadi IDR adalah Rp {round(int(num1) * 15580, 2)},00\n')
    elif pilih == "IDR -> USD":
        num1 = input("Masukan Jumlah Uang Rupiah:\n")
        print(f'{int(num1)} IDR di konversikan menjadi USD adalah {round(int(num1) / 15580, 2)}$\n')
    else:
        print("Pilihan yang anda input tidak exist.")