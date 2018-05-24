import os, sys
import time
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from psql_queries import get_cities_for_title, get_titles_for_city, get_titles_and_cords_for_author, get_title_for_cords

start = time.time()
timeit.timeit('get_cities_for_title("Denmark")', number=10)
end = time.time()
print(end - start)