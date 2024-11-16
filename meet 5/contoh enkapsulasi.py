class Makanan:
    def __init__(self, nama, kalori):
        self.__nama = nama  # Variabel privat
        self._kalori = kalori  # Variabel proteksi

    def tampilkan_info(self):
        print(f"Nama Makanan: {self.__nama}")
        print(f"Jumlah Kalori: {self._kalori} kkal")

class MakananSehat(Makanan):
    def tampilkan_kalori(self):
        print(f"Kalori Makanan Sehat: {self._kalori} kkal")

# Membuat objek dari kelas Makanan
makanan1 = Makanan("Nasi Goreng", 500)
makanan1.tampilkan_info()

# Membuat objek dari kelas MakananSehat
makanan2 = MakananSehat("Salad", 150)
makanan2.tampilkan_info()
makanan2.tampilkan_kalori()