def bolunen_sayi_bulma(minsayi, maxsayi, boluneceksayi):
    dizi = []
    for eleman in range(minsayi, maxsayi + 1):
        if eleman % boluneceksayi == 0:
            dizi.append(eleman)
    print("toplam sayı : ", len(dizi))
    return dizi


min_sayi = int(input("minimum sayı : "))
max_sayi = int(input("maximum sayı : "))
bolunecek_sayi = int(input("bölünecek sayı : "))
print("bölünenlerdizisi : ", bolunen_sayi_bulma(min_sayi, max_sayi, bolunecek_sayi))
