class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir, yetenekler: list):
        self.Ad = ad
        self.Soyad = soyad
        self.Yas = yas
        self.Ulke = ulke
        self.Sehir = sehir
        self.Yetenekler = yetenekler

    def kisi_bilgileri(self):
        return self.Ad, self.Soyad, self.Yas, self.Ulke, self.Sehir, self.Yetenekler

    def yetenek_ekle(self, yeni_yetenek):
        self.Yetenekler.append(yeni_yetenek)


insan1 = Insan("furkan", "korkmaz", "25", "türkiye", "istanbul", ["bisiklete binmek", "python"])
insan1.yetenek_ekle("ata binmek")
print(insan1.kisi_bilgileri())
