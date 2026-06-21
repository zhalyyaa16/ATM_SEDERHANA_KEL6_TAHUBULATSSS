import csv

akun = {}

with open("data.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        akun[row["no_rekening"]] = {
            "nama": row["nama"],
            "pin": row["pin"],
            "saldo": int(row["saldo"])
        }