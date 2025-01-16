# Hesap Makinesi

def hesap_makinesi(ilk_kullanimi=True):
    # Hesap makinesi ilk kez kullanıldığında bir karşılama mesajı yazdırılır.
    if ilk_kullanimi:
        print("Hesap Makinesine Hoş Geldiniz")

    # Kullanıcıdan bir işlem seçmesi istenir.
    islem = input("Bir işlem seçin:\n"
                  "1. Toplama\n"
                  "2. Çıkarma\n"
                  "3. Çarpma\n"
                  "4. Bölme\n")

    # Kullanıcının seçimine göre işlem yapılır.
    if islem == "1":
        # Toplama
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        sonuc = sayi1 + sayi2
        print("Sonuç:", sonuc)

    elif islem == "2":
        # Çıkarma
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        sonuc = sayi1 - sayi2
        print("Sonuç:", sonuc)

    elif islem == "3":
        # Çarpma
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        sonuc = sayi1 * sayi2
        print("Sonuç:", sonuc)

    elif islem == "4":
        # Bölme
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        if sayi2 != 0:
            sonuc = sayi1 / sayi2
            print("Sonuç:", sonuc)
        else:
            print("Hata: Sıfıra bölme yapılamaz.")

    else:
        # Geçersiz işlem
        print("Geçersiz işlem. Lütfen tekrar deneyin.")

    # Kullanıcıya tekrar işlem yapıp yapmak istemediği sorulur.
    tekrar = input("Devam etmek istiyor musunuz? (e/h): ")
    if tekrar.lower() == "e":
        hesap_makinesi(ilk_kullanimi=False)
    else:
        print("Hoşçakalın")

# Hesap makinesini başlatıyoruz.
hesap_makinesi()
