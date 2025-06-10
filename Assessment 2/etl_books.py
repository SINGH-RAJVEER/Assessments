import pandas as pd
from pymongo import MongoClient

df = pd.read_csv("books.csv")
df = df.dropna(subset=["_id", "title", "author", "isbn", "available_copies", "total_copies"])

# standardization 
df["_id"] = df["_id"].astype(int)
df["available_copies"] = df["available_copies"].astype(int)
df["total_copies"] = df["total_copies"].astype(int)
df["title"] = df["title"].astype(str).str.strip()
df["author"] = df["author"].astype(str).str.strip()
df["isbn"] = df["isbn"].astype(str).str.strip()

# derived fields
df["is_available"] = df["available_copies"] > 0
df["percent_available"] = (df["available_copies"] / df["total_copies"] * 100).round(2)


client = MongoClient("mongodb://localhost:27017/")
db = client["book_rental_service"]
collection = db["books"]

records = df.to_dict(orient="records")
for record in records:
    collection.replace_one({"_id": record["_id"]}, record, upsert=True)

print("process completed successfully")