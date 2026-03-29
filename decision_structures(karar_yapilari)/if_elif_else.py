#Programlar her zaman aynı adımları takip etmez. Bir koşul doğruysa bir şey, yanlışsa başka bir şey yapması gerekir. İşte bu noktada dallanma ifadeleri devreye girer.

# if koşul doğruysa çalışır.
# elif koşul doğruysa çalışır. aynı zamanda if koşuluna alternatif olarak kullanılır.
# else koşul doğru değilse çalışır. if ve elif koşullarına alternatif olarak kullanılır.

# 📐 if Sözdizimi
# if koşul:
#     # koşul True ise bu satır çalışır
#     ifade


a = 12
if a > 13: # koşul ifadesi True ise bu satır çalışır. false ise bu satır atlanır.
    print("a 13'ten büyüktür.")
elif a == 14: #false olduğu için bu satır atlanır.
    print("a 14'e eşittir.")
elif a < 11: #false olduğu için bu satır atlanır.
    print("a 11'den küçüktür.")
elif a == 12: #true olduğu için bu satır çalışır.
    print("a 12'ye eşittir.")

# a,b,c değişkenlerinin en büyüğünü bulmak için if-elif-else yapısını kullanabiliriz.
a = 12
b = 15
c = 10
if a > b and a > c: # and eğer her iki koşul da doğruysa True döner. a'nın b'den büyük ve a'nın c'den büyük olması gerekir.
    print("a en büyüktür.")
elif b > a and b > c:
    print("b en büyüktür.")
elif c > a and c > b:
    print("c en büyüktür.")
else:
    print("a, b ve c eşittir.")

# a,b,c değişkenlerinin en büyüğünü bulmak için if-elif-else yapısını kullanabiliriz.
a = 10
b = 20
c = 15
if a > b:
    print (f"a büyüktür b.")
elif a > c:
    print(f"a büyüktür c.")
elif b < c:
    print(f"b büyüktür c.")
elif a < c < b:
    print(f"b büyüktür a ve c.")
else:
    print(f"c büyüktür a ve b.")

# yaş hesaplama programı ve ehliyet alma durumu. eğer yaşı 17'ye eşit veya büyükse ehliyet alabilir, değilse alamaz. yaş bilgisini kullanıcıdan alarak bu programı yazalım.

yas = input("Yaşınızı giriniz: ") # input fonksiyonu kullanıcıdan veri almak için kullanılır. input fonksiyonu her zaman string (metin) döner. bu yüzden yaş değişkeni string olarak saklanır.
yas = int(yas) # yaş değişkenini integer (tamsayı) tipine dönüştürürüz.

if yas >= 17:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsınız.")


