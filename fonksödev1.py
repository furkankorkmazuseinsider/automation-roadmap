

def bolunenSayiBulma(min_sayi,max_sayi,bolunecek_sayi):
        dizi = []
        for i in range(min_sayi,max_sayi+1):
            if  ( i % bolunecek_sayi==0) :
                dizi.append(i)
        toplam_sayi = int(len(dizi))
        print("toplam sayı : ", toplam_sayi)

        return dizi

while True:

    min_sayi = int(input("minimum sayı : "))
    max_sayi = int(input("maximum sayı : "))
    bolunecek_sayi = int(input("bölünecek sayı : "))

    print("bölünenlerdizisi :  ", bolunenSayiBulma(min_sayi,max_sayi,bolunecek_sayi))






"""


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



 


global vize1,vize2,final
while True:
    vize1 = int(input("Vize1:"))
    if (vize1 > 100 or vize1 < 0):
       print("Lütfen 0-100 aralığında not giriniz")
       continue
    vize2 = int(input("Vize2:"))
    if (vize2 > 100 or vize2 < 0):
       print("Lütfen 0-100 aralığında not giriniz")
       continue
    final = int(input("Final:"))
    if (final > 100 or final < 0):
       print("Lütfen 0-100 aralığında not giriniz")
       continue

    genel_not = vize1 * 3 / 10 + vize2 * 3 / 10 + final * 4 / 10

    if (genel_not >= 90):
        print("AA")
    elif (genel_not >= 85):
        print("BA")
    elif (genel_not >= 80):
        print("BB")
    elif (genel_not >= 75):
        print("CB")
    elif (genel_not >= 70):
        print("CC")
    elif (genel_not >= 65):
        print("DC")
    elif (genel_not >= 60):
        print("DD")
    elif (genel_not >= 55):
        print("FD")
    else:
        print("FF")
    break

"""