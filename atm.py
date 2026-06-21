from data import akun as data_akun
import data

class Akun:
    def __init__(self, no_rekening, nama, pin, saldo):
        self.no_rekening = no_rekening
        self.nama = nama
        self.pin = pin
        self.saldo = saldo
        self.riwayat = []


class ATM:
    def __init__(self):
        self.akun = {}

        for data in data_akun:
            self.akun[data["no_rekening"]] = Akun(
                no_rekening=data["no_rekening"],
                nama=data["nama"],
                pin=data["pin"],
                saldo=data["saldo"]
    )

    def login(self, no_rekening, pin):
        if (
            no_rekening in self.akun
            and self.akun[no_rekening].pin == pin
        ):
            return self.akun[no_rekening]

        return None

    def setor(self, akun, nominal):
        akun.saldo += nominal

        akun.riwayat.append({
        "jenis": "Setor Tunai",
        "nominal": nominal
    })

        return True, "Setor tunai berhasil"

    def tarik(self, akun, nominal):
        if nominal > akun.saldo:
            return False, "Saldo tidak mencukupi"

        akun.saldo -= nominal

        akun.riwayat.append(
            {
                "jenis": "Tarik Tunai",
                "nominal": nominal
            }
        )

        return True, "Tarik tunai berhasil"

    def transfer(self, pengirim, norek_tujuan, nominal):
        if norek_tujuan not in self.akun:
            return False, "Rekening tujuan tidak ditemukan"

        if nominal > pengirim.saldo:
            return False, "Saldo tidak mencukupi"

        penerima = self.akun[norek_tujuan]

        pengirim.saldo -= nominal
        penerima.saldo += nominal

        pengirim.riwayat.append({
             "jenis": "Transfer Keluar",
             "tujuan": penerima.nama,
             "nominal": nominal
         })

        penerima.riwayat.append(
            {
                "jenis": "Transfer Masuk",
                "dari": pengirim.nama,
                "nominal": nominal
            }
        )

        return True, f"Transfer berhasil ke {penerima.nama}"

    def get_riwayat(self, akun):
        return akun.riwayat