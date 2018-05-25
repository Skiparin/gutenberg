from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import pymongo
from pymongo import MongoClient


client = MongoClient("mongodb://127.0.0.1:27017")
db = client.book_database
books = db.books
authors = db.authors
cities = db.cities

#books.insert({"_id":1, "title": "books", "city_ids": arrays, "authors": arrays})


def get_titles_for_city():
	cityFound = db.cities.find_one({"name": "Odense"})
	#result = db.books.find({"titles": {"$in": ["city_ids": "True", cityFound]}})
	#result = db.books.find({"titles": {"$in": ["city_ids": "True", cityFound]}})

	print(cityFound)

get_titles_for_city()


def to_array(results):
        arrays = []
        for result in results:
                arrays.append(result[0])
        return arrays