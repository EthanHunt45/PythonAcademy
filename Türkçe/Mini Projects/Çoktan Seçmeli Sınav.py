# 'Question' (Soru) adlı bir sınıf tanımlama
class Question:
    def __init__(self, question, answer):
        self.question = question  # Soru metnini saklar
        self.answer = answer  # Doğru cevabı saklar

# Matematik sorularının listesi
math_questions = [
    "2+2 kaç eder?\na-) 3\nb-) 4\nc-) 5",  # 1. soru
    "2*2 kaç eder?\na-) 3\nb-) 4\nc-) 5"   # 2. soru
]

# Question nesnelerinden oluşan bir sınav listesi oluşturma
exam = [
    Question(math_questions[0], "b"),  # İlk sorunun doğru cevabı: 'b'
    Question(math_questions[1], "b"),  # İkinci sorunun doğru cevabı: 'b'
]

# Sınavı çalıştıran fonksiyon
def run_exam():
    score = 0  # Başlangıç puanı
    for question in exam:
        # Kullanıcıdan soru için cevap alma
        answer = input(question.question + "\nCevabınız: ").lower()
        if answer == question.answer:  # Cevabın doğru olup olmadığını kontrol et
            score += 1  # Doğru cevap verilirse puanı artır
    print(f"Sonuç: {score}/{len(exam)}")  # Final puanını ekrana yazdır

# Sınavı başlat
run_exam()
