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
    "A": ("Su",        10),
    "B": ("Ayran",     15),
    "C": ("Kola",      20),
    "D": ("Limonata",  25),
}

# adım 1: Programı başlat. kullanıcıyı ilk karşılayan görsel
print("╔══════════════════════════════════╗")
print("║  🍽️  RESTORAN SİPARİŞ SİSTEMİ     ║")
print("╚══════════════════════════════════╝")

masa_no = int(input("\nMasa Numaranız: "))

# 2. ADIM — YEMEK MENÜSÜNÜ GÖSTER
print("\n===ANA YEMEKLER===")
# items() metodunu kullanarak sözlükteki anahtar(key) ve değerlere aynı anda erişiyoruz.
for numara, bilgi in menu.items():
    ad, fiyat = bilgi # Tuple yapısını parçalara ayırdık.
    print(f"[{numara}] {ad:<18} {fiyat:>3} TL")

# 3. ADIM — YEMEK SEÇİMİ AL VE DOĞRULA
secim_yemek = input("\nSeçiminiz (1-5): ")
# Seçilen kodun menüde olup olmadığını kontrol edelim.
if secim_yemek in menu:
    yemek_adi = menu[secim_yemek][0] # 0. index isim
    yemek_fiyat = menu[secim_yemek][1] # 1. index fiyat
    print(f"✓ Seçtiniz: {yemek_adi}")
else:
    print("❌ Geçersiz seçim! Program sonlandırılıyor.")
    exit()

print("=== İÇECEKLER ===")
for harf, bilgi in icecekler.items():
    ad, fiyat = bilgi
    print(f"[{harf}] {ad:<18} {fiyat:>3} TL")

# 5. ADIM — İÇECEK SEÇİMİ AL VE DOĞRULA
secim_icecek = input("\nSeçiminiz(A-D): ")
if secim_icecek in icecekler:
    icecek_adi = icecekler[secim_icecek][0] # 0. index isim
    icecek_fiyat = icecekler[secim_icecek][1] # 1. index fiyat
    print(f"✓ Seçtiniz: {icecek_adi}")
else:
    print("❌ Geçersiz seçim! Program sonlandırılıyor.")
    exit()

# 6. ADIM — KİŞİ SAYISINI AL VE DOĞRULA
kisi_sayisi = int(input("\nKaç kişisiniz? "))
if kisi_sayisi <1 or kisi_sayisi >10:
    print("❌ Geçersiz kişi sayısı! (1-10 arası olmalı)")
    exit()

# 7. ADIM — TUTARLARI HESAPLA
yemek_toplam  = yemek_fiyat  * kisi_sayisi
icecek_toplam = icecek_fiyat * kisi_sayisi
ara_toplam    = yemek_toplam + icecek_toplam
# print(f"{ara_toplam}") # f-string: f"{}"

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
print(f"indirim tutarı: {indirim_tutari}")


