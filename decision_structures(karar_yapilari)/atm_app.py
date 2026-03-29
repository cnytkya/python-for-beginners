# Algoritma:
# 1. Kullanıcıdan bakiye ve çekilecek miktarı al 
# 2. Eğer miktar 0'dan küçük veya eşitse → "Geçersiz miktar!" yaz 
# 3. Eğer miktar bakiyeden büyükse → "Yetersiz bakiye!" yaz 
# 4. Eğer miktar 1000'den büyükse → "Tek seferde max 1000 TL çekebilirsiniz." yaz 
# 5. Değilse → İşlemi gerçekleştir, kalan bakiyeyi yaz    

# Beklenen çıktı:
# Bakiye: 2500
# Çekilecek miktar: 750
# → İşlem başarılı! Kalan bakiye: 1750 TL

print("="*50)
print("     🏧 PARA ÇEKME UYGULAMASI")
print("="*50)

# 1. Kullanıcıdan bakiye ve çekilecek miktarı al 
bakiye = float(input("Bakiye: "))
miktar = float(input("Çekilecek Miktar: "))
print("="*50)

if miktar <= 0:# 2. Eğer miktar 0'dan küçük veya eşitse → "Geçersiz miktar!" yaz
    print("❌ Geçersiz miktar!")
elif miktar > bakiye:# 3. Eğer miktar bakiyeden büyükse → "Yetersiz bakiye!" yaz 
    print("❌ Yetersiz bakiye!")
elif miktar > 1000:# 4. Eğer miktar 1000'den büyükse → "Tek seferde max 1000 TL çekebilirsiniz." yaz 
    print("Tek seferde max 1000 TL çekebilirsiniz.")
else:# 5. Değilse → İşlemi gerçekleştir, kalan bakiyeyi yaz 
    bakiye = bakiye - miktar
    print(f"☑️ İşlem başarılı! Kalan bakiye: {bakiye:.0f} TL")
    
