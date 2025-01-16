# Fonksiyonlar (Functions)

# Bu basit bir fonksiyon tanımı. 'say_hello' adındaki fonksiyon "Hello World" yazdırıyor.
def say_hello():
    print("Hello World")  # Ekrana "Hello World" yazdırır.

# Fonksiyonu çağırıyoruz.
say_hello()

# Bu fonksiyon kullanıcıdan isim ve yaş bilgisi alıyor.
def say_hi():
    # Kullanıcıdan isim bilgisi alınıyor.
    name = input("Adınız nedir?")

    # Kullanıcıdan yaş bilgisi alınıyor ve integer olarak kaydediliyor.
    age = int(input("Kaç yaşındasınız?"))

    # Kullanıcıya adı ve yaşıyla ilgili bir mesaj yazdırılıyor.
    print("Merhaba, " + name + "! " + str(age) + " yaşındasın.")

# Fonksiyonu çağırıyoruz.
say_hi()

# Bu fonksiyon, dışarıdan iki parametre alıyor: isim ve yaş.
def say_hi2(name, age):
    # Gelen parametrelerle bir mesaj yazdırılıyor.
    print("Merhaba, " + name + "! " + str(age) + " yaşındasın.")

# Fonksiyonu çağırıyoruz ve gerekli parametreleri sağlıyoruz.
say_hi2("John", 12)

# Bu fonksiyon, verilen bir sayının küpünü hesaplar.
def cube(number):
    # Sayının küpü hesaplanıyor ve bir değişkene kaydediliyor.
    cube = number * number * number

    # Hesaplanan değer geri dönülüyor.
    return cube

# Fonksiyonu çağırıyoruz ve sonucunu yazdırıyoruz.
print(cube(5))  # 5'in küpü olan 125 ekrana yazdırılır.