# kullanıcıdan bilgileri alalım. öğrenci adını,vize ve final notlarını alın.

# ortalama hesapla (%40 vize,%60 final):

# harf notu belirleme(if/elif/else) AA(Pekiyi)/BA(iyi)/BB(orta)/CB(geçer)/CC(zayıf geçer)/FF(başarısız).

# öğrencinin kaldı / geçti durumu.

# sonuçları ekrana yazdır.

print("="*50)
print("Not Hesaplama Programı")
print("="*50)
ad=input("Lütfen adınızı giriniz: ")
vize=float(input("Lütfen vize notunuzu giriniz: "))
final=float(input("Lütfen final notunuzu giriniz: "))
ort = (vize * 0.4) + ( final *0.60)
if ort >= 90 and ort<=100:
    harf = "AA"
    durum = "Pekiyi"
    # print(f"Vize: {vize}\nFinal: {final}\nOrtalama: {ort}\nHarf Notu: {harf}\nDurum: {durum}")
elif ort >= 80 and ort<90:
    harf = "BA"
    durum = "iyi"
elif ort >= 70 and ort<80:
    harf = "BB"
    durum = "Orta"
elif ort >= 60 and ort<70:
    harf = "CB"
    durum = "Geçer"
elif ort >= 50 and ort<60:
    harf = "CC"
    durum = "Zayıf geçer"
elif ort<50:
    harf = "FF"
    durum = "Başarısız"
else:
    harf="Doğru sonuç için 0-100 arasında değerler giriniz"
    durum = "Başarısız"
#kaldı-geçti durumu
if ort >= 50 and ort<=100:
    gecti_mi = "GEÇTİ"
else:
    gecti_mi = "Kaldı"
# sonuçları ekrana yazdır.
print("\n" + "="*50)
print(f"Adı: {ad.upper()}\n" + "="*50)
print(f"Vize: {vize}")
print(f"Final: {final}")
print(f"Ortalama: {ort}")
print(f"Harf: {harf}")
print(f"Durum: {durum}")
print(f"Sonuç: {gecti_mi}")
print("="*50)
