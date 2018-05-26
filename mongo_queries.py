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
	book_array = []
	ids = cities.find_one({"name": "Odense"},{'book_ids': 1})
	book_results = books.find({'_id': {'$in': ids["book_ids"] }}, {'title': 1, 'authors': 1})
	for book in book_results:
		author_array = []
		if 'authors' in book:
			author_results = authors.find({'_id': {'$in': book['authors']}})
			for author in author_results:
				author_array.append(author['name'])
		temp_array = [book['title'], author_array]
		book_array.append(temp_array)
	return book_array

def get_cities_for_title():
	city_array = []
	ids = books.find_one({"title": "Denmark"},{"city_ids":1})
	city_result = cities.find({'_id': {'$in': ids['city_ids'] }},{'x_cord': 1, 'y_cord': 1})
	array = []
	for r in city_result:
		array.append((float(r['x_cord']),float(r['y_cord'])))
	return array

def get_titles_and_cords_for_author():
	title_array = []
	cord_array = []
	ids = authors.find_one({"name": "Fridtjof Nansen"},{'book_ids': 1, 'city_ids': 1})
	book_result = books.find({'_id': {'$in': ids["book_ids"] }}, {'title': 1, 'city_ids': 1})
	city_result = cities.find({'_id': {'$in': ids['city_ids'] }},{'x_cord': 1, 'y_cord': 1})

	for t in book_result:
		title_array.append(t['title'])

	for cords in city_result:
		cord_array.append((float(cords['x_cord']),float(cords['y_cord'])))

	r_dict = get_titles_and_cords_for_author_to_dict(title_array, cord_array)
	print(r_dict)
	#return title_array, cord_array


def get_titles_and_cords_for_author_to_dict(title_array, cord_array):
    r_dict = {}
    r_dict["titles"] = []
    r_dict["cords"] = []
    for t in title_array:
        r_dict["titles"].append(t[0])
        for x,y in zip((t[1]),(t[2])):
            r_dict["cords"].append((float(x),float(y)))
    return r_dict

def get_titles_for_city1():
	books_docs = []
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
			    	'as': books_docs
			    }
		}
	])

get_titles_and_cords_for_author()
	