# this is the file i will be using for my practice sessions on this Assignment.

import pandas as pd 

# first name a variable and then see what is in the file.
df = pd.read_csv("dirty_finance.csv")

# lets clean it up it as some empty spaces lets start with the category section. 
df["category"] = (
    df["category"]
    .fillna("unknown")
    .astype(str)
    .str.strip()
    .str.lower()
)

# lets now clean the amount section
df["amount"] = (
    df["amount"]
    .astype(str)
    .str.replace("K", "", regex=False)
    .str.replace("k", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
    .replace("", "0")
)

# convert amount to float in a cleaner way.
df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)

# drop empty sections
df = df.drop_duplicates()

print(df)