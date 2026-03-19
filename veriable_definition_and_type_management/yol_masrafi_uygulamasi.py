# 1-Kullanıcıdan bir ayda çalışılan gün sayısını alın.
# 2-Günlük yol ücretini kullanıcıdan isteyin.
# 3-Aylık toplamı hesaplayın. bir ayda yolda harcadığı para ne kadar.

# Verileri kullanıcıdan alıyoruz
calisilan_gun = int(input("Bu ay kaç gün çalıştınız? "))
gunluk_ucret = float(input("Günlük yol ücretiniz ne kadar? (Örn: 45.5): "))

# aylık hesaplama
aylik_toplam = calisilan_gun * gunluk_ucret

# Çıktı
print("-" * 30)
print(f"AYLIK MASRAF RAPORU")
print(f"Toplam Gün: {calisilan_gun}")
print(f"Günlük Ücret: {gunluk_ucret} TL")
print(f"Toplam Yol Masrafı: {aylik_toplam} TL")
print("-" * 30)