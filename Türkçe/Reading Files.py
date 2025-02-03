# 'r' okumak (read) anlamına gelir.
employee_file = open('employees.txt', 'r')

# Dosyanın okunabilir olup olmadığını kontrol et (boolean değer döndürür)
print(employee_file.readable())  # Çıktı: Okunabiliyorsa True, aksi halde False

# Dosyadan bir satır oku ve yazdır
print(employee_file.readline())  # İlk satırı okur

# readline() her çağrıldığında bir sonraki satıra geçer
print(employee_file.readline())  # İkinci satırı okur

# Eğer bir dosyayı açtıysak, mutlaka kapattığımızdan emin olmalıyız.
employee_file.close()

#### Belirli bir satırı okuma ####
employee_file = open('employees.txt', 'r')

# Tüm satırları bir liste olarak okur ve ikinci satırı yazdırır (indeks 1)
print(employee_file.readlines()[1])  # İkinci satırı ekrana yazdırır

employee_file.close()

#### Dosyanın tüm satırlarını döngü ile okuma ####
employee_file = open('employees.txt', 'r')

# Dosyadaki tüm satırları döngü içinde okuyarak yazdırma
for employee in employee_file.readlines():
    print(employee)

employee_file.close()
