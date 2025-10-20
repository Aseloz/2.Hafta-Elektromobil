import random

class SayiTahminOyunu:
    def __init__(self):
        # Oyun başlarken rastgele bir sayı üret
        self.gizli_sayi = random.randint(1, 100)
        self.deneme_sayisi = 0

    def oyunu_baslat(self):
        print("=== Sayı Tahmin Oyunu ===")
        print("1 ile 100 arasında bir sayı tuttum, bakalım tahmin edebilecek misin?")

        while True:
            try:
                tahmin = int(input("Tahminini gir: "))
            except ValueError:
                print("Lütfen sadece sayı gir!")
                continue

            self.deneme_sayisi += 1

            if tahmin < self.gizli_sayi:
                print("Daha büyük bir sayı dene!")
            elif tahmin > self.gizli_sayi:
                print("Daha küçük bir sayı dene!")
            else:
                print(f"Tebrikler 🎉 {self.deneme_sayisi} denemede doğru bildin!")
                break


# --- Oyunu Başlat ---
oyun = SayiTahminOyunu()
oyun.oyunu_baslat()
