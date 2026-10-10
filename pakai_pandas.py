import pandas as pd

df = pd.read_csv("nilai.csv")

print("Rata-rata nilai per kelas:")
print(df.groupby("kelas")["nilai"].mean())

print("\nSiswa yang lulus:")
print(df[df["nilai"] >= 75]["nama"].tolist())

print("\nNilai tertinggi:")
print(df.sort_values("nilai", ascending=False).head(1))