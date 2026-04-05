# for döngüsü ve while döngüsü karşılaştırması

# 1. aynı işi iki farklı yolla yapmak.
print("1. aynı işi iki farklı yolla yapmak.")
print("="*40)

print("\nfor döngüsü ile 1'den 5'e kadar say")
# liste = [1,2,3,4,5,6,7,8,9,10]
for gezgin in range(1,6):
    print(gezgin)

print("\nwhile döngüsü ile 1'den 5'e kadar say( önce artır sonra ekrana yazdır)")
i = 0
while i <= 6:
    i +=1 # önce artır sonra ekrana yazdır
    print(i, end=" ") # 1,2,3,4,5,6,7

print("\nwhile döngüsü ile 1'den 5'e kadar say(önce ekrana yazdır sonra artır.)")
i = 1
while i < 6: # koşul: i 6'dan küçük olduğu sürece döngü devam eder.
    print(i, end=" ") # önce ekrana yazdır sonra artır.
    i +=1 # burda artırma operatörü kullanmasaydık sonsuz bir döngü oluşrdu. döngüyü kırmak için ekrana önce i'nin ilk halini yazdırıp sonra i'yi 1 artırıp döngüyü devam ettiriz. burda da koşul sağlandığı sürece i değişkeni 1 artırılır.