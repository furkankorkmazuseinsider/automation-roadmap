birler_bas = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar_bas = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def sayı_okunusu(sayı_atama):


    birinci = sayı_atama % 10
    ikinci = sayı_atama // 10

    return onlar_bas[ikinci] + " " + birler_bas[birinci]

sayı_atama = int(input("Sayı:"))

if ( sayı_atama > 99):
    print("lütfen geçerli format  olan iki basamaklı sayı giriniz")

elif (sayı_atama < 10):
   print("lütfen geçerli format olan iki basamaklı sayı giriniz")

else:
    print(sayı_okunusu(sayı_atama))

