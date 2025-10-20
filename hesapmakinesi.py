class HesapMakinesi:
    def toplama(self, a, b):
        return a + b

    def cikarma(self, a, b):
        return a - b

    def carpma(self, a, b):
        return a * b

    def bolme(self, a, b):
        if b == 0:
            return "Hata: Sıfıra bölme yapılamaz!"
        else:
            return a / b


# --- Kullanıcı Etkileşimi ---
hesap = HesapMakinesi()

print("=== Basit Hesap Makinesi ===")

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /): ")

if islem == "+":
    sonuc = hesap.toplama(sayi1, sayi2)
elif islem == "-":
    sonuc = hesap.cikarma(sayi1, sayi2)
elif islem == "*":
    sonuc = hesap.carpma(sayi1, sayi2)
elif islem == "/":
    sonuc = hesap.bolme(sayi1, sayi2)
else:
    sonuc = "Geçersiz işlem seçimi!"

print(f"Sonuç: {sonuc}")
