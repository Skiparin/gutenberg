import os, sys
import time
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from mongo_queries import get_titles_for_city, get_cities_for_title, get_titles_and_cords_for_author

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

temp_time = 0

print("get_titles_for_city")
for i in city_array:
	start = time.time()
	get_titles_for_city(i)
	end = time.time()
	sample_time = end - start
	temp_time += sample_time
	
print(temp_time/10)
temp_time = 0

print("get_cities_for_title")
for i in title_array:
	start = time.time()
	get_cities_for_title(i)
	end = time.time()
	sample_time = end - start
	temp_time += sample_time
	
print(temp_time/10)
temp_time = 0

print("get_titles_and_cords_for_author")
for i in authors_array:
	start = time.time()
	get_titles_and_cords_for_author(i)
	end = time.time()
	sample_time = end - start
	temp_time += sample_time
	
print(temp_time/10)
temp_time = 0