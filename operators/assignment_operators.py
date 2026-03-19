"""
Operator	Example	                                 Same As	
=	        x = 5	                                 x = 5	
+=	        x += 3	                                 x = x + 3	
-=	        x -= 3	                                 x = x - 3	
*=	        x *= 3	                                 x = x * 3	
/=	        x /= 3	                                 x = x / 3	
%=	        x %= 3	                                 x = x % 3	
//=	        x //= 3	                                 x = x // 3	
**=	        x **= 3	                                 x = x ** 3	
&=	        x &= 3	                                 x = x & 3	
|=	        x |= 3	                                 x = x | 3	
^=	        x ^= 3	                                 x = x ^ 3	
>>=	        x >>= 3	                                 x = x >> 3	
<<=	        x <<= 3	                                 x = x << 3	
:=	        print(x := 3)	x = 3
print(x)
"""

print("----------------- Standart atama op(=) -----------------")
a = 5 # a değişkenine 5 değerini atadım.
print("----------------- Topla ve ata op(+=) -----------------")
b = 5; b += 2; b = b + 2 # ikisi de aynı.
print("-----------------Topla ve ata op (-=)-----------------")
c = 5; c -= 2; c = c - 2 # ikisi de aynı.
print("-----------------Çarp ve ata op (*=)-----------------")
x = 5; x *= 6; x = x * 6 # ikisi de aynı.


""" elma stok takibi-----------
adım 1: Başla

adım 2: sabit değerleri belirle(stok_miktari = 50; elma_fiyati = 5)
adım 3: kullanıcıdan "kaç adet elma istediğini" sor ve bu değeri al(istenen_deger)
adım 4:(hesaplama) istenen miktarı birim fiyatla çarp ve topla.
adım 5: (kontrol/kıyas) istenen mikatarın mevcut stoktan küçük veya eşit olup olmadığını kontrol et.
adım 6: eğer miktar uygunsa "true" değilse "false" sonucu istensin.
adım 7: toplam tutarı ve stok durumunu ekrana yazdır.

adım 8: Bitir
"""
stok_miktari = 50; elma_fiyati = 5 #adım 2
istenen_deger = int(input("Kaç adet elma almak istersin: ")) #adım 3
toplam_tutar = istenen_deger * elma_fiyati # adım 4: burda kullanıcıdan aldığımız değerle elma fiyatıyla çarptık ve topladık.(kullanıcı 8 adet almak isterse toplam_tutar 40 olur)
stok_yeterli_mi = istenen_deger <= stok_miktari # adım 5

stok_miktari -= istenen_deger # eğer satın alınırsa stoktan düş
print(f"kalan elmalar: {stok_miktari}")
print(f"stok yeterli mi: {stok_yeterli_mi}")
print(f"Toplam Tutar: {toplam_tutar}")
print(f"stokta var mı: {stok_yeterli_mi}")



