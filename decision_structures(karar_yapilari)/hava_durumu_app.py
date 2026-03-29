# eğer hava durumu 10-15 arasında ise "hava ılık", 15 dercenin üzerinde ise "hava süper", eğer 25 derecenin üzerinde ise "hava sıcak", eğer 30 derecenin üzerinde ise "hava çok sıcak" ise "Tişört giy" uyarısı verelim. bunların hiç biri değilse "hava soğuk" yazsın. hava soğuk ise kullanıcıya "kalın şeyler giy" uyarı ver.

derece = int(input("Hava sıcaklığını giriniz: "))

# karar yapısı
if derece > 30:
    print("Hava çok sıcak! Tişört giy")
elif derece > 25:
    print("Hava sıcak. Hafif şeyler giyebilirsin!")
elif derece > 15:
    print("Hava süper!")
elif derece >=10:
    print("Hava ılık.")
elif derece < 0:
    print(f"Hava sıfırın altında {derece} derecedir. Dikkat et. Üşütme!!!!!")
else:
    print("Hatalı giriş")
