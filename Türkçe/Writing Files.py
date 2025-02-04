# 'a' (append) modu, dosyada var olan içeriği silmeden yeni veri ekler.
employee_file = open("employees.txt", "a")

# Dosyaya yeni bir çalışan kaydı ekleme
new_employee = employee_file.write("\nBahar - Bilgisayar Mühendisi")

# Yazma işlemi bittikten sonra dosyayı kapatma
employee_file.close()

# 'w' (write) modu, dosyayı tamamen sıfırlar ve baştan yazar.
employee_file = open("employees.txt", "w")

# Yeni çalışan kaydı yazma (önceki içerik tamamen silinir)
new_employees = employee_file.write("\nBahar - Bilgisayar Mühendisi")

# Dosyayı kapatma
employee_file.close()
