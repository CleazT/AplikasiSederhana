print("Aplikasi Sederhana CleazT\n")

def pilih():
    pilihan = input("\nPilihlah apa yang ingin anda hitung! [Kalkulator, Temperatur, Konversi Mata Uang]\n")
    if pilihan == "Kalkulator":
        from m_kalkulator import main
        main.perhitungan()

        lagi = input("\nApakah kamu ingin mengulanginya lagi? [ya/tidak]\n")
        if lagi == "ya":
            return pilih()
        else:
            print("Baiklah terimakasih!\n by: CleazT")

    elif pilihan == "Temperatur":
        from m_temperatur import main
        main.temp()

        lagi = input("\nApakah kamu ingin mengulanginya lagi? [ya/tidak]\n")
        if lagi == "ya":
            return pilih()
        else:
            print("Baiklah terimakasih!\n by: CleazT")

    elif pilihan == "Konversi Mata Uang":
        from m_uang import main
        main.konv()

        lagi = input("\nApakah kamu ingin mengulanginya lagi? [ya/tidak]\n")
        if lagi == "ya":
            return pilih()
        else:
            print("Baiklah terimakasih!\n by: CleazT")
        
    else: print(f'\nPilihan "{pilihan}" tidak exist')
pilih()