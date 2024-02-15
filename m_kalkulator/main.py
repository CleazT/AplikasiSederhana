print("\nKalkulator Sederhana")
print("=-=-=-=-=-=-=-=-=-=-=-=-=\n")

num1 = input("Masukan angka pertama: \n")
num2 = input("Masukan angka kedua: \n")

operator = input("Masukan operator [+, -, *, /]\n")
def perhitungan():
    if operator == "+":
        print(f"Hasil perhitungan {num1} {operator} {num2} adalah = ", int(num1) + int(num2))
    elif operator == "-":
        print(f"Hasil perhitungan {num1} {operator} {num2} adalah = ", int(num1) - int(num2))
    elif operator == "*":
        print(f"Hasil perhitungan {num1} {operator} {num2} adalah = ", int(num1) * int(num2))
    elif operator == "/":
        print(f"Hasil perhitungan {num1} {operator} {num2} adalah = ", int(num1) / int(num2))
    else:
        print("Nomor atau operator yang anda input tidak terdefinisikan!")