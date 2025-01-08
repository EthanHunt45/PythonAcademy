# Veri Tipleri ve Değişkenler (Data Types and Variables)

# String türündeki değişkenler çift tırnak (" ") içerisinde tutulur.
# Number (sayı) türündeki değişkenlerde ise tırnağa gerek yoktur.
character_name = "Erinç"
character_age = 21
print(character_name)
print(character_age)

# Burada değişkenler güncelleniyor. Yani, bir değişkenin değerini sonradan değiştirebiliriz.
character_name = "Messi"
character_age = 38

# + işareti, print fonksiyonunda stringleri birleştirmek (concatenate) için kullanılır.
# character_age bir sayı (number) olduğu için, str() fonksiyonu ile string'e dönüştürülmesi gerekir.
print("Name is " + character_name + " and " + str(character_age) + " years old.")

# Alternatif olarak f-string kullanılabilir.
print(f"Name is {character_name} and {character_age} years old.")

# Sayılar ondalık (decimal) biçimde de tanımlanabilir.
character_age = 18.01
print(character_age)

# Python'da 3 temel veri türü (data type) vardır:
# Number (Sayı)
number = 1
# String (Metin)
string = "Hello"
# Boolean (Mantıksal Değer)
is_True = True

# \n, yeni bir satır oluşturmak için kullanılır.
print('Erinç \nkodlama öğreniyor')

# \' ifadesi, string içinde tek tırnağı kaçış karakteri olarak kullanmamızı sağlar.
print('Erinç \'kodlama\' öğreniyor')
