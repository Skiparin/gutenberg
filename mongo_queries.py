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
	city_result = cities.find_one({'_id': {'$in': ids['city_ids'] }},{'location': 1})
	array = []
	for cords in city_result:
		array.append(cords)
	print(array)
	return array

def get_titles_and_cords_for_author(author):
	title_array = []
	cord_array = []
	ids = authors.find_one({"name": author},{'book_ids': 1, 'city_ids': 1})
	book_result = books.find({'_id': {'$in': ids["book_ids"] }}, {'title': 1, 'city_ids': 1})
	city_result = cities.find({'_id': {'$in': ids['city_ids'] }},{'coordinates': 1})
	for t in book_result:
		title_array.append(t['title'])
	for cords in city_result:
		cord_array.append(cords)
	r_dict = get_titles_and_cords_for_author_to_dict(title_array, cord_array)
	print(r_dict)
	return r_dict

def get_title_for_cords():
	book_array = []
	location_array = []
	ids = cities.find({'_id': {'$geoNear': {'$center': {'x_cord': 50, 'y_cord': 20}}}}, {'book_ids': 1})
	for book in ids:
		location_array.append(book['book_ids'])
	print(location_array)
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
	for cords in cord_array:
		r_dict["cords"].append(cords)
	return r_dict

get_cities_for_title("Danger at the Drawbridge")
#get_titles_and_cords_for_author("Max Simon Nordau")