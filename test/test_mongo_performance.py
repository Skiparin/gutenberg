import os, sys
import time
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from mongo_queries import get_titles_for_city, get_cities_for_title, get_titles_and_cords_for_author, get_title_for_cords

get_titles_for_city("Odense")

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

cord_array = [
[1,1,1000000],
[2,2,2000000],
[3,3,3000000],
[4,4,4000000],
[5,5,5000000],
[6,6,6000000],
[7,7,7000000],
[8,8,8000000],
[9,9,9000000],
[10,10,10000000],
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

print("get_title_for_cords")
for i in cord_array:
	start = time.time()
	get_title_for_cords(i[0],i[1],i[2])
	end = time.time()
	sample_time = end - start
	temp_time += sample_time

print(temp_time/10)
temp_time = 0