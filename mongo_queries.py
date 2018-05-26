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
	ids = []
	cityFound = db.cities.find_one({"name": "Odense"})
	for book_ids in cityFound:
		ids.append[book_ids]

	result = db.books.find({"titles": {"$where": city_ids == ids} })

	print(result)

def get_titles_for_city1():
	result = db.cities.aggregate([
		{
			'$unwind': 'city_ids'
		},
		{
			'$lookup':
				{
			    	'from': cities,
			    	'localField': 'city_ids',
			    	'foreignField': 'book_ids',
			    	'as': books
			    }
		}
	])

	print(result)

get_titles_for_city1()


def to_array(results):
        arrays = []
        for result in results:
                arrays.append(result[0])
        return arrays