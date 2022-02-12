birler_bas = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar_bas = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
inputsayi = int(input("Sayı:"))
def sayiAtama(inputsayi):
    return inputsayi
def sayiOkunusu(sayi_atama):
    birinci = sayi_atama % 10
    ikinci = sayi_atama // 10
    return onlar_bas[ikinci] + " " + birler_bas[birinci]
if ( inputsayi > 99):
      print("lütfen geçerli format  olan iki basamaklı sayı giriniz")
elif (inputsayi < 10):
      print("lütfen geçerli format olan iki basamaklı sayı giriniz")
else:
      print(sayiOkunusu(inputsayi))
