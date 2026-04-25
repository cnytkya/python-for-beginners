import sqlite3 # py ile sql lite veritabanı arasında bağlantı kurmayı sağlayan kütüphane(lib)

def baglan(): # Veritabanı dosyasına erişim sağlamak için bir connection(bağlantı) nesnesi oluşturuyıoruz.
    return sqlite3.connect('db.sqlite3') # veritabanına bağlantı oluşturur.

def tablolari_olustur(): # Uygulamanın ilk açılışında gerekli olan tabloları (hastalar ve randevular) hazırlar.
    connect = baglan()
    cursor = connect.cursor()

    # hastalar tablosu: Kullanıcının bilgilerini ve uniq(benzersiz) TC numarasının saklandığı yer.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hastalar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tc_no TEXT UNIQUE NOT NULL,
            ad TEXT NOT NULL,
            soyad TEXT NOT NULL,
            telefon TEXT NOT NULL,
            dogum_tarihi TEXT
        )
    ''')
    # Randevular tablosu: Randevu kayıtlarını tutar. Kimin hangi randevuyu aldığı yazılır. Yani hasta tablosuyla ilişki(FOREIGN KEY) kurar.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS randevular (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hasta_id INTEGER NOT NULL,
            randevu_tarihi TEXT NOT NULL, -- YYYY-MM-DD
            randevu_saati TEXT NOT NULL, -- HH:MM
            doktor TEXT NOT NULL,
            aciklama TEXT,
            durum TEXT DEFAULT &#39;aktif&#39;, -- aktif, iptal, tamamlandı
            FOREIGN KEY (hasta_id) REFERENCES hastalar(id) ON DELETE CASCADE
        );
    """)
    connect.commit() # Yapılan değişiklikleri veritabanına yansıt.
    connect.close() # bellek yönetimi için bağlantıyı koparırır.




    