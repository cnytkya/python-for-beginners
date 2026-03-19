# değişken tanımlama kuralları
# sayı ile başlayamaz => 1sayi = 3
#1- değişken isimleri bir harf(a-z) veya alt çizgi(_) ile başlayabilir. sayıyla başlamak yasaktır.

elma1 = 15 # veriabla = value(değişken = değer)
# 1elma = 15 yanlış tanımlama hata verir.

# 2-boşluk kullanılamaz(no spaces). değişken isminde boşluk bırakmak hata verir. boşluk yerine (_) alt çizgi kullanılabilir.
gunluk_yol_masrafları = 46
# gunluk yol masrafları = 46 bu şekilde hata verir.

# 3-Büyük/Küçük harf duyarlılığı vardır(case sensitivity)
# mesela py iin seftali,Seftali ve SEFTALI bunlar tamamen farklı değişkenlerdir.
seftali = 12
Seftali = 17
SEFTALI = 20 # bunların hepsi farklı kutu olduğunu düşünebilirsiniz.
elma = 10
yesil_elma = 45
Elma = 12
# print(Elma,seftali,Seftali,SEFTALI,elma)

# örneğin küçük e ile başlayan "elma" değişkenindeki değeri ekrana açıklamalı olarak yazdırmak istersek
print("🍎",elma)
print("🍏",yesil_elma)
# formatting string ile "yesil_elma" değerini str(yani çift tırnak içerisinde gösterimi) ile gösterimi
print(f"Yeşil Elma🍏: {yesil_elma}")
# print(f"🍏: {yesil_elma}")


# 3- özel karakterler içeremez: $,<,> , -, =
fiyat_dolar = 39 # doğru kullanım
# fiyat-dolar = 34 eksi işareti hata verdirir
# fiyat$ = 35 hata verir.

# 4- py nın özel kelimleri kullanılamaz(reserved word)
# if,else,for,while,class,True,False : bu özel tanımlamaları değişken olarak kullanamazsın.

# c# ile py arasındaki bazı farklar
seftali2 = 12.5 #py'da değişken tanımlama ve değer atama. değişkenin tipini belirtmene gerek yoktur, py bunu değerden anlar zaten(dynamic typing)
# double seftali = 12.5 # c# ta değişken tanımlama ve değer atama. c# değişkenişn tipini en başta açıkça bir şekilde belirtmelisin(static typing)


"""
                      ne öğrendik?
1-değişken tanımlama ve değer atama
2-değişken atama kuralları
3-syntax(py ve diğer yazılım dilleri ile karşılaştırılması)
4-print() fonk. ile ekrana yazdırma.
5-f-string kullanımı.
"""