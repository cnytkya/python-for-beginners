# Envanter Yönetim Sistemi Algoritması
# 1. Hazırlık Aşaması
# Adım 1: envanter isminde boş bir liste oluştur. (Bu liste içinde sözlükler tutacağız).

# Adım 2: Programın sürekli çalışması için bir Sonsuz Döngü başlat.

# 2. Menü Tasarımı (Döngü İçinde)
# Adım 3: Ekrana şu seçenekleri yazdır:

# Ürün Ekle

# Ürünleri Listele

# Stok Güncelle (Fiyat veya Adet)

# Ürün Sil

# Çıkış

# Adım 4: Kullanıcıdan secim değişkeni için bir girdi al.

# 3. Karar Yapıları (Seçim Kontrolü)
# EĞER seçim "1" ise (Ekleme):

# Kullanıcıdan "Ürün Adı", "Fiyat" ve "Stok Miktarı" bilgilerini al.

# Bu bilgileri bir Sözlük (Dictionary) yapısına dönüştür: {"ad": ..., "fiyat": ..., "stok": ...}

# Bu sözlüğü envanter listesine ekle.

# Ekrana "Ürün başarıyla eklendi!" mesajı ver.

# EĞER seçim "2" ise (Listeleme):

# Eğer liste boşsa "Henüz ürün yok" uyarısı ver.

# Değilse, listedeki her bir öğe için döngü kur ve ekrana; sıra numarası (index), adı, fiyatı ve stoğu yazdır.

# EĞER seçim "3" ise (Güncelleme):

# Kullanıcıya "Güncellemek istediğiniz ürünün sıra numarasını girin" de.

# Kullanıcının girdiği sıra numarası listede var mı kontrol et.

# Varsa: Kullanıcıdan yeni fiyatı al ve listedeki o öğenin "fiyat" değerini güncelle.

# Yoksa: "Geçersiz sıra numarası" mesajı ver.

# EĞER seçim "4" ise (Silme):

# Kullanıcıdan silmek istediği ürünün sıra numarasını al.

# Girilen index geçerliyse, o öğeyi listeden çıkart (pop veya del kullanabilirsin).

# Ekrana "Ürün silindi" onayı ver.

# EĞER seçim "5" ise (Çıkış):

# Ekrana "Sistemden çıkılıyor..." yazdır.

# break komutu ile döngüyü sonlandır.

# AKSİ TAKDİRDE (Geçersiz Seçim):

# "Lütfen 1-5 arasında bir rakam giriniz!" uyarısı ver.



# NOT: KAYITLARI JSON DOSYASINDA TUTALIM