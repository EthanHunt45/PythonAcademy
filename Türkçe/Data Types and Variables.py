# Veri Tipleri ve Değişkenler (Data Types and Variables)

# String türündeki değişkenler çift tırnak (" ") veya tek tırnak (' ') içinde tanımlanır.
# Sayı (Number) türündeki değişkenlerde tırnağa gerek yoktur.
character_name = "Erinç"  # String türünde bir değişken
character_age = 21  # Sayı (tam sayı) türünde bir değişken
print(character_name)  # Değişkeni ekrana yazdırır: Erinç
print(character_age)  # Değişkeni ekrana yazdırır: 21

# Değişkenler sonradan yeni bir değer alabilir.
character_name = "Messi"  # Değişkenin yeni değeri: Messi
character_age = 38  # Değişkenin yeni değeri: 38

# + operatörü string birleştirmek (concatenate) için kullanılır.
# Ancak sayılar string'e dönüştürülmeden birleştirilemez.
# str() fonksiyonu ile bir sayıyı string'e dönüştürüyoruz.
print("Name is " + character_name + " and " + str(character_age) + " years old.")
# Çıktı: Name is Messi and 38 years old.

# f-string, string birleştirme için daha kolay ve okunabilir bir yöntemdir.
# Süslü parantez ({}) içinde değişken isimlerini kullanarak birleştirme yapılır.
print(f"Name is {character_name} and {character_age} years old.")
# Çıktı: Name is Messi and 38 years old.

# Sayılar ondalık (float) türünde de tanımlanabilir.
character_age = 18.01  # Ondalık sayı türünde bir değişken
print(character_age)  # Çıktı: 18.01

# Python'da 3 temel veri türü (data type) vardır:
# 1. Sayı (Number): Tam sayılar (int) veya ondalık sayılar (float)
number = 1  # Tam sayı
# 2. Metin (String): Karakterlerden oluşan bir veri türü
string = "Hello"  # String türünde bir veri
# 3. Mantıksal Değer (Boolean): True (Doğru) veya False (Yanlış)
is_True = True  # Boolean türünde bir veri

# \n, yeni bir satır eklemek için kullanılır.
print('Erinç \nkodlama öğreniyor')
# Çıktı:
# Erinç
# kodlama öğreniyor

# \' ifadesi, string içinde tek tırnak kullanmak için kaçış karakteridir.
print('Erinç \'kodlama\' öğreniyor')
# Çıktı: Erinç 'kodlama' öğreniyor
