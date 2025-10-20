from decimal import Decimal, InvalidOperation, getcontext

getcontext().prec = 28  # Para hesaplarında güvenli hassasiyet

class BankaHesabi:
    def __init__(self, hesap_no: str, bakiye: Decimal = Decimal("0.00")):
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self, miktar: Decimal):
        if miktar <= 0:
            print("Geçersiz miktar! Pozitif bir tutar girin.")
            return
        self.bakiye += miktar
        print(f"{miktar:.2f} TL yatırıldı. Yeni bakiye: {self.bakiye:.2f} TL")

    def para_cek(self, miktar: Decimal):
        if miktar <= 0:
            print("Geçersiz miktar! Pozitif bir tutar girin.")
            return
        if miktar > self.bakiye:
            print("Yetersiz bakiye! İşlem iptal edildi.")
            return
        self.bakiye -= miktar
        print(f"{miktar:.2f} TL çekildi. Kalan bakiye: {self.bakiye:.2f} TL")

    def hesap_bilgileri(self):
        print("\n=== Hesap Bilgileri ===")
        print(f"Hesap No : {self.hesap_no}")
        print(f"Bakiye   : {self.bakiye:.2f} TL")

def tutar_oku(istek: str) -> Decimal:
    """
    Kullanıcıdan tutar okur. '12,50' veya '12.50' kabul eder.
    Hatalı girişte tekrar sorar.
    """
    while True:
        s = input(istek).strip().replace(" ", "")
        s = s.replace(",", ".")  # Virgülü noktaya çevir
        try:
            val = Decimal(s)
            # 2 ondalığa yuvarla
            return val.quantize(Decimal("0.01"))
        except (InvalidOperation, ValueError):
            print("Geçersiz tutar! Örnek: 100,00 ya da 100.00")

# --- Program akışı ---
print("=== Mini Banka Sistemi ===")
hesap_no = input("Hesap numarası girin: ").strip()
ilk_bakiye = tutar_oku("Başlangıç bakiyesi (örn: 0,00): ")

hesap = BankaHesabi(hesap_no, ilk_bakiye)
hesap.hesap_bilgileri()

while True:
    print("\n--- MENÜ ---")
    print("1) Para yatır")
    print("2) Para çek")
    print("3) Hesap bilgileri")
    print("4) Çıkış")
    secim = input("Seçiminiz: ").strip()

    if secim == "1":
        miktar = tutar_oku("Yatırılacak tutar: ")
        hesap.para_yatir(miktar)

    elif secim == "2":
        miktar = tutar_oku("Çekilecek tutar: ")
        hesap.para_cek(miktar)

    elif secim == "3":
        hesap.hesap_bilgileri()

    elif secim == "4":
        print("Güle güle! Program sonlandırılıyor.")
        break

    else:
        print("Geçersiz seçim. 1-4 arası bir değer girin.")
