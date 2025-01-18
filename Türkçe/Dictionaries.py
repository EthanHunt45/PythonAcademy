# Sözlükler (Dictionaries)

# İlk kısma anahtar (key) denir; benzersiz (unique) olmalıdır.
monthConversions = {
    "Jan": "Ocak",
    "Feb": "Şubat",
    "Mar": "Mart",
    "Apr": "Nisan",
    "May": "Mayıs",
    "Jun": "Haziran",
    # Sayıları da kullanabilirsiniz; tek kural benzersiz olmalarıdır.
      0  : "Temmuz",
      1  : "Ağustos",
    "Sep": "Eylül",
    "Oct": "Ekim",
    "Nov": "Kasım",
    "Dec": "Aralık"
}

# Anahtarlar (keys) kullanılarak sözlük değerlerine erişim
print(monthConversions["Jan"])  # Çıktı: Ocak
print(monthConversions["Feb"])  # Çıktı: Şubat

# get() metodu ile bir anahtara göre değer çağırma
print(monthConversions.get("Jan"))  # Çıktı: Ocak

# Eğer anahtar yoksa, varsayılan bir değer belirtebilirsiniz.
print(monthConversions.get("Max", 'Anahtar yok!'))  # Çıktı: Anahtar yok!
