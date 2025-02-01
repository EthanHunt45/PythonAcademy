# Bir string içinde döngü kullanımı
for letter in "Python":
    print(letter)  # "Python" kelimesindeki her harfi yazdırır

# Arkadaş listesi
friends = ["Erinc", "Bahar", "Defne", "Berke", "Bahar", "Yaren"]
# 'friend' değişkenine istediğimiz ismi verebiliriz, örneğin: isim, kelime...
for friend in friends:
    print(friend)  # Listedeki her arkadaşın ismini yazdırır

# Bir listeyi indeks kullanarak döngü ile gezme
for index in range(len(friends)):
    if friends[index] == "Erinc":
        print("O Erinc.")  # Eğer isim "Erinc" ise özel mesaj yazdırır
    else:
        print("Erinc değil")  # Diğer isimler için bu mesaj yazdırılır

# Belirtilen aralıkta döngü (10 dahil değil)
for index in range(10):
    print(index)  # 0'dan 9'a kadar olan sayıları yazdırır

# Belirtilen aralıkta döngü (3 dahil, 10 dahil değil)
for index in range(3, 10):
    print(index)  # 3'ten 9'a kadar olan sayıları yazdırır

# Üs alma işlemi yapan fonksiyon
def exponent_function():
    result = 1
    base_num = int(input("Taban sayıyı girin: "))  # Kullanıcıdan taban sayıyı alır
    pow_num = int(input("Üs sayısını girin: "))  # Kullanıcıdan üs sayısını alır
    for i in range(pow_num):
        result = float(result * base_num)  # Taban sayıyı üs kadar çarpar
    return result  # Sonucu döndürür

# Fonksiyonu çağır ve sonucu ekrana yazdır
print(exponent_function())
