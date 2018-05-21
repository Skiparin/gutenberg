from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
import pymongo

def to_array(results):
        arrays = []
        for result in results:
                arrays.append(result[0])
        return arrays

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.book_database
books = db.books
authors = db.authors
cities = db.cities

#books.insert({"_id":1, "title": "books", "city_ids": arrays, "authors": arrays})


def getByCityName():
	for city in cities.find({}).count():	
		print(city)

getByCityName()