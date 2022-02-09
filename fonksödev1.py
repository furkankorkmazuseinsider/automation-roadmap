

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


