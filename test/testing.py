from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import unittest
import os, sys
from unittest.mock import patch
parentPath = os.path.abspath("gutenberg")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from psql_queries import *
#import solr_query


class funny():
	var = 0
	def setVariable(a):
		var = a
	def getVariable():
		return a


def db_connect():
    """
    Connect to database where we'll save properties.
    """
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
        self.assertEqual(result[0],"The 2000 CIA World Factbook\n")

    def test_get_cities_for_title(self):
        result = database.getCitiesForTitle("Denmark")

    def test_CityCord(self):
        result = database.getCityCord("London")
        self.assertEqual(float(result[0]),42.98339)
        self.assertEqual(float(result[1]),-81.23304)


    def test_AuthorTitle(self):
        result = database.getTitleAuthor()
        self.assertEqual(result[0],"Alaska Days with John Muir\n")

    def testMetode(self):
        result = conn.execute(text("SELECT 1"))
        print(result)

    """
    def test_solr(self):
        result = solr_query.city_name("Denmark")
        self.assertEqual(result[0][0], "A New Voyage Round the World in the Years 1823, 24, 25, and 26. Vol. 1")
        self.assertEqual(result[1][0], "Otto von Kotzebue")
    """



if __name__ == '__main__':
    unittest.main()
