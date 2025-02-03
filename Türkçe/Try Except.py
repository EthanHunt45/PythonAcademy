# Her durumu kapsayacak şekilde istisnaları (exception) ele almalıyız.
try:
    # Bu işlem ZeroDivisionError (sıfıra bölme hatası) oluşturacaktır
    value = 10 / 0

    # Kullanıcıdan giriş al ve tamsayıya çevir
    number = int(input("Bir sayı girin: "))

    # Girilen sayıyı ekrana yazdır
    print(number)

# Sıfıra bölme hatasını yakalama
except ZeroDivisionError as err:
    print(err)  # Hata mesajını ekrana yazdırır

# Geçersiz giriş hatasını yakalama (Eğer kullanıcı sayısal olmayan bir değer girerse)
except ValueError:
    print("Geçersiz giriş")  # Geçersiz giriş için hata mesajı yazdırır
