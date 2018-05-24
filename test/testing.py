from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import unittest
import os, sys
from unittest.mock import patch

parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from psql_queries import get_cities_for_title, get_titles_for_city, get_titles_and_cords_for_author, get_title_for_cords


class funny():
	var = 0
	def setVariable(a):
		var = a
	def getVariable():
		return a

"""
Connect to database where we'll save properties.
"""
def db_connect():
    return create_engine(URL(**{
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '54320',
    'username': 'book',
    'password': 'secret',
    'database': 'book'
}))

class database():
    def getTitlesForCity(city):
        result = get_titles_for_city(city)
        for title, author in result:
            a = [title, author]
            return a

    def getCitiesForTitle(title):
        result = get_cities_for_title(title)
        for xcord,ycord in result:
            a = [xcord,ycord]
        return a

    def getTitlesAndCordsForAuthor(author):
        result = get_title_and_cords_for_author(author)
        for title,xcord,y_cord in result:
            a = [title,xcord,ycord]
            return a

    def getTitleForCords(x,y,r):
        result = get_title_for_cords(x,y,r)
        for title in result:
            a = [title]
            return a

class TestTest(unittest.TestCase):

    @patch('Testing.funny.getVariable',return_value=3)
    def test_mock(self,getVariable):
        self.assertEqual(getVariable(), 3)

    def test_con(self):
        engine = db_connect()
        conn = engine.connect()

    def test_get_titles_for_city(self):
        result = database.getTitlesForCity("Odense")
        self.assertEqual(result[0],"A Danish Parsonage")
        self.assertEqual(result[1],"['John Fulford Vicary']")

        result = database.getTitlesForCity("London")
        self.assertEqual(result[0],"1000 Mythological Characters Briefly Described Adapted to Private Schools, High Schools and Academies")
        self.assertEqual(result[1],"['Edward S. Ellis']")

    def test_get_cities_for_title(self):
        result = database.getCitiesForTitle("London")
        self.assertEqual(float(result[0]),42.98339)
        self.assertEqual(float(result[1]),-81.23304)

    def test_get_titles_for_cords(self):
        result = database.getTitleForCords(25,50,0.5)
        self.assertEqual(result[0],"Southern Arabia")
        self.assertEqual(result[5],"The Book of the Thousand Nights and a Night, Volume 1")

if __name__ == '__main__':
    unittest.main()
