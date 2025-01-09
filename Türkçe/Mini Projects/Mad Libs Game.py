# Mad Libs Oyunu

# Mad Libs, kelime türlerine dayalı boşluk doldurma oyunudur.
# Bir hikâye şablonu hazırlanır ve bu şablonda bazı kelimeler boş bırakılır.
# Oyuncudan belirli türde kelimeler (örneğin sıfat, isim, fiil) istenir.
# Bu kelimeler hikâyedeki boşluklara yerleştirilir.
# Ortaya çıkan hikâye genellikle komik ve eğlenceli olur.
# Bu oyun, hem eğlenmek hem de Python öğrenirken temel becerileri geliştirmek için harikadır!

# Oyuna hoş geldiniz mesajı
print("Mad Libs Oyununa Hoş Geldiniz!")
print("Komik bir hikâye oluşturmak için sizden bazı kelimeler isteyeceğiz.\n")

# Kullanıcıdan girdiler alıyoruz
day = input("Haftanın en sevdiğiniz günü nedir? ")
day = day.capitalize()
age = input("Yaşınız: ")
name = input("İsminiz: ")
food = input("En sevdiğiniz yemek: ")
place = input("Sevdiğiniz bir yer: ")
animal = input("En sevdiğiniz hayvan: ")
verb = input("Bir fiil (eylem): ")
adjective = input("Bir sıfat: ")

# Hikâye şablonu
story = f"""
Bir zamanlar {adjective} bir {day} günü, {age} yaşında {name} adında biri çok aç uyanmış.
{name}, kahvaltıda {food} yemeye karar vermiş ama hiç kalmadığını fark etmiş!
Bunun üzerine {name} çantasını toplayıp {place} gitmiş.
Yolda, {animal} bir hayvanın {verb} yapmaya çalıştığını görmüş. Bu şimdiye kadar gördüğü en komik şeymiş!
{name} o kadar çok gülmüş ki etraftaki herkes gülmeye başlamış.
Ve işte böylece {name}'in {day} günü en {adjective} gün olmuş!
"""

# Hikâyeyi yazdır
print("\nİşte sizin Mad Libs hikâyeniz:\n")
print(story)
