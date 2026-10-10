import csv

with open("nilai.csv", "r", encoding="utf-8") as file:
    data = list(csv.DictReader(file))

rekap = {}

for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(int(d["nilai"]))

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")

for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")