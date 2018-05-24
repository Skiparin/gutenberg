import os, sys
import time
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from psql_queries import get_cities_for_title, get_titles_for_city, get_titles_and_cords_for_author, get_title_for_cords

print("get_cities_for_title")
for i in range(10):
	start = time.time()
	get_cities_for_title("Denmark")
	end = time.time()
	print(end - start)

print("get_titles_for_city")
for i in range(10):
	start = time.time()
	get_titles_for_city("Odense")
	end = time.time()
	print(end - start)

print("get_titles_and_cords_for_author")
for i in range(10):
	start = time.time()
	get_titles_and_cords_for_author("Hans Christian Andersen")
	end = time.time()
	print(end - start)

print("get_title_for_cords")
for i in range(10):
	start = time.time()
	get_title_for_cords(1,1,1)
	end = time.time()
	print(end - start)