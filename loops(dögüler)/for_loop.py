# for loop(for döngüsü): daha çok liste,tuple ve dictionary üzerinde işlemler yapmak için kullanılır.

# kullanıcıdan alınan n sayısına kadar tüm sayıları topla. ör: kullanıcı 10 (1 den başlayıp 11 ' a kadar olan sayıları toplar 11 dahil değildir.)

# range(1, n+1)

# n = int(input("Kaça kadar toplayalım: "))
# toplam = 0
# for i in range(1, n + 1): 
#     toplam = toplam + i # 0 + 1, 1 + 2, 3 + 3, 6 + 4,10 + 5, 

# print(f"1'den {n}'e kadar olan sayıların toplamı: {toplam}")


# faktöriyel hesaplama
# n! = 1 * 2 * 3 * 4....n => n = 5 = 5!=> 5 * 4 * 3 * 2 * 1 = 120
# her adımda sonucu bir öncekiyle çarparız.
# range(1,n + 1) # 0'dan kaçınmak için 1'den başla diyoruz.

# n = int(input("Sayı Gir: "))
# sonuc = 1
# for i in range(1,n + 1):
#     sonuc *=i #sonuc = sonuc * i

# print(f"{n}! = {sonuc}")


# asal sayıları bulan app
# 2'den n'e kadar asal sayıları bulur. yalnızca 1 ve kendisine bölünen sayılar asaldır.

# for döngüsü ile her sayının bölenlerini kontrol edelim ve kullanıcıdan aldığımız sayı aralığındaki asal sayıları ekrana yazdıralım

n = int(input("Kaça kadar asal sayı bulalım: "))
asallar = []
for sayi in range(2, n + 1):
    asal_mi = True
    for bolen in range(2, sayi):
        if sayi % bolen == 0:
            asal_mi = False
            break
    if asal_mi:
        asallar.append(sayi)
print(f"Asal sayılar: {asallar}")
#eğer liste uzunluğnu görmek istersem
print(f"Toplamda {len(asallar)} adet asal sayı vardır.")

