# Q2

# a)
import pandas as pd

df =pd.read_excel("nba.xlsx")

duplicated_rows = df[df.duplicated()]
df = df.drop_duplicates()

print(f'Number of duplicated rows: {len(duplicated_rows)}')


# b)
df["College"].fillna("No college", inplace=True)

# c)
stars = df[df["Age"] <= 25]
stars[["Name", "Team", "Age"]].to_excel("nba_young_stars.xlsx", index=False)
