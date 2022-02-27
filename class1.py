giden_net = 0
netsayisi = 0
puan = 0


class Ogrenci:
    ogrenciAdi = "furkan"
    ogrenciSoyadi = "korkmaz"
    ogrenciSinifi = "5-A"


ogrenci1 = Ogrenci()


class Soru:
    def netsayisi(self, dogru_sayisi, yanlis_sayisi, bos_sayisi):
        self.dogru_sayisi = dogru_sayisi
        self.yanlis_sayisi = yanlis_sayisi
        self.bos_sayisi = bos_sayisi


dogru_sayisi = int(input("doğru sayısı : "))
yanlis_sayisi = int(input("yanlış sayısı : "))
bos_sayisi = int(input("boş sayısı : "))
if dogru_sayisi + yanlis_sayisi + bos_sayisi != 50:
    print("lütfen toplamları 50 olacak şekilde giriniz.")
else:
    giden_net = yanlis_sayisi / 4
    giden_net = float(giden_net)
    netsayisi = dogru_sayisi - giden_net
    netsayisi = float(netsayisi)


class Soru:
    def hesapla(self, puan):
        self.puan = puan


puan = float(netsayisi * 2)
print(ogrenci1.ogrenciAdi, ogrenci1.ogrenciSoyadi, ogrenci1.ogrenciSinifi, "net sayısı:", netsayisi, "Puanı:", puan)
