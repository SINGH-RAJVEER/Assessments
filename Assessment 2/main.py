from pymongo import MongoClient
from datetime import datetime, timezone

client = MongoClient("mongodb://localhost:27017/")
db = client["book_rental_service"]

users = db["users"]
books = db["books"]
rentals = db["rentals"]
reviews = db["reviews"]

def get_books_rented_by_user(user_id):
    pipeline = [
        {"$match": {"user_id": user_id}},
        {
            "$lookup": {
                "from": "books",
                "localField": "book_id",
                "foreignField": "_id",
                "as": "book_info"
            }
        },
        {"$unwind": "$book_info"},
        {
            "$project": {
                "_id": 0,
                "title": "$book_info.title",
                "author": "$book_info.author",
                "rental_date": 1,
                "due_date": 1,
                "return_date": 1
            }
        }
    ]
    results = list(rentals.aggregate(pipeline))
    for r in results:
        print(r)

def list_overdue_rentals():
    today = datetime.now(timezone.utc)
    overdue = rentals.find({
        "due_date": {"$lt": today},
        "return_date": None
    })
    for r in overdue:
        user = users.find_one({"_id": r["user_id"]})
        book = books.find_one({"_id": r["book_id"]})
        print({
            "user": user["name"],
            "book": book["title"],
            "due_date": r["due_date"]
        })

def rent_book(user_id, book_id):
    book = books.find_one({"_id": book_id})
    if book["available_copies"] > 0:
        rental = {
            "user_id": user_id,
            "book_id": book_id,
            "rental_date": datetime.now(timezone.utc),
            "due_date": datetime.now(timezone.utc).replace(day=datetime.now(timezone.utc).day + 14),
            "return_date": None
        }
        rentals.insert_one(rental)
        books.update_one(
            {"_id": book_id},
            {"$inc": {"available_copies": -1}}
        )
        print("Book rented successfully.")
    else:
        print("No copies available.")

def get_average_rating_per_book():
    pipeline = [
        {
            "$group": {
                "_id": "$book_id",
                "avg_rating": {"$avg": "$rating"},
                "count": {"$sum": 1}
            }
        },
        {
            "$lookup": {
                "from": "books",
                "localField": "_id",
                "foreignField": "_id",
                "as": "book_info"
            }
        },
        {"$unwind": "$book_info"},
        {
            "$project": {
                "title": "$book_info.title",
                "avg_rating": 1,
                "count": 1
            }
        }
    ]
    results = list(reviews.aggregate(pipeline))
    for r in results:
        print(r)

get_average_rating_per_book()
rent_book(101, 201)
get_books_rented_by_user(101)
list_overdue_rentals()