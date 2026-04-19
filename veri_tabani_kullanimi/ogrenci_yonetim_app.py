# öğrenci yönetim uygulaması: kayıtlar için sql lite kullanalım
import sqlite3

# 1.adım veritabanı oluştur
def veritabani_hazirla():
    # connect() komutu eğer yoksa 'okul.db' adında bir dosya oluştururur. 
    connection = sqlite3.connect("okul.db")

    imlec = connection.cursor() # veritabanı içerisindeki komutları tetikler.

    # execute() ile sql komutu gönder
    # eğer öğrenciler tablosu yoksa, isim ve numara sütunlarıyla table oluştur.
    imlec.execute("CREATE TABLE IF NOT EXISTS ogrenciler (isim TEXT, numara TEXT)")

    # commit() yapılan değişikliği (tablo oluşturma gibi) kalıcı hale getirilir
    connection.commit()
    connection.close() # iş bitince bağlantıyı kapat.
# CRUD => CREATE,READ,UPDATE,DELETE
# db ve table hazırsa o zaman table'a data ekleyebilelim.
def insert_student(ad,no): # create students: öğrenci ekleme
    connection = sqlite3.connect("okul.db")
    imlec = connection.cursor()

    imlec.execute("INSERT INTO ogrenciler VALUES (?, ?)", (ad,no))
    connection.commit()
    connection.close()
    print(f"{ad} veritabanına başarılı bir şekilde kadedildi.")
# ad = "Ahmet" # global değişken
def list_students(): #list student: öğrencileri listeleme. global func
    connection = sqlite3.connect("okul.db")

    imlec = connection.cursor()
    imlec.execute("SELECT * FROM ogrenciler")
    # veritabanından dataları çekerken bir listeye atarız
    students = imlec.fetchall()
    print("========== Kayıtlı Öğrenciler ======================")
    # eğer öğrenci yoksa ekranda "kayıtlı öğrenci bulunamadı" yazsın.
    if not students:
        print("kayıtlı öğrenci bulunamadı")
    # varsa da data listesini ekranda gösterelim.
    else:
        for student in students:
            print(f"İsim: {student[0]} | Numara: {student[1]}")
    connection.close()

def main(): # ana fonksiyon
    veritabani_hazirla() # program başlar başlamaz önce veritabanı ve tablo hazır mı diye kontrol ediyoruz.

    while True:
        #amacımız öğrenci eklereken sürekli sürekli programı çalıştırmamak. bir defa çalışsın, kullanıcı istediği sürece kayıt eklemesine olanaka verelim. eğer kullanıcı çıkmak isterse "q" tuşuna basarak döngüyü kırsın ve programı sonlandırsın.
        print("\n-----ÖĞRENCİ YÖENTİM PANELİ----")
        print("1 - Yeni Öğrenci Ekle")
        print("2 - Tüm Öğrencileri Listele")
        print("q - Çıkış Yap") # break komutu ile döngü sonlanır.
        # kullanıcıdan seçim alalım. yani choice
        choice = input("\nÖğrenci eklemek için 1\nÖğrencileri listelemek için 2\nÇıkış için 'q' tuşuna basınız\nSeçim Yapnız: ")
        if choice == "1":
            isim = input("Öğrenci Adı Soyadı: ")
            numara = input("Öğrenci Okul No: ")
            insert_student(isim,numara)
        # eğer seçim 2 ise öğrencileri listele.
        elif choice == "2":
            list_students()
        elif choice == "q":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Hatalı seçim!!! Lütfen 1,2 veya q giriniz.")

    
# programı başlatan tetikleyici
if __name__ == "__main__":
    main()
