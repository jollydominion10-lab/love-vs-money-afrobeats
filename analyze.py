import pandas as pd

df = pd.read_csv("songs.csv")
df["title_lower"] = df["title"].str.lower()

love_words = ["love", "baby", "heart", "forever"]
money_words = ["money", "cash", "rich", "fund", "dollar", "pay"]

def label(title):
    has_love = any(word in title for word in love_words)
    has_money = any(word in title for word in money_words)
    if has_love and has_money:
        return "both"
    if has_love:
        return "love"
    if has_money:
        return "money"
    return "other"

df["theme"] = df["title_lower"].apply(label)

print("Total songs:", len(df))
print()
print("Theme counts:")
print(df["theme"].value_counts())
print()
print("Love vs money by year group:")
df["period"] = df["year"].apply(lambda y: "2017-2020" if y <= 2020 else "2021-2026")
print(pd.crosstab(df["period"], df["theme"]))
