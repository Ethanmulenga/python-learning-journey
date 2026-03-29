import pandas as pd 

df = pd.read_csv("dirty_finance.csv")

# Clean the amount section
df["amount"] = (
    df["amount"]
    .astype(str)
    .str.replace("K", "", regex=False)
    .str.replace("k", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
    .replace("", "0") # this converts the empty string you converted to amount zero.
    
    )

# convert it to a float 
df["amount"] = pd.to_numeric(df["amount"], errors= "coerce").fillna(0)

# Clean the Category section
df["category"] = (
    df["category"]
    .fillna("unknown")
    .astype(str)
    .str.strip()
    .str.lower()
    
)

# Remove Duplicates
df = df.drop_duplicates()

print(df.info())
print(df.head())

