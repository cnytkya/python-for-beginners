# ürün yönetim uygulaması
# konu: CRUD işlemleri -> Create,Read,Update,Delete

envanter = [
    {"ad": "Laptop","fiyat":45000,"stok":10},
    {"ad": "Mouse","fiyat":2500,"stok":50}
]

print("🍎Ürün Yönetim Uygulaması")

while True:
    print("\n" + "-"*40)
    print("               📁ANA MENÜ")
    print("-"*40)
    print("1-➕ Ürün Ekle")
    print("2-📊 Ürün Listele")
    print("3-🖊️ Ürün Düzenle")
    print("4-⚔️ Ürün Sil")
    print("5-⭐ Envanter Özeti")
    print("0-❌ Çıkış Yap")

    choice = int(input("Yapmak istediğiniz işlem (0-5): "))

    if choice == 0: #true
        print("\nSistemden çıkış yapılıyor... İyi çalışmalar!")
        break
    elif choice == 1: #ekleme mantığı: Create
        ad = input("Ürün Adı: ")
        fiyat = float(input("Ürün fiyatını giriniz: "))
        stok = int(input("Stok adedi: "))

        yeni_urun = {"ad":ad,"fiyat":fiyat,"stok":stok}
        envanter.append(yeni_urun) # envanter'e yeni ürünü ekle.
        print(f"👌 {ad} başarıyla envantere eklendir.")
    elif choice == 2: # listele mmantığı: Read
        print(f"\n{'ID':<5} {'Ürün Adı':<10} {'Ürün Fiyatı':<15} {'Stok':<15}")
        print("-"*40)
        for index, urun in enumerate(envanter):
            print(f"\n{index:<5} {urun['ad']:<10} {urun['fiyat']:<15} {urun['stok']:<15}")
    elif choice == 3:
        #kullanıcıdan güncellenecek ürün ID
        id_no = int(input("Güncellenecek ürün ID: "))
        # ID no 0 ve listeenin aralağında bir sayı mı?
        if 0 <= id_no < len(envanter):
            yeni_fiyat = float(input(f"{envanter[id_no]['ad']} için yeni fiyat gir: "))# yeni_fiyat alınacak
            envanter[id_no]['fiyat'] = yeni_fiyat # yeni_fiyat eski fiyat ile değişecek
            print(f"👌 {ad} başarıyla güncellendi.")# güncellendi mesajı
        else:
            # geçersiz değer ise Geçersiz ID yazsın
            print("❌ Ürün bulunamadı!")
    elif choice == 4:
        # silinecek ürün ID
        id_no = int(input("Silinecek ürün ID: "))
        if 0 <= id_no < len(envanter):
            silinen = envanter.pop(id_no)
            print(f"👌 {silinen['ad']} başarıyla silindi.")
        else:
            # geçersiz değer ise Geçersiz ID yazsın
            print("❌ Ürün bulunamadı!")
    elif choice == 5:
        # özet rapor
        toplam_urun = len(envanter)
        toplam_maliyet = sum(urun['fiyat'] * urun['stok'] for urun in envanter)
        print("\n---ENVANTER ÖZETİ----")
        print(f"Toplam çeşit: {toplam_urun}")
        print(f"Toplam En vanter Değeri: {toplam_maliyet:.2f} TL")
    else:
        print("❌ Lütfen 0-5 arasında geçerli bir değer giriniz!")
            
        


