print("\nKonversi Temperatur Sederhana")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

def temp():
    pilih = input("Konversi apa yang ingin kamu lakukan?\n[C -> F]\n[C -> K]\n[F -> C]\n[F -> K]\n[K -> C]\n[K -> F]\n")
    if pilih == "C -> F":
        num1 = input("Masukan Temperatur Celcius untuk di konversikan ke Fahrenheit\n")
        print(f'Hasil Konversi {int(num1)} Celsius ke Fahrenheit adalah: {int(num1) * 1.8 + 32} Fahrenheit.')
    elif pilih == "C -> K":
        num1 = input("Masukan Temperatur Celcius untuk di konversikan ke Kelvin\n")
        print(f'Hasil Konversi {int(num1)} Celsius ke Kelvin adalah: {int(num1) + 273.15} Kelvin.')
    elif pilih == "F -> C":
        num1 = input("Masukan Temperatur Fahrenheit untuk di konversikan ke Celsius\n")
        print(f'Hasil Konversi {int(num1)} Fahrenheit ke Celcius adalah: {(int(num1) - 32) * 5/9} Celcius.')
    elif pilih == "F -> K":
        num1 = input("Masukan Temperatur Fahrenheit untuk di konversikan ke Kelvin\n")
        print(f'Hasil Konversi {int(num1)} Fahrenheit ke Kelvin adalah: {(int(num1) - 32) * 5/9 + 273.15} Kelvin.')
    elif pilih == "K -> C":
        num1 = input("Masukan Temperatur Kelvin untuk di konversikan ke Celcius\n")
        print(f'Hasil Konversi {int(num1)} Kelvin ke Celsius adalah: {int(num1) - 273.15} Celsius.')
    elif pilih == "K -> F":
        num1 = input("Masukan Temperatur Kelvin untuk di konversikan ke Fahrenheit\n")
        print(f'Hasil Konversi {int(num1)} Kelvin ke Fahrenheit adalah: {(int(num1) - 273.15) * 1.8 + 32} Fahrenheit.')