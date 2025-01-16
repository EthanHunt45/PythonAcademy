# If Statements

# Bu degiskenler bir kisinin erkek ve/veya uzun olup olmadigini temsil ediyor.
is_Male = False
is_Tall = False

# Duruma bagli olarak farkli ciktilar ureten bir dizi kosul kullaniyoruz.
if is_Male and is_Tall:
    print("Uzun bir erkeksiniz!")  # Eger her iki kosul da dogruysa.

elif is_Male or is_Tall:
    print("Ya erkeksiniz ya da uzunsunuz!")  # En az bir kosul dogruysa.

elif is_Male and not is_Tall:
    print("Kisa bir erkeksiniz!")  # Erkek ama uzun degilse.

elif not is_Male and is_Tall:
    print("Uzun bir kadinsiniz!")  # Erkek degil ama uzunsa.

else:
    print("None!")  # Hicbir kosul dogru degilse.

# Bu fonksiyon kullanicidan alinan üç sayi arasinda en büyük degeri bulur.
def find_max():
    # Üç sayi girdi olarak alinir ve bir listeye kaydedilir.
    numbers = [float(input("Birinci sayiyi giriniz: ")), float(input("Ikinci sayiyi giriniz: ")), int(input("Ücüncü sayiyi giriniz: "))]

    # Sayilar karsilastirilarak en büyük olan bulunur.
    if numbers[0] >= numbers[1] and numbers[0] >= numbers[2]:
        return numbers[0]  # Birinci sayi en büyükse.
    elif numbers[1] >= numbers[0] and numbers[1] >= numbers[2]:
        return numbers[1]  # Ikinci sayi en büyükse.
    elif numbers[2] >= numbers[1] and numbers[2] >= numbers[0]:
        return numbers[2]  # Ücüncü sayi en büyükse.
    else:
        return 'Null'  # Gecerli bir sonuc yoksa.

# Fonksiyonu çağiriyoruz ve sonucunu yazdırıyoruz.
print(find_max())
