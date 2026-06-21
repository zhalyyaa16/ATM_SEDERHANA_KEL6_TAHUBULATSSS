import csv

akun = []

with open("data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        akun.append({
            "no_rekening": row["no_rekening"],
            "nama": row["nama"],
            "pin": row["pin"],
            "saldo": int(row["saldo"])
        })