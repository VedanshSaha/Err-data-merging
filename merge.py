import pandas as pd

df = pd.read_csv('dwarf_stars.csv')
# df = df['Star_name'].notna()
df = df['Distance'].notna()

for i in enumerate(df]) :
    a = df[4][i]
    print(a)
