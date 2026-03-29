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

#Date cleaner
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["date"] = df["date"].ffill()
df["date"] =df["date"].bfill()

# drop empty sections
df = df.drop_duplicates()

#totals spent
total_spent = df["amount"].sum()
average_spent = df["amount"].mean()
max_amount = df["amount"].max()
min_amount = df["amount"].min()

# preping plotting data 
category_totals = df.groupby("category")["amount"].sum().sort_values(ascending=False)
daily_totals = df.groupby("dates")["amount"].sum()


print(df)
print(f"The Total Amount Spent: {total_spent}")
print(f"Average Transaction: {average_spent}")
print(f"Largest Transaction: {max_amount}")
print(f"smallest Transaction: {min_amount}")
print(category_totals)
print(daily_totals)


