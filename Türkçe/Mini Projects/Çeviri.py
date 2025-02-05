# Kullanıcıdan giriş al
word = input("Bir kelime girin: ")

# Çeviri için boş bir string başlat
translation = ""

# Girilen kelimedeki her harfi döngüyle kontrol et
for letter in word:
    # Eğer harf bir sesli harfse (a, e, i, o, u)
    if letter.lower() in "aeiou":
        # Eğer harf büyükse, 'G' ile değiştir
        if letter.isupper():
            letter = "G"
            translation += letter
        # Eğer harf küçükse, 'g' ile değiştir
        else:
            letter = "g"
            translation += letter
    else:
        # Eğer sesli harf değilse, harfi olduğu gibi bırak
        translation += letter

# Çeviri sonucunu ekrana yazdır
print(translation)
