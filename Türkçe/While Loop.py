# While Döngüsü

# Bir değişken başlatma
i = 1
numbers = []

# Koşul doğru olduğu sürece devam eden bir while döngüsü
while i <= 10:
    # i'nin mevcut değerini listeye ekle
    numbers.append(i)
    # i'yi 2 artır
    i = i + 2

# Ortaya çıkan listeyi yazdır
print(numbers)

# Değişkenleri başlatma
x = 10
numbers1 = []  # 10'a tam bölünebilen sayılar için liste
numbers2 = []  # 10'a tam bölünemeyen sayılar için liste

# x 100'den küçük veya eşit olduğu sürece devam eden bir while döngüsü
while x <= 100:
    # x'in 10'a bölünüp bölünmediğini kontrol et
    if x % 10 == 0:
        # 10'a bölünebiliyorsa x'i numbers1'e ekle
        numbers1.append(x)
        x = x + 2
    else:
        # 10'a bölünemiyorsa x'i numbers2'ye ekle
        numbers2.append(x)
        x = x + 2

# Listeleri yazdır
print(numbers1)  # 10'a tam bölünebilen sayıların listesi
print(numbers2)  # 10'a tam bölünemeyen sayıların listesi
