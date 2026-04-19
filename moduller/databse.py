# mutfak kısmı. yani veritabanı işlemlerini gerçekleştirecek katman.
# restoranın deposu = veritabanı
# depo_adı = hes_res_depo, veritabanı ismi de =>DB_NAME = "arac_kiralama.db"
import sqlite3 as sql #sqlite3 için takma isim => as sql
import os

moduler_dizin = os.path.dirname(os.path.abspath(__file__))

database_name = os.path.join(moduler_dizin, "arac_kirlama.db")
def db_connection():
    """Merkezi """
    return sql.connect(database_name)

def create_table(): # Tabo oluştururken veritabanına query(sorgu) atıyoruz. tablo ismi ve tablo özellikleri(property) il oluşturulur.
    with db_connection() as baglanti:
        imlec = baglanti.cursor()
        imlec.execute("""
            CREATE TABLE IF NOT EXISTS araclar(
                plaka TEXT PRIMARY KEY,
                marka TEXT,
                model TEXT
            )
        """)
        baglanti.commit() # oluşturulan veritabanı tablosuyla birlikte yeni haliyle kaydeder.
        print("Tablo oluşturuldu.")
    
def create_oto(plaka,marka,model):# araç ekleme
    """Veritabanına yeni bir araç ekler. eğer plaka çakışması varsa False dönsün"""
    try: # sorun yoksa bu kod bloğu çalışır.
        with db_connection() as baglanti:
            imlec = baglanti.cursor()
            imlec.execute("INSERT INTO araclar VALUES (?, ?, ?)",
                          (plaka.upper(), marka.capitalize(), model.capitalize()))
            baglanti.commit()
            return True
    except sql.IntegrityError: # eğer hata varsa(execption) bu kod bloğu çalışır.
        return False
def oto_list(): #araç listeleme
    with db_connection() as baglanti:
        imlec = baglanti.cursor()
        imlec.execute("SELECT * FROM araclar")
        return imlec.fetchall()

def delete_oto(plaka):
    with db_connection() as c:
        imlec = c.cursor()
        imlec.execute("DELETE FROM araclar WHERE plaka = ?", (plaka.upper(),))
        c.commit()
        return imlec.rowcount > 0

# def soft_delete(): # veritabanından tamamen silmez.