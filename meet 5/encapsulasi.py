class KelasSaya:
    def __init__(self, variabel_privat, variabel_proteksi):
        self.__variabel_privat = variabel_privat  # Variabel privat
        self._variabel_proteksi = variabel_proteksi  # Variabel proteksi

    def tampilkan_nilai(self):
        print(f"Variabel privat: {self.__variabel_privat}")
        print(f"Variabel proteksi: {self._variabel_proteksi}")

class KelasTurunan(KelasSaya):
    def akses_proteksi(self):
        print(f"Mengakses variabel proteksi: {self._variabel_proteksi}")

# Membuat objek dari kelas KelasSaya
obj = KelasSaya(10, 20)
obj.tampilkan_nilai()

# Membuat objek dari kelas KelasTurunan
obj_turunan = KelasTurunan(30, 40)
obj_turunan.akses_proteksi()
