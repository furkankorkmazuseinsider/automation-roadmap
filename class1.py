class Ogrenci:
    ogrenciAdi = "furkan"
    ogrenciSoyadi = "korkmaz"
    ogrenciSinifi = "5-A"


ogrenci1 = Ogrenci()


class Soru:
    def __init__(self):
        self.yanlis = yanlis
        self.bos = bos
        self.puan = puan
        self.dogru = dogru

    def net_sayisi(self):
        return self.yanlis, self.dogru, self.bos

    def hesapla(self):
        return self.puan


dogru = int(input("doğru sayısı : "))
yanlis = int(input("yanlış sayısı : "))
bos = int(input("boş sayısı : "))
if dogru + yanlis + bos != 50:
    print("lütfen toplamları 50 olacak şekilde giriniz.")
else:
    giden_net = yanlis / 4
    giden_net = float(giden_net)
    netsayisi = dogru - giden_net
    netsayisi = float(netsayisi)
    puan = float(netsayisi * 2)
    print(ogrenci1.ogrenciAdi, ogrenci1.ogrenciSoyadi, ogrenci1.ogrenciSinifi, "net sayısı:", netsayisi, "Puanı:", puan)
