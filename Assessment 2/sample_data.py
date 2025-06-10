from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["book_rental_service"]

db.books.delete_many({})
db.users.delete_many({})
db.rentals.delete_many({})
db.reviews.delete_many({})

books = [
  { "_id": 201, "title": "1984", "author": "George Orwell", "isbn": "9780451524935", "available_copies": 2, "total_copies": 3 },
  { "_id": 202, "title": "To Kill a Mockingbird", "author": "Harper Lee", "isbn": "9780061120084", "available_copies": 0, "total_copies": 2 },
  { "_id": 203, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "isbn": "9780743273565", "available_copies": 0, "total_copies": 1 },
  { "_id": 204, "title": "Dune", "author": "Frank Herbert", "isbn": "9780441013593", "available_copies": 3, "total_copies": 5 },
  { "_id": 205, "title": "The Hobbit", "author": "J.R.R. Tolkien", "isbn": "9780618260300", "available_copies": 4, "total_copies": 4 },
  { "_id": 206, "title": "Pride and Prejudice", "author": "Jane Austen", "isbn": "9780141439518", "available_copies": 1, "total_copies": 3 },
  { "_id": 207, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "isbn": "9780316769488", "available_copies": 0, "total_copies": 2 },
  { "_id": 208, "title": "Brave New World", "author": "Aldous Huxley", "isbn": "9780060850524", "available_copies": 2, "total_copies": 2 },
  { "_id": 209, "title": "Fahrenheit 451", "author": "Ray Bradbury", "isbn": "9781451673319", "available_copies": 1, "total_copies": 3 },
  { "_id": 210, "title": "Moby Dick", "author": "Herman Melville", "isbn": "9781503280786", "available_copies": 2, "total_copies": 2 },
  { "_id": 211, "title": "War and Peace", "author": "Leo Tolstoy", "isbn": "9781400079988", "available_copies": 1, "total_copies": 1 },
  { "_id": 212, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "isbn": "9780618640157", "available_copies": 0, "total_copies": 3 },
  { "_id": 213, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "isbn": "9780486415871", "available_copies": 2, "total_copies": 2 },
  { "_id": 214, "title": "The Odyssey", "author": "Homer", "isbn": "9780140268867", "available_copies": 3, "total_copies": 3 },
  { "_id": 215, "title": "Frankenstein", "author": "Mary Shelley", "isbn": "9780486282114", "available_copies": 0, "total_copies": 2 },
  { "_id": 216, "title": "Jane Eyre", "author": "Charlotte Brontë", "isbn": "9780141441146", "available_copies": 1, "total_copies": 1 },
  { "_id": 217, "title": "Wuthering Heights", "author": "Emily Brontë", "isbn": "9780141439556", "available_copies": 2, "total_copies": 3 },
  { "_id": 218, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "isbn": "9780486278070", "available_copies": 1, "total_copies": 2 },
  { "_id": 219, "title": "Dracula", "author": "Bram Stoker", "isbn": "9780486411095", "available_copies": 0, "total_copies": 1 },
  { "_id": 220, "title": "A Tale of Two Cities", "author": "Charles Dickens", "isbn": "9780141439600", "available_copies": 3, "total_copies": 3 },
  { "_id": 221, "title": "Les Misérables", "author": "Victor Hugo", "isbn": "9780451419439", "available_copies": 1, "total_copies": 1 },
  { "_id": 222, "title": "The Alchemist", "author": "Paulo Coelho", "isbn": "9780062315007", "available_copies": 2, "total_copies": 4 },
  { "_id": 223, "title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "isbn": "9780062316097", "available_copies": 1, "total_copies": 3 }
]

users = [
  { "_id": 101, "name": "Alice", "email": "alice@example.com", "membership_date": { "$date": "2023-01-10T00:00:00Z" } },
  { "_id": 102, "name": "Bob", "email": "bob@example.com", "membership_date": { "$date": "2023-02-15T00:00:00Z" } },
  { "_id": 103, "name": "Charlie", "email": "charlie@example.com", "membership_date": { "$date": "2023-03-20T00:00:00Z" } },
  { "_id": 104, "name": "David", "email": "david@example.com", "membership_date": { "$date": "2023-04-01T00:00:00Z" } },
  { "_id": 105, "name": "Emily", "email": "emily@example.com", "membership_date": { "$date": "2023-04-05T00:00:00Z" } },
  { "_id": 106, "name": "Frank", "email": "frank@example.com", "membership_date": { "$date": "2023-05-11T00:00:00Z" } },
  { "_id": 107, "name": "Grace", "email": "grace@example.com", "membership_date": { "$date": "2023-06-22T00:00:00Z" } },
  { "_id": 108, "name": "Henry", "email": "henry@example.com", "membership_date": { "$date": "2023-07-14T00:00:00Z" } },
  { "_id": 109, "name": "Ivy", "email": "ivy@example.com", "membership_date": { "$date": "2023-08-09T00:00:00Z" } },
  { "_id": 110, "name": "Jack", "email": "jack@example.com", "membership_date": { "$date": "2023-09-01T00:00:00Z" } },
  { "_id": 111, "name": "Kate", "email": "kate@example.com", "membership_date": { "$date": "2023-10-18T00:00:00Z" } },
  { "_id": 112, "name": "Liam", "email": "liam@example.com", "membership_date": { "$date": "2023-11-25T00:00:00Z" } },
  { "_id": 113, "name": "Mia", "email": "mia@example.com", "membership_date": { "$date": "2023-12-30T00:00:00Z" } },
  { "_id": 114, "name": "Noah", "email": "noah@example.com", "membership_date": { "$date": "2024-01-15T00:00:00Z" } },
  { "_id": 115, "name": "Olivia", "email": "olivia@example.com", "membership_date": { "$date": "2024-02-20T00:00:00Z" } },
  { "_id": 116, "name": "Peter", "email": "peter@example.com", "membership_date": { "$date": "2024-03-10T00:00:00Z" } },
  { "_id": 117, "name": "Quinn", "email": "quinn@example.com", "membership_date": { "$date": "2024-04-05T00:00:00Z" } },
  { "_id": 118, "name": "Rachel", "email": "rachel@example.com", "membership_date": { "$date": "2024-05-12T00:00:00Z" } },
  { "_id": 119, "name": "Sam", "email": "sam@example.com", "membership_date": { "$date": "2024-06-19T00:00:00Z" } },
  { "_id": 120, "name": "Tina", "email": "tina@example.com", "membership_date": { "$date": "2024-07-21T00:00:00Z" } },
  { "_id": 121, "name": "Uma", "email": "uma@example.com", "membership_date": { "$date": "2024-08-28T00:00:00Z" } },
  { "_id": 122, "name": "Victor", "email": "victor@example.com", "membership_date": { "$date": "2024-09-16T00:00:00Z" } },
  { "_id": 123, "name": "Wendy", "email": "wendy@example.com", "membership_date": { "$date": "2024-10-03T00:00:00Z" } }
]

rentals = [
  { "_id": 401, "user_id": 101, "book_id": 201, "rental_date": { "$date": "2024-05-01T00:00:00Z" }, "due_date": { "$date": "2024-05-15T00:00:00Z" }, "return_date": { "$date": "2024-05-10T00:00:00Z" } },
  { "_id": 402, "user_id": 102, "book_id": 202, "rental_date": { "$date": "2025-05-20T00:00:00Z" }, "due_date": { "$date": "2025-06-04T00:00:00Z" }, "return_date": None },
  { "_id": 403, "user_id": 103, "book_id": 203, "rental_date": { "$date": "2025-05-25T00:00:00Z" }, "due_date": { "$date": "2025-06-09T00:00:00Z" }, "return_date": None },
  { "_id": 404, "user_id": 104, "book_id": 204, "rental_date": { "$date": "2025-01-10T00:00:00Z" }, "due_date": { "$date": "2025-01-25T00:00:00Z" }, "return_date": { "$date": "2025-01-20T00:00:00Z" } },
  { "_id": 405, "user_id": 105, "book_id": 206, "rental_date": { "$date": "2025-02-15T00:00:00Z" }, "due_date": { "$date": "2025-03-02T00:00:00Z" }, "return_date": { "$date": "2025-03-05T00:00:00Z" } },
  { "_id": 406, "user_id": 101, "book_id": 205, "rental_date": { "$date": "2025-03-01T00:00:00Z" }, "due_date": { "$date": "2025-03-16T00:00:00Z" }, "return_date": { "$date": "2025-03-15T00:00:00Z" } },
  { "_id": 407, "user_id": 102, "book_id": 207, "rental_date": { "$date": "2025-04-20T00:00:00Z" }, "due_date": { "$date": "2025-05-05T00:00:00Z" }, "return_date": None },
  { "_id": 408, "user_id": 106, "book_id": 209, "rental_date": { "$date": "2025-04-22T00:00:00Z" }, "due_date": { "$date": "2025-05-07T00:00:00Z" }, "return_date": { "$date": "2025-05-01T00:00:00Z" } },
  { "_id": 409, "user_id": 107, "book_id": 212, "rental_date": { "$date": "2025-04-25T00:00:00Z" }, "due_date": { "$date": "2025-05-10T00:00:00Z" }, "return_date": None },
  { "_id": 410, "user_id": 108, "book_id": 215, "rental_date": { "$date": "2025-05-01T00:00:00Z" }, "due_date": { "$date": "2025-05-16T00:00:00Z" }, "return_date": None },
  { "_id": 411, "user_id": 109, "book_id": 218, "rental_date": { "$date": "2025-05-02T00:00:00Z" }, "due_date": { "$date": "2025-05-17T00:00:00Z" }, "return_date": { "$date": "2025-05-15T00:00:00Z" } },
  { "_id": 412, "user_id": 110, "book_id": 222, "rental_date": { "$date": "2025-05-05T00:00:00Z" }, "due_date": { "$date": "2025-05-20T00:00:00Z" }, "return_date": None },
  { "_id": 413, "user_id": 111, "book_id": 214, "rental_date": { "$date": "2025-05-08T00:00:00Z" }, "due_date": { "$date": "2025-05-23T00:00:00Z" }, "return_date": { "$date": "2025-05-20T00:00:00Z" } },
  { "_id": 414, "user_id": 112, "book_id": 217, "rental_date": { "$date": "2025-05-10T00:00:00Z" }, "due_date": { "$date": "2025-05-25T00:00:00Z" }, "return_date": None },
  { "_id": 415, "user_id": 113, "book_id": 220, "rental_date": { "$date": "2025-05-12T00:00:00Z" }, "due_date": { "$date": "2025-05-27T00:00:00Z" }, "return_date": { "$date": "2025-05-28T00:00:00Z" } },
  { "_id": 416, "user_id": 114, "book_id": 208, "rental_date": { "$date": "2025-05-15T00:00:00Z" }, "due_date": { "$date": "2025-05-30T00:00:00Z" }, "return_date": None },
  { "_id": 417, "user_id": 115, "book_id": 213, "rental_date": { "$date": "2025-05-18T00:00:00Z" }, "due_date": { "$date": "2025-06-02T00:00:00Z" }, "return_date": None },
  { "_id": 418, "user_id": 116, "book_id": 219, "rental_date": { "$date": "2025-05-20T00:00:00Z" }, "due_date": { "$date": "2025-06-04T00:00:00Z" }, "return_date": None },
  { "_id": 419, "user_id": 117, "book_id": 223, "rental_date": { "$date": "2025-05-21T00:00:00Z" }, "due_date": { "$date": "2025-06-05T00:00:00Z" }, "return_date": None },
  { "_id": 420, "user_id": 104, "book_id": 212, "rental_date": { "$date": "2025-05-22T00:00:00Z" }, "due_date": { "$date": "2025-06-06T00:00:00Z" }, "return_date": None },
  { "_id": 421, "user_id": 105, "book_id": 202, "rental_date": { "$date": "2025-05-28T00:00:00Z" }, "due_date": { "$date": "2025-06-12T00:00:00Z" }, "return_date": None },
  { "_id": 422, "user_id": 118, "book_id": 209, "rental_date": { "$date": "2025-06-01T00:00:00Z" }, "due_date": { "$date": "2025-06-16T00:00:00Z" }, "return_date": None },
  { "_id": 423, "user_id": 119, "book_id": 222, "rental_date": { "$date": "2025-06-05T00:00:00Z" }, "due_date": { "$date": "2025-06-20T00:00:00Z" }, "return_date": None }
]

reviews = [
  { "_id": 301, "user_id": 101, "book_id": 201, "rating": 5, "comment": "Amazing!", "review_date": { "$date": "2024-05-12T00:00:00Z" } },
  { "_id": 302, "user_id": 102, "book_id": 202, "rating": 4, "comment": "Great read.", "review_date": { "$date": "2025-05-22T00:00:00Z" } },
  { "_id": 303, "user_id": 103, "book_id": 203, "rating": 3, "comment": "Good, but not my style.", "review_date": { "$date": "2025-05-28T00:00:00Z" } },
  { "_id": 304, "user_id": 104, "book_id": 204, "rating": 5, "comment": "A masterpiece of sci-fi.", "review_date": { "$date": "2025-01-22T00:00:00Z" } },
  { "_id": 305, "user_id": 105, "book_id": 206, "rating": 4, "comment": "A timeless classic.", "review_date": { "$date": "2025-03-06T00:00:00Z" } },
  { "_id": 306, "user_id": 101, "book_id": 205, "rating": 5, "comment": "A delightful adventure for all ages.", "review_date": { "$date": "2025-03-18T00:00:00Z" } },
  { "_id": 307, "user_id": 106, "book_id": 209, "rating": 4, "comment": "Thought-provoking and scary.", "review_date": { "$date": "2025-05-02T00:00:00Z" } },
  { "_id": 308, "user_id": 109, "book_id": 218, "rating": 5, "comment": "Wilde's wit is unmatched.", "review_date": { "$date": "2025-05-16T00:00:00Z" } },
  { "_id": 309, "user_id": 111, "book_id": 214, "rating": 4, "comment": "An epic journey.", "review_date": { "$date": "2025-05-21T00:00:00Z" } },
  { "_id": 310, "user_id": 113, "book_id": 220, "rating": 3, "comment": "A bit slow at times, but a powerful story.", "review_date": { "$date": "2025-05-29T00:00:00Z" } },
  { "_id": 311, "user_id": 102, "book_id": 207, "rating": 2, "comment": "I didn't connect with the protagonist.", "review_date": { "$date": "2025-05-01T00:00:00Z" } },
  { "_id": 312, "user_id": 107, "book_id": 212, "rating": 5, "comment": "The best fantasy book ever written.", "review_date": { "$date": "2025-05-15T00:00:00Z" } },
  { "_id": 313, "user_id": 108, "book_id": 215, "rating": 4, "comment": "A foundational text of gothic horror.", "review_date": { "$date": "2025-05-20T00:00:00Z" } },
  { "_id": 314, "user_id": 110, "book_id": 222, "rating": 5, "comment": "Inspirational and beautifully written.", "review_date": { "$date": "2025-05-25T00:00:00Z" } },
  { "_id": 315, "user_id": 112, "book_id": 217, "rating": 4, "comment": "Dark, passionate, and unforgettable.", "review_date": { "$date": "2025-05-28T00:00:00Z" } },
  { "_id": 316, "user_id": 114, "book_id": 208, "rating": 4, "comment": "A chilling vision of the future.", "review_date": { "$date": "2025-06-01T00:00:00Z" } },
  { "_id": 317, "user_id": 115, "book_id": 213, "rating": 5, "comment": "A psychological masterpiece.", "review_date": { "$date": "2025-06-05T00:00:00Z" } },
  { "_id": 318, "user_id": 116, "book_id": 219, "rating": 3, "comment": "Classic horror, but a bit dated.", "review_date": { "$date": "2025-06-08T00:00:00Z" } },
  { "_id": 319, "user_id": 117, "book_id": 223, "rating": 5, "comment": "Changed the way I see the world.", "review_date": { "$date": "2025-06-09T00:00:00Z" } },
  { "_id": 320, "user_id": 104, "book_id": 212, "rating": 5, "comment": "Had to read it again. Still amazing.", "review_date": { "$date": "2025-06-09T00:00:00Z" } },
  { "_id": 321, "user_id": 105, "book_id": 202, "rating": 4, "comment": "A very important book.", "review_date": { "$date": "2025-06-09T00:00:00Z" } },
  { "_id": 322, "user_id": 118, "book_id": 209, "rating": 4, "comment": "Still relevant today.", "review_date": { "$date": "2025-06-09T00:00:00Z" } },
  { "_id": 323, "user_id": 119, "book_id": 222, "rating": 5, "comment": "A journey worth taking.", "review_date": { "$date": "2025-06-09T00:00:00Z" } }
]

db.books.insert_many(books)
db.users.insert_many(users)
db.rentals.insert_many(rentals)
db.reviews.insert_many(reviews)

print("Sample data inserted") 