class Insan:
    def __init__(self, Ad, Soyad, Yas, Ulke, Sehir, Yetenekler: list):
        self.Ad = Ad
        self.Soyad = Soyad
        self.Yas = Yas
        self.Ulke = Ulke
        self.Sehir = Sehir
        self.Yetenekler = Yetenekler

    def kisi_bilgileri(self):
        return self.Ad, self.Soyad, self.Yas, self.Ulke, self.Sehir, self.Yetenekler

    def yetenek_ekle(self, yeni_yetenek):
        self.Yetenekler.append(yeni_yetenek)


insan1 = Insan("furkan", "korkmaz", "25", "türkiye", "istanbul", ["bisiklete binmek", "python"])
insan1.yetenek_ekle("ata binmek")
print(insan1.kisi_bilgileri())
