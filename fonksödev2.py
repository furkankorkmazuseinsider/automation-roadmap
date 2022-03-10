def sayiatama(inputsayi):
    if inputsayi > 99 or inputsayi < 10:
        print("lütfen geçerli format olan iki basamaklı sayı giriniz")
    else:
        sayi_atama = inputsayi
        sayiokunusu(sayi_atama)


def sayiokunusu(sayi_atama):
    birler_bas = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
    onlar_bas = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
    birinci = sayi_atama % 10
    ikinci = sayi_atama // 10
    print(onlar_bas[ikinci] + " " + birler_bas[birinci])


sayi = int(input("Sayı:"))
sayiatama(sayi)
