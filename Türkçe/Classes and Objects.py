# 'Person' adlı bir sınıf tanımlama
class Person:
    def __init__(self, name, age):
        # Nitelikleri başlatma
        self.name = name
        self.age = age

    # Kişinin yaşlı olup olmadığını kontrol eden metot
    def is_old(self):
        if self.age <= 65:
            return False
        else:
            return True

# 'Person' sınıfından bir nesne oluşturma
person1 = Person("John", 25)
print(person1.name)  # Kişinin ismini yazdırır
print(person1.age)   # Kişinin yaşını yazdırır
print(person1.is_old())  # Kişinin yaşlı olup olmadığını kontrol eder (False)

person2 = Person("Karen", 70)
print(person2.name)  # Kişinin ismini yazdırır
print(person2.age)   # Kişinin yaşını yazdırır
print(person2.is_old())  # Kişinin yaşlı olup olmadığını kontrol eder (True)

# 'Person' sınıfından türetilmiş 'Student' (Öğrenci) adlı alt sınıf
class Student(Person):
    def __init__(self, name, age, major, gpa):
        super().__init__(name, age)  # Üst sınıfın yapıcı metodunu çağırır
        self.major = major  # 'major' (bölüm) niteliğini başlatır
        self.gpa = gpa  # 'gpa' (not ortalaması) niteliğini başlatır

    # Öğrencinin onur listesinde olup olmadığını kontrol eden metot
    def is_on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

# 'Student' sınıfından bir nesne oluşturma
student = Student("Erinc", 21, "Bilgisayar Mühendisliği", 3.5)
print(student.name)  # Öğrencinin ismini yazdırır
print(student.age)   # Öğrencinin yaşını yazdırır
print(student.major) # Öğrencinin bölümünü yazdırır
print(student.gpa)   # Öğrencinin not ortalamasını yazdırır
print(student.is_old())  # Öğrencinin yaşlı olup olmadığını kontrol eder (False)
print(student.is_on_honor_roll())  # Öğrencinin onur listesinde olup olmadığını kontrol eder (True)
