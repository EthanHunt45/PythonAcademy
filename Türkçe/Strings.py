# Strings

name = 'Beşiktaş'
print(name)

# .upper() fonksiyonu, bir string içindeki tüm harfleri büyük harfe çevirir.
name = name.upper()
print(name)
# .isupper() ve .islower() fonksiyonları, string içindeki karakterlerin
# tamamen büyük harf ya da tamamen küçük harf olup olmadığını kontrol eder. Boolean (True/False) değer döner.
print('Şimdi tüm harfler büyük mü? Doğru mu Yanlış mı? --> ' + str(name.isupper()))
print('Şimdi tüm harfler küçük mü? Doğru mu Yanlış mı? --> ' + str(name.islower()))

# .lower() fonksiyonu, bir string içindeki tüm harfleri küçük harfe çevirir.
name = name.lower()
print(name)
print('Şimdi tüm harfler büyük mü? Doğru mu Yanlış mı? --> ' + str(name.isupper()))
print('Şimdi tüm harfler küçük mü? Doğru mu Yanlış mı? --> ' + str(name.islower()))

# len() fonksiyonu, bir string'in uzunluğunu hesaplar.
# Boşluklar ve özel karakterler de bu hesaba dahildir.
name = 'Python öğreniyorum'
print(len(name))  # Boşlukları da hesaba kattığı için toplam uzunluk 20'dir (17 harf ve 3 boşluk).

# Index, bir karakterin string içerisindeki konumunu ifade eder. Index 0'dan başlar.
job = 'Bilgisayar Mühendisi'
# [] içerisine yazılan sayı, string'deki indexi belirtir. İlk karakter her zaman 0. indexte bulunur.
print(job[4])
# .index() fonksiyonu, bir string içerisinde belirtilen harfin ya da kelimenin başlangıç indexini döner.
print(job.index('r'))  # 'r' harfinin bulunduğu ilk index döner.
print(job.index('Mühendisi'))  # 'Mühendisi' kelimesinin başladığı index döner.

# .replace() fonksiyonu, string içindeki bir harfi, bir grup harfi ya da kelimeyi değiştirmek için kullanılır.
job = 'Bilgisayar Mühendisi'
job = job.replace('Bilgisayar Mühendisi', 'Çiftçi')
print(job)
