import csv

with open("nilai.csv", "r", encoding="utf-8") as file:
    data = list(csv.DictReader(file))

nilai = [int(d["nilai"]) for d in data]
rata = sum(nilai) / len(nilai)
print(f"Rata-rata: {rata:.1f}")

lulus = [
    d["nama"] for d in data
    if int(d["nilai"]) >= 75
]
print("Lulus:", lulus)

top = max(data, key=lambda d: int(d["nilai"]))
print("Tertinggi:", top["nama"])