#iç içe if yapısı
age = 15
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")

ogr_not = 55
gecme_notu = 55
gecti_mi = True

if ogr_not >= 55:
    if gecme_notu >= 80:
        if gecti_mi:
            print("Öğrenci AA geçti")
    else:
        print("Geçti ama zayıf not")
else:
    print("Kaldı")


