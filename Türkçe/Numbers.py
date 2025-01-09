# Sayılar (Numbers)
from math import *  # Matematik işlemleri için gerekli fonksiyonları içeren bir modül

# Doğrudan bir tam sayıyı ekrana yazdırabiliriz.
print(2)  # 2 çıktısı verir.

# Ondalık bir sayıyı da yazdırabiliriz.
print(2.01034)  # 2.01034 çıktısı verir.

# İşlem önceliğine göre matematiksel hesaplama yapılır.
print(3 - 4.5 * 2)  # Önce çarpma işlemi yapılır: 4.5 * 2 = 9. Sonra çıkarma: 3 - 9 = -6.
print((3 - 4.5) * 2)  # Parantez içi önce hesaplanır: 3 - 4.5 = -1.5. Sonra çarpma: -1.5 * 2 = -3.

# Kalanı (mod) hesaplamak için % operatörü kullanılır.
print(10 % 3)  # 10'u 3'e böldüğümüzde kalan 1'dir.

# Değişkenler ile matematiksel işlemler yapılabilir.
my_num = 4  # Bir tam sayı değişken
my_num2 = 2  # Başka bir tam sayı değişken
print(my_num + my_num2)  # 4 + 2 = 6 çıktısı verir.

# Sayıları string'e (metin) dönüştürerek başka bir metinle birleştirebiliriz.
print(str(my_num) + " benim favori sayım")  # str() olmadan hata alınır.

# Mutlak değer (absolute value) almak için abs() fonksiyonu kullanılır.
negative_num = -5  # Negatif bir sayı
print(abs(negative_num))  # Mutlak değer: |-5| = 5.

# Bir sayının üssünü almak için pow() fonksiyonu kullanılır.
num = 3
print(pow(num, 2))  # 3 üzeri 2 = 9.

# max() fonksiyonu, bir listedeki en büyük değeri bulur.
print(max(3, 2, 5, 7))  # En büyük sayı 7.

# min() fonksiyonu, bir listedeki en küçük değeri bulur.
print(min(3, 2, 5, 7))  # En küçük sayı 2.

# round() fonksiyonu, bir sayıyı en yakın tam sayıya yuvarlar.
print(round(3.86))  # 3.86'yı 4'e yuvarlar.

# floor() fonksiyonu, bir sayıyı aşağı yuvarlar.
print(floor(3.86))  # 3'e yuvarlar.

# ceil() fonksiyonu, bir sayıyı yukarı yuvarlar.
print(ceil(3.86))  # 4'e yuvarlar.

# sqrt() fonksiyonu, bir sayının karekökünü hesaplar.
print(sqrt(4))  # 4'ün karekökü 2'dir.
