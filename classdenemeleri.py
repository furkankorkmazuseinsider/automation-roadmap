class Insan:
    def __init__(self, Ad, Soyad, Yas, Ulke, Sehir, Yetenekler: list):
        self.Ad = Ad
        self.Soyad = Soyad
        self.Yas = Yas
        self.Ulke = Ulke
        self.Sehir = Sehir
        self.Yetenekler = Yetenekler

    def yetenek_ekle(self, yeni_yetenek):
        self.Yetenekler.append(yeni_yetenek)

    def kisi_bilgileri(self):
        print(f"""
        kişi bilgisi:
        Ad: {self.Ad}
        Soyad: {self.Soyad}
        Yaş: {self.Yas}
        Ülke: {self.Ulke}
        Şehir: {self.Sehir}
        Yetenekler: {self.Yetenekler}
        """)


insan1 = Insan("furkan", "korkmaz", "25", "türkiye", "istanbul", ["bisiklete binmek", "python"])
insan1.yetenek_ekle("ata binmek")
insan1.kisi_bilgileri()
