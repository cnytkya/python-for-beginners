import json # json dosyaları üzerinde çalışırken kurmamız gereken kütüphane
import os # os kütüphanesi dosya okuma,oluşturma ve silme işlemleri yapar.
# import openpyxl

# amaç: bir kayıt eklenirken o kaydın bir json dosyasında tutulması. eğer json dosyası varsa kaydı oluştursun,eğer yoksa da önce json dosyasını oluştursun sonra kaydı oluştursun.

# dosya işlemleri yaparken "w"(write) ve "r"(read) modu var. "w" modu dosya oluşturur, "r" modu ise dosyayı okur.

# istenilen path içerisinde dosyanın oluşması için path tanımla
dosya_yolu = "loops(dögüler)/ogrenciler.json"
def veriyi_yukle(): # bu metot belirtilen path(konum)'te dosya var mı? varsa yükler.
    """dosya varsa veriyi okur, yoksa boş liste döner"""
    if os.path.exists(dosya_yolu):
        with open(dosya_yolu,"r",encoding = "utf-8") as dosya:
            return json.load(dosya)
    return []


def veriyi_kaydet(ogrenciler):
    """listeyi JSON formatında dosyaya yazar."""
    klasor_yolu = os.path.dirname(dosya_yolu)
    if not os.path.exists(klasor_yolu):
        os.makedirs(klasor_yolu)
    with open(dosya_yolu, "w",encoding = "utf-8") as dosya:
        json.dump(ogrenciler, dosya, ensure_ascii=False, indent=4)



ogrenciler = veriyi_yukle()
# ana program
while True:
    print("=====Öğrenci Yönetim Uygulaması=====")
    print("-"*50)
    print("1.Ekle")
    print("2.Listele")
    print("3.Güncelle")
    print("4.Sil")
    print("5.Öğrenci Başarı Ortalaması")
    print("0.Çıkış Yap")
    
    secim = int(input("Bir seçim yapınız (0-5): "))
    if secim == 0:
        print("Çıkış yapılıyor...")
        break
    #kayıt ekle
    elif secim == 1:
        ad_soyad = input("Öğrenci adı soyadı giriniz: ")
        no = input("Öğrenci no giriniz: ")
        notu = float(input("Öğrenci not ortalaması giriniz: "))

        yeni_ogrenci = {"no":no,"ad_soyad":ad_soyad,"not":notu}
        ogrenciler.append(yeni_ogrenci)
        veriyi_kaydet(ogrenciler) # savchanges => eklenen datayı dosyada uygula. değişiklikleri uygulayan yer burası
        print(f"{ad_soyad} başarılıyla eklendi")