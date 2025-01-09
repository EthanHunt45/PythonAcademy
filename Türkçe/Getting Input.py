#Getting Inputs

# Kullanıcıdan adını alır ve selamlar.
name = input("Adınızı girin: ")  # input() kullanıcıdan veri almak için kullanılır.
print("Merhaba, " + name + "!")  # Kullanıcının adını ekrana yazdırır.

# Kullanıcıdan yaşını alır ve bu bilgiyi ekrana yazdırır.
age = int(input("Yaşınızı girin: "))  # input() ile alınan değer string olarak gelir, bunu int'e çeviriyoruz.
print("Sen " + str(age) + " yaşındasın.")  # Sayıyı string'e dönüştürerek birleştirme yapıyoruz.

# Basit bir hesap makinesi: İki sayıyı toplar.
num1 = int(input("Birinci sayıyı girin: "))  # İlk tam sayıyı kullanıcıdan alır.
num2 = int(input("İkinci sayıyı girin: "))  # İkinci tam sayıyı kullanıcıdan alır.
toplam = num1 + num2  # İki sayıyı toplar.
print("Toplamınız: " + str(toplam))  # Toplamı ekrana yazdırır.

# Yukarıdaki hesap makinesi sadece tam sayılarla çalışıyor.
# Ondalıklı sayıları (float) da desteklemesi için int yerine float kullanabiliriz.

num1 = float(input("Birinci sayıyı girin: "))  # İlk ondalık sayıyı kullanıcıdan alır.
num2 = float(input("İkinci sayıyı girin: "))  # İkinci ondalık sayıyı kullanıcıdan alır.
toplam = num1 + num2  # İki ondalık sayıyı toplar.
print("Toplamınız: " + str(toplam))  # Toplamı ekrana yazdırır.
