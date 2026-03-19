# Artitmatik operatörler: Matematiksel işlemlerde kullanılır.

"""
+	Addition(toplama)	x + y
-	Subtraction(çıkarma)	x - y	
*	Multiplication(çarpma)	x * y	
/	Division(bölme)	x / y	
%	Modulus(mod alma)	x % y	
**	Exponentiation(üs alma)	x ** y	
//	Floor division(tam bölme)	x // y

"""
# print("-"*90)
# print("Toplama İşlemi")
# x = 4; y = 5
# t = x + y
# print(f"x + y = {t}")

# print("-"*90)
# print("Çıkarma İşlemi")
# x = 4; y = 7
# c = x - y
# print(f"x - y = {c}")

# print("-"*90)
# print("Çarpma İşlemi")
# x = 6; y = 15
# c = x * y
# print(f"x * y = {c}")

# HESAP MAKİNESİ

# 1-Kullanıcıdan iki sayı isteyin.
# sayi1 = input("Birinci sayıyı gir: ") # ör: eğer karışık karakterli şifre olacaksa input bu şekilde. yani içinde nümerik ve char ifadeler geçebilir. "A" =>char
sayi1 = int(input("Birinci sayıyı gir: ")) # eğer sadece tam sayı olsun istersek bu şekilde. 
sayi2 = int(input("İkinci sayıyı gir: ")) 
# 2-ilk sayı ile ikinci sayıyı topla,çıkar,çarp,böl,mod al.
toplam = sayi1 + sayi2
cikar = sayi1 - sayi2
carp = sayi1 * sayi2
bol = sayi1 / sayi2; tam_bolme = sayi1 // sayi2
mod_al = sayi1 % sayi2
print(f"➕iki sayının toplamı: {toplam}") # icon koymak için tr klavyede ctrl + shift + p bastıktan sonra emoji-insert kısmına tıklıyoruz.
print(f"iki sayının farkı: {cikar}")
print(f"iki sayının carpımı: {carp}")
print(f"➗ilk sayının ikinci sayıya bölümü: {bol}") #eğer float ise ondalıklı kısmıda gelir
print(f"ilk sayının ikinci sayıya bölümü: {tam_bolme}") # ondalıklı kısmını göstermez.
print(f"mod alma: {mod_al}") # kalanı bulma

