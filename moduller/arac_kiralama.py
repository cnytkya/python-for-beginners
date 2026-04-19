# sunum tarafı. kullanıcıyla etkileşim giren(sunum) ana dosya.
import databse as db
import os

def console_ekrani_temizle():
    """console ekranını her işlemden sonra temizler"""
    os.system('cls' if os.name == 'nt' else 'clear')

def verileri_console_ekraninda_göster(veriler):
    """Verileri bir tablo formatında ekrana basar"""
    # başlıklar
    print(f"\n{'PLAKA':<15} | {'MARKA':<15} | {'MODEL':<15}")
    print("-"*50)

    # eğer veriler yoksa "Sistemde Kayıtlı Araç Bulunamadı" yazsın.
    if not veriler:
        print("Sistemde Kayıtlı Araç Bulunamadı")
    else:
        for item in veriler:
            print(f"{item[0]:<15} | {item[1]:<15} | {item[2]:<15}") # eğer [0],[1] vs şeklinde yapılmazsa veriler düzgün görünmez.
    print("-"*50)

def ana_menu():
    db.create_table()
    
    while True:
        print("\n================ARAÇ KİRALAMA YÖENTİM SİSTEMİ==========================")
        print("1. EKLE")
        print("2. LİSTELE")
        print("3. SİL")
        print("0. ÇIKIŞ")

        # kullanıcıdan bir seçim yapmasını isteyeceğiz
        secim = input("\nSeçim yapınız (0-3): ")
        if secim == "1":
            console_ekrani_temizle()
            print("---------YENİ ARAÇ KAYDI----------")
            plaka = input("Plaka giriniz: ")
            marka = input("Marka giriniz: ")
            model = input("Model giriniz: ")

            if db.create_oto(plaka,marka,model):
                print(f"{plaka.upper()} başarıyla sisteme dahil edildi.")
            else:
                print(f"\nHata: {plaka.upper()} zaten sistemde kayıtlı.")
            input("\nDevam etmek için enter tuşuna basın")
        elif secim == "2":
            console_ekrani_temizle()
            araclar = db.oto_list()
            verileri_console_ekraninda_göster(araclar)
            input("\nDevam etmek için enter tuşuna basın")
        elif secim == "3":
            console_ekrani_temizle()
            print("-----------ARAÇ SİL-------------")
            plaka = input("Silinecek aracın plakası: ")
            if db.delete_oto(plaka):
                print("Silindi")
            else:
                print("Araç bulunamadı")
            input("\nDevam etmek için enter tuşuna basın")
            
        elif secim == "0":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Yanlış seçim. 0-3 arası seim yapınız.")
            input("\nDevam etmek için enter tuşuna basın")
            
if __name__ == "__main__":
    ana_menu()
       


    