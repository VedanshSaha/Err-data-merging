import pandas as pd
import csv

df = pd.read_csv('dwarf_stars.csv')
df = df[df['Distance'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]

df["Mass"] = float(df["Mass"])
df["Radius"] = float(df["Radius"])

df["Mass"] = 0.000954588*df["Mass"]
df["Radius"] = 0.102763*df["Radius"]

with open("bright_stars.csv") as h:
    csv.reader = csv.reader(h)

with open("dwarf_stars.csv") as r:
    csv.reader = csv.reader(r)

with open("total_stars.csv","w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(h)
        csv_writer.writerow(r)



