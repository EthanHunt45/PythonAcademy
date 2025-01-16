# Lists and Tuples

# Burada bir arkadas listesi olusturdum. Bu liste, arkadaslarimin isimlerini tutuyor.
friends = ["Erinç", "Bahar", "Defne", "Berke", "Bahar", "Yaren"]

# Bir liste farkli turde verileri icerebiliyor: bir string, bir boolean ve bir integer.
List = ["Name", True, 2]

# Sadece sayilardan olusan bir liste de olusturabiliriz.
numbers = [3, 2, 1]

# Listeden belirli bir elemani yazdiriyorum. Bu durumda indeks 1'i secip "Bahar"'i yazdiriyor.
print(friends[1])

# Listenin son elemanini yazdiriyorum. Negatif indeks kullanarak bunu yapabilirim.
print(friends[-1])

# Listenin belirli bir araligini yazdiriyorum. Indeks 1'den 3'e kadar olan elemanlari secip yazdiriyor (3 dahil degil).
print(friends[1 : 3])

# Listenin icinde "Bahar"'in bulundugu ilk konumun indeksini buluyorum.
print(friends.index("Bahar"))

# Listenin icinde "Bahar"'in kac kez gectigini sayiyorum.
print(friends.count("Bahar"))

# Listeyi alfabetik olarak siraliyorum.
friends.sort()
print(friends)

# Listeyi ters ceviriyorum.
friends.reverse()
print(friends)

# Listeyi kopyaliyorum ve yeni bir liste olusturuyorum.
friends2 = friends.copy()
print(friends2)

# Listenin belirli bir elemanini degistiriyorum. Indeks 0'daki elemani "Erinç" olarak degistiriyorum.
friends[0] = "Erinç"
print(friends[0])

# Bir listenin sonuna baska bir liste ekliyorum.
friends.extend(numbers)
print(friends)

# "best_players" adinda yeni bir liste olusturuyorum ve bu listeye eleman ekliyorum.
best_players = ["Messi", "Ronaldo"]
best_players.append("Neymar")
print(best_players)

# Listenin belirli bir konumuna eleman ekliyorum. "Quaresma" en basa ekleniyor.
best_players.insert(0, "Quaresma")
print(best_players)

# Listeden bir elemani cikariyorum. Bu durumda "Ronaldo"yu cikariyorum.
best_players.remove("Ronaldo")
print(best_players)

# Listenin son elemanini kaldiriyorum.
best_players.pop()
print(best_players)

# Tüm listeyi bosaltiyorum.
best_players.clear()
print(best_players)

# Burada sabit bir veri yapisi olan bir demet (tuple) olusturuyorum.
coordinates = (3, 4)

# Demetten belirli bir elemani yazdiriyorum. Indeks 1'deki elemani seciyorum.
print(coordinates[1])