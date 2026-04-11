# ============================================================
# RESTORAN SİPARİŞ SİSTEMİ
# Konu: for döngüsü + if / elif / else
# Amaç: Python temelleri(değişkenler,sözlükler,döngüler,koşullar)
# ============================================================
# Yemek menüsü: {numara: (ad, fiyat)}
# Sözlük(Dictonary) yapısı kullanarak ürün kodlarını(Key) ve ürün bilgilerini(Value(değer)) tutuyoruz.
menu = {
    "1": ("Izgara Köfte",    85),
    "2": ("Tavuk Şiş",       75),
    "3": ("Vejetaryen Wrap", 60),
    "4": ("Lahmacun",        45),
    "5": ("Adana Kebap",     95),
}

# İçecek menüsü: {harf: (ad, fiyat)}
icecekler = { 
    "A": ("Su",        10), # index[0]
    "B": ("Ayran",     15), # index[1]
    "C": ("Kola",      20), # index[2]
    "D": ("Limonata",  25), # index[3]
}
# siparis_listesi = []

# adım 1: Programı başlat. kullanıcıyı ilk karşılayan görsel
print("╔══════════════════════════════════╗")
print("║  🍽️  RESTORAN SİPARİŞ SİSTEMİ     ║")
print("╚══════════════════════════════════╝")

masa_no = int(input("\nMasa Numaranız: "))
# kisi_sayi = int(input("Kişi sayısını giriniz: "))

# is_true = True
print("\n===ANA YEMEKLER===")
# 2. ADIM — YEMEK MENÜSÜNÜ GÖSTER
    # items() metodunu kullanarak sözlükteki anahtar(key) ve değerlere aynı anda erişiyoruz.
for numara, bilgi in menu.items():
    ad, fiyat = bilgi # Tuple yapısını parçalara ayırdık.
    print(f"[{numara}] {ad:<18} {fiyat:>3} TL")
while True:
    # 3. ADIM — YEMEK SEÇİMİ AL VE DOĞRULA
    secim = input("\nSeçiminiz (1-5)")
    # Seçilen kodun menüde olup olmadığını kontrol edelim.

    if secim in menu:
        yemek_adi = menu[secim][0]
        yemek_fiyat = menu[secim][1]
        print(f"✓ Setiniz: {yemek_adi}")
        break
    else:
        print("❌ Geçersiz seçim! Program sonlandırılıyor.")


print("=== İÇECEKLER ===")
for harf, bilgi in icecekler.items():
    ad, fiyat = bilgi
    print(f"[{ad}] {bilgi} {fiyat:>3} TL")

while True:
    # 5. ADIM — İÇECEK SEÇİMİ AL VE DOĞRULA
    secim_icecek = input("\nSeçiminiz(A-D)").upper()

    if secim_icecek in icecekler:
        icecek_adi = icecekler[secim_icecek][0]
        icecek_fiyat = icecekler[secim_icecek][1]
        print(f"✓ Setiniz: {icecek_adi}")
        break
    else:
        print("❌ Geçersiz seçim! Program sonlandırılıyor.")
    

# 6. ADIM — KİŞİ SAYISINI AL VE DOĞRULA
while True:
    kisi_sayisi = int(input("\nKaç kişisiniz? "))
    if 1 <= kisi_sayisi <= 10:
        break
    else:
        print("❌ Geçersiz kişi sayısı! (1-10 arası olmalı)")

# 7. ADIM — TUTARLARI HESAPLA

yemek_toplam  = yemek_fiyat  * kisi_sayisi
icecek_toplam = icecek_fiyat * kisi_sayisi
ara_toplam    = yemek_toplam + icecek_toplam
print(f"{ara_toplam}") # f-string: f"{}"

# 8. ADIM — İNDİRİM HESAPLA (İç İçe if/elif/else)
if kisi_sayisi > 5:
    # → indirim_oran = 0.20
    indirim_oran = 0.20
    # → indirim_mesaj = "Grup İndirimi (%20)"
    indirim_mesaj = "Grup indirimi (%20)"
elif ara_toplam > 500:
    # → indirim_oran = 0.15
    indirim_oran = 0.15
    # → indirim_mesaj = "500 TL Üzeri İndirimi (%15)"
    indirim_mesaj = "500 TL Üzeri İndirimi (%15)"
elif ara_toplam > 300:
    indirim_oran = 0.10
    indirim_mesaj = "300 TL Üzeri İndirimi (%10)"
else:
    indirim_oran = 0
    indirim_mesaj = "İndirim Yok"
indirim_tutari = ara_toplam * indirim_oran
# print(f"indirim tutarı: {indirim_tutari}")

# 9. ADIM — VIP MASA SERVİS ÜCRETİ
if masa_no > 10:
    servis_ucreti = ara_toplam * 0.10
    vip_mesaj = "(VIP)"
else:
    servis_ucreti = 0
    vip_mesaj = ""

genel_toplam = ara_toplam - indirim_tutari + servis_ucreti

# 10. ADIM — ÖDEME YÖNTEMİ SEÇ
print("\nÖdeme Yöntemi: 1-Nakit  2-Kart   3-Temassız")
secim_odeme = input("Seçiminiz: ")
if secim_odeme == "1":
    odeme = "Nakit"
elif secim_odeme == "2":
    odeme = "Kart"
elif secim_odeme == "3":
    odeme = "Temassız"
else:
    odeme = "Ödeme Yöntemi Belirtilmedi!"

# 11. ADIM — FİŞİ YAZDIR
print("╔══════════════════════════════════╗")
print("║            🧾 FİŞ                ║")
print("╚══════════════════════════════════╝")
print(f"Masa No: {masa_no}{vip_mesaj}")
print(f"Kişi sayısı: {kisi_sayisi}")
print("--- Sipariş ---")

# dor döngüsüyle sipariş kalemlerini yazdır.
siparisler = [
    (yemek_adi,   yemek_fiyat,   yemek_toplam),
    (icecek_adi,  icecek_fiyat,  icecek_toplam)
]
for ad, fiyat, toplam in siparisler:
    print(f"{ad:<14}: {fiyat:>4} TL x {kisi_sayisi} = {toplam:>5} TL")
print("-"*40)
print(f"{'Ara Toplam':<30} {ara_toplam:>6} TL")
if indirim_tutari > 0:
    print(f"{indirim_mesaj:<30} {-indirim_tutari:>6} TL")
if servis_ucreti > 0:
    print(f"{'VIP Servis Ücreti (%10)':<30} {servis_ucreti:+6} TL")
print("-"*40)
print(f"{'GENEL TOPLAM :':<30} {genel_toplam:>6} TL")
print("-"*40)
print(f"Ödeme        : {odeme}")
print("Afiyet olsun! 🍽️")

