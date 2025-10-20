import json
import os
from datetime import datetime

class YapilacaklarListesi:
    def __init__(self, dosya_yolu="gorevler.json"):
        self.dosya_yolu = dosya_yolu
        self.gorevler = []
        self._yukle()

    # ---------- Kalıcılık ----------
    def _yukle(self):
        if os.path.exists(self.dosya_yolu):
            try:
                with open(self.dosya_yolu, "r", encoding="utf-8") as f:
                    self.gorevler = json.load(f)
            except (json.JSONDecodeError, OSError):
                print("⚠️ Kayıt dosyası bozulmuş olabilir. Yeni dosya oluşturulacak.")
                self.gorevler = []
        else:
            self.gorevler = []

    def _kaydet(self):
        try:
            with open(self.dosya_yolu, "w", encoding="utf-8") as f:
                json.dump(self.gorevler, f, ensure_ascii=False, indent=2)
        except OSError:
            print("⚠️ Kayıt dosyasına yazılamadı!")

    # ---------- Temel İşlevler ----------
    def gorev_ekle(self, aciklama):
        aciklama = aciklama.strip()
        if not aciklama:
            print("⚠️ Boş görev eklenemez!")
            return
        yeni = {
            "aciklama": aciklama,
            "tamamlandi": False,
            "olusturma_zamani": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.gorevler.append(yeni)
        self._kaydet()
        print(f"✅ '{aciklama}' eklendi.")

    def gorev_sil(self, index):
        if 0 <= index < len(self.gorevler):
            silinen = self.gorevler.pop(index)
            self._kaydet()
            print(f"🗑️ '{silinen['aciklama']}' silindi.")
        else:
            print("⚠️ Geçersiz numara!")

    def gorevleri_listele(self):
        if not self.gorevler:
            print("📭 Henüz görev yok.")
            return
        print("\n--- YAPILACAKLAR ---")
        for i, g in enumerate(self.gorevler, start=1):
            durum = "✅" if g["tamamlandi"] else "⏳"
            print(f"{i}. {durum} {g['aciklama']}  (eklenme: {g['olusturma_zamani']})")

    # ---------- Bonus: Tamamlama/Geri Alma ----------
    def gorev_tamamla_degistir(self, index):
        if 0 <= index < len(self.gorevler):
            self.gorevler[index]["tamamlandi"] = not self.gorevler[index]["tamamlandi"]
            durum = "tamamlandı" if self.gorevler[index]["tamamlandi"] else "geri alındı"
            self._kaydet()
            print(f"🔁 '{self.gorevler[index]['aciklama']}' {durum}.")
        else:
            print("⚠️ Geçersiz numara!")


# ---------- Ana Menü ----------
def main():
    liste = YapilacaklarListesi()

    while True:
        print("\n=== YAPILACAKLAR LİSTESİ ===")
        print("1) Görev ekle")
        print("2) Görev sil")
        print("3) Görevleri listele")
        print("4) Görevi tamamla/geri al")
        print("5) Çıkış")

        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            gorev = input("Eklemek istediğiniz görev: ").strip()
            liste.gorev_ekle(gorev)

        elif secim == "2":
            if not liste.gorevler:
                print("Silinecek görev yok.")
            else:
                liste.gorevleri_listele()
                try:
                    idx = int(input("Silinecek görev numarası: ")) - 1
                    liste.gorev_sil(idx)
                except ValueError:
                    print("⚠️ Lütfen sayı girin.")

        elif secim == "3":
            liste.gorevleri_listele()

        elif secim == "4":
            if not liste.gorevler:
                print("Tamamlanacak görev yok.")
            else:
                liste.gorevleri_listele()
                try:
                    idx = int(input("Tamamla/Geri al numarası: ")) - 1
                    liste.gorev_tamamla_degistir(idx)
                except ValueError:
                    print("⚠️ Lütfen sayı girin.")

        elif secim == "5":
            print("👋 Görüşürüz!")
            break

        else:
            print("⚠️ Geçersiz seçim. 1-5 arası bir değer girin.")

if __name__ == "__main__":
    main()
