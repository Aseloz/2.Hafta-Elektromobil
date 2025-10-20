class Kisi:
    def __init__(self, ad, soyad, yas, meslek):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.meslek = meslek

    def bilgileri_goster(self):
        print(f"Ad: {self.ad}, Soyad: {self.soyad}, Yaş: {self.yas}, Meslek: {self.meslek}")


kisiler = []

while True:
    print("\n=== KİŞİ BİLGİLERİ YÖNETİM SİSTEMİ ===")
    print("1. Yeni kişi ekle")
    print("2. Kişileri listele")
    print("3. Kişi sil")
    print("4. Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        yas = input("Yaş: ")
        meslek = input("Meslek: ")

        yeni_kisi = Kisi(ad, soyad, yas, meslek)
        kisiler.append(yeni_kisi)
        print(f"{ad} {soyad} başarıyla eklendi.")

    elif secim == "2":
        if len(kisiler) == 0:
            print("Henüz kayıtlı kişi yok.")
        else:
            print("\n--- Kayıtlı Kişiler ---")
            for i, kisi in enumerate(kisiler, start=1):
                print(f"{i}. ", end="")
                kisi.bilgileri_goster()

    elif secim == "3":
        if len(kisiler) == 0:
            print("Silinecek kişi yok.")
        else:
            for i, kisi in enumerate(kisiler, start=1):
                print(f"{i}. {kisi.ad} {kisi.soyad}")
            sil_index = int(input("Silmek istediğiniz kişinin numarasını girin: ")) - 1

            if 0 <= sil_index < len(kisiler):
                silinen = kisiler.pop(sil_index)
                print(f"{silinen.ad} {silinen.soyad} silindi.")
            else:
                print("Geçersiz numara!")

    elif secim == "4":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
