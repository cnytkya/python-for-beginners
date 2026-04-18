# senaryo: Bir robotunuz var ve ona her gün 10 adım yürümesini,durmasını ve selam vermesini söylüyorsunuz. Her seferinde bu 3 satırı tek tek mi yazmak istersiniz yoksa tekrar eden işe bir isim verip sadece ismini mi çağırırsınız?

# 1.gün
# print("10 adım yürü")
# print("Dur")
# print("Selam ver")

# # 2.gün
# print("10 adım yürü")
# print("Dur")
# print("Selam ver")

# # 3.gün
# print("10 adım yürü")
# print("Dur")
# print("Selam ver")

# bir fonksiyon tanımlarken def anahtar kelimesi(keyword) oluştururuz.

def sabah_rutini():
    print("10 adım yürü")
    print("Dur")
    print("Selam ver")

# print("----1.Gün------")
# sabah_rutini()
# print("----2.Gün------")
# sabah_rutini()
# print("----3.Gün------")
# sabah_rutini()

# 1'den 4'e kadar git (4 dahil değil) bir sayı dizisi oluştur.
for gun_sayisi in range(1,4): # bu diziyi oluşturmamın amacı 1.gün,2.gün ve 3.gün yazdırabilmek. liste = [1,2,3]
    print(f"-------{gun_sayisi}.Gün------")
    sabah_rutini()



