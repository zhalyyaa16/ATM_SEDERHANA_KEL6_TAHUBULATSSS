from data import akun as data_akun

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

        for norek, data in data_akun.items():
            self.akun[norek] = Akun(
                no_rekening=norek,
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

        akun.riwayat.append(
            f"Setor tunai Rp {nominal:,}"
        )

        return True, "Setor tunai berhasil"

    def tarik(self, akun, nominal):
        if nominal > akun.saldo:
            return False, "Saldo tidak mencukupi"

        akun.saldo -= nominal

        akun.riwayat.append(
            f"Tarik tunai Rp {nominal:,}"
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

        pengirim.riwayat.append(
            f"Transfer ke {penerima.nama} Rp {nominal:,}"
        )

        penerima.riwayat.append(
            f"Transfer dari {pengirim.nama} Rp {nominal:,}"
        )

        return True, f"Transfer berhasil ke {penerima.nama}"

    def get_riwayat(self, akun):
        return akun.riwayat