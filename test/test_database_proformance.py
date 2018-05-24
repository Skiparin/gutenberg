import os, sys
import time
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from psql_queries import get_cities_for_title, get_titles_for_city, get_titles_and_cords_for_author, get_title_for_cords

get_cities_for_title("Denmark")
title_array = ["Danger at the Drawbridge",
"Sally Dows and Other Stories",
"Alaska Days with John Muir",
"Undine",
"Fun And Frolic",
"Missing",
"The Red Hand of Ulster",
"The Confession of a Fool",
"William Shakespeare",
"Zero Data"]

city_array = ["Dubai",
 "Sharjah",
 "Al Ain",
 "Ajman",
 "Abu Dhabi",
 "Mazar-e Sharif",
 "Kunduz",
 "Kandahar",
 "Kabul",
 "Jalalabad"
]

authors_array = [ "Max Simon Nordau",
"Lewis Carroll",
"Mildred A. Wirt",
"David Belasco",
"Antonio Colmenero de Ledesma",
"Nathaniel Hawthorne",
"J. H. MerleD'Aubigne",
"Bret Harte",
"Elizabeth Cooper",
"Harold Whetstone Johnston",
]

cord_array = [
[1,1,1],
[2,2,2],
[3,3,3],
[4,4,4],
[5,5,5],
[6,6,6],
[7,7,7],
[8,8,8],
[9,9,9],
[10,10,10],
]
time = 0

print("get_cities_for_title")
for i in title_array:
	start = time.time()
	get_cities_for_title(i)
	end = time.time()
	sample_time = end - start
	time += sample_time
	
print(time/10)
time = 0
print("get_titles_for_city")
for i in city_array:
	start = time.time()
	get_titles_for_city(i)
	end = time.time()
	sample_time = end - start
	time += sample_time
	
print(time/10)
time = 0
print("get_titles_and_cords_for_author")
for i in authors_array:
	start = time.time()
	get_titles_and_cords_for_author(i)
	end = time.time()
	sample_time = end - start
	time += sample_time
	
print(time/10)
time = 0
print("get_title_for_cords")
for i in cord_array:
	start = time.time()
	get_title_for_cords(str(i[0]),str(i[1]),str(i[2]))
	end = time.time()
	sample_time = end - start
<<<<<<< HEAD
	print("\t" + str(sample_time))
=======
	time += sample_time

print(time/10)
time = 0
>>>>>>> e50a667d32a2f4c4aba23709a24b71720ae752c0
