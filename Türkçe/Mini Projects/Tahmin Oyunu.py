def guessing_game():
    # Tahmin edilmesi gereken gizli kelime
    secret_word = "Messi"

    # Oyun sırasında verilen ipuçları
    hint = {
        1: "16 yaşından beri profesyonel olarak oynuyor.",
        2: "Thierry Henry ile oynadı.",
        3: "Şampiyonlar Ligi'ni kazandı.",
        4: "La Liga'yı kazandı.",
        5: "Tüm Zamanların En İyisi (GOAT)."
    }

    # Değişkenleri başlatma
    guess = ""  # Kullanıcının tahmini
    guess_count = 0  # Kullanıcının tahmin sayacı
    hint_word = "hint"  # İpucu istemek için anahtar kelime
    x = 0  # Verilen ipuçlarının sayısını takip eder
    hint_requested = False  # Kullanıcının ipucu isteyip istemediğini gösterir
    guesses_maxed = False  # Maksimum tahminlere ulaşıldığını gösterir

    # Ana oyun döngüsü
    while guess != secret_word and not guesses_maxed:
        if guess_count < 3:  # Sadece 3 tahmine izin verilir
            if hint_requested and x < 5:
                x += 1
                print(hint.get(x, "Daha fazla ipucu yok."))
                hint_requested = False

            # Kullanıcının tahminini al
            guess = input("Tahmin et (ipucu için 'hint' yaz): ").capitalize()

            if guess == secret_word:
                print("Oyuncuyu doğru tahmin ettiniz!")  # Doğru tahmin
                break
            elif guess.lower() == hint_word:
                if x < 5:
                    hint_requested = True  # İpucu istendiğini işaretle
                else:
                    print("Daha fazla ipucu yok.")  # Daha fazla ipucu verilemez
            else:
                print("Üzgünüm, bu doğru değil!")  # Yanlış tahmin
                guess_count += 1  # Tahmin sayacını artır
        else:
            print("Tahmin hakkınız bitti.")  # Maksimum tahminlere ulaşıldı
            guesses_maxed = True


# Oyunu başlat
guessing_game()
