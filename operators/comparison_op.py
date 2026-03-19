# karşılaştırma operatörleri
"""
    ==	Equal(eşit mi)	x == y	
    !=	Not equal(eşit değil mi? )	x != y	
    >	Greater than(büyük mü)	x > y	
    <	Less than(küçük mü)	x < y	
    >=	Greater than or equal to(büyük eşit mi)	x >= y	
    <=	Less than or equal to(küçük eşit mi)	x <= y

    k.o'leri programlamada karar verme mekanizmalrın temelidir. py'da bu op'leri kullandığımızda bilgisayara bir soru sormuş oluruz ve o da "evet(true)" veya "hayır(false)" cevabını verir.
"""
print("-"*10,"== Equal(eşit mi) örneği","-"*10)
sifre = "1234"
girilen_sifre = "1234"
print(sifre == girilen_sifre) # True

sifre = 1234
girilen_sifre = "1234"
print(sifre == girilen_sifre) # False: çünkü sifre int tipinde girilen_sifre ise str tipinde

print("-"*10,"!= Not equal(eşit değil mi? )","-"*10)
user_role = "admin"
print(user_role != "misafir") # True
sayi = 10
print(sayi != 10) # False

print("-"*10,">	Greater than(büyük mü)","-"*10)
yas = 20
print(yas > 25) # False

print("-"*10,"<	Less than(küçük mü)","-"*10)
sepet_tutari = 150
limit = 200
print(sepet_tutari < limit) # True

#sınır değer kontrolleri
print("-"*10,">= Greater than or equal to(büyük eşit mi)","-"*10)
sinav_notu = 50
gecme_notu = 50
print(sinav_notu >= gecme_notu) # sonuç: True(öğrenci tam sınırda geçti)

print("-"*10,"<= Less than or equal to(küçük eşit mi)","-"*10)
hiz = 120
limit_hiz = 120
print(hiz <= limit_hiz) # True(ceza yemedi, tam limitte)





