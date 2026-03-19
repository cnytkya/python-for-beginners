# kullanıcıdan değer almak için input() func. kullanılır.
name = input("Adınızı giriniz: ") # input(kullanıcıdan girdi ister). str tipinde girdi.
number = int(input("Okul numaranızı giriniz: ")) # kullanıcdan özellikle int veya float tipinden değer almak istersek tipini başa yazmamız gerekir. eğer belirtmezsek girdi her ihtmalle str tipinde olur.
sube = input("Şube giriniz: ")
not_ortalamasi = float(input("Not ortalamanızı giriniz: "))
# print(f"Adınız: {name}")
# print(f"Okul Numaranız: {number}")
# print(f"Şubeniz: {sube}")

#Not: Alt alta hepsini ekrana basmak istediğimizde sürekli print kullanmak yerine aşağıdaki gibi yaparız
# \n kullanımı: sonraki satırı bir alt satıra iter.
print(f"Adınız: {name}\nOkul Numaranız: {number}\nŞubeniz: {sube}\nNot ort: {not_ortalamasi}")