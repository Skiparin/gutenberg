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

def get_titles_for_city(city):
	book_array = []
	ids = cities.find_one({"name": city},{'book_ids': 1})
	book_result = books.find({'_id': {'$in': ids["book_ids"] }}, {'title': 1, 'authors': 1})
	for book in book_result:
		author_array = []
		author_results = authors.find({'_id': {'$in': book['authors']}})
		for author in author_results:
			author_array.append(author['name'])
		temp_array = [book['title'], author_array]
		book_array.append(temp_array)
	return book_array

def get_cities_for_title(title):
	city_array = []
	ids = books.find_one({"title": title},{"city_ids":1})
	city_result = cities.find({'_id': {'$in': ids['city_ids'] }},{'x_cord': 1, 'y_cord': 1})
	array = []
	for r in city_result:
		array.append((float(r['x_cord']),float(r['y_cord'])))
	return array

def get_titles_and_cords_for_author(author):
	title_array = []
	cord_array = []
	ids = authors.find_one({"name": author},{'book_ids': 1, 'city_ids': 1})
	book_result = books.find({'_id': {'$in': ids["book_ids"] }}, {'title': 1, 'city_ids': 1})
	city_result = cities.find({'_id': {'$in': ids['city_ids'] }},{'x_cord': 1, 'y_cord': 1})

	for t in book_result:
		title_array.append(t['title'])

	for cords in city_result:
		cord_array.append((float(cords['x_cord']),float(cords['y_cord'])))

	r_dict = get_titles_and_cords_for_author_to_dict(title_array, cord_array)
	return r_dict

def get_title_for_cords():
	book_array = []
	location = cities.find({'x_cord': 1, 'y_cord': 1})
	print(location)
	"""
	ids = cities.find({'_id': {'type': 'point' , ['x_cord': 50, 'y_cord': 20]}}, {'book_ids': 1})
	book_result = books.find({'_id': {'$in': ids['book_ids']}}, {'title': 1})
	for title in book_results:
		book_result.append(title['title'])
	print(book_array)
	"""

def get_titles_and_cords_for_author_to_dict(title_array, cord_array):
	r_dict = {}
	r_dict["titles"] = []
	r_dict["cords"] = []
	for t in title_array:
		r_dict["titles"].append(t)
	for x,y in cord_array:
		r_dict["cords"].append((float(x),float(y)))
	return r_dict

get_title_for_cords()