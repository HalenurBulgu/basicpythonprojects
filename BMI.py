ad1 = input("Lütfen adınızı yazınız")
ad = ad1.capitalize()
soyad1 = input("lütfen soyadınızı yazınız")
soyad = soyad1.capitalize()
 
boy1 = int(input("lütfen boyunuzu yazınız"))
boy= boy1/100
kilo = int(input("lütfen kilonuzu yazınız"))

kitle_endeks = kilo/(boy**2)

if kitle_endeks < 18.49:
    print(ad+" "+soyad+" "+"ideal kilonun altındasınız")
elif 18.5<kitle_endeks<24.99:
    print(ad+" "+soyad+" "+ "ideal kilodasınız")
elif 25< kitle_endeks <29.99:
    print(ad+" "+soyad+ " "+"ideal kilonun üzerindesiniz")
else:
    (ad+" "+soyad+ " " +"ideal kilonun çok üzerindesiniz")
    
