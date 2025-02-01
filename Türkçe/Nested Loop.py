# 2D liste (iç içe liste)
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# İlk indeks satır indeksini, ikinci indeks sütun indeksini ifade eder.
print(numbers[0][2])  # 0. satır, 2. sütundaki elemanı yazdırır (Çıktı: 3)

# 2D listedeki her satırı döngü ile yazdırma
for row in numbers:
    print(row)  # Her satırı yazdırır

# İç içe döngü kullanarak 2D listedeki her elemana erişme
for row in numbers:
    for col in row:
        print(col)  # Matristeki her elemanı yazdırır
