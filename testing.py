from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import unittest
from unittest.mock import patch
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

    def getCityCord(city):
        engine = db_connect()
        conn = engine.connect()
        result = conn.execute(text("select x_cord, y_cord from cities where city_name = '"+city+"'"))
        for xcord,y_cord in result:
            a = [xcord,y_cord]
        return a
    def getTitleAuthor():
        engine = db_connect()
        conn = engine.connect()
        result = conn.execute(text("select title,author from books limit 10"))
        for title,author in result:
            a = [title,author]
        return a
    def getTitleAuthorByCity(city_name):
        engine = db_connect()
        conn = engine.connect()
        result = conn.execute(text("select title,author from books b, book_vectors v where v.vector @@ to_tsquery(:city) and b.id = v.id"), city=city_name)
        for title,author in result:
            a = [title,author]
        return a
def testMetode():
    result = conn.execute(text("SELECT 1"))
    print(result)



class TestTest(unittest.TestCase):

    @patch('Testing.funny.getVariable',return_value=3)
    def test_mock(self,getVariable):
        self.assertEqual(getVariable(), 3)

    def test_con(self):
        engine = db_connect()
        conn = engine.connect()
    def test_CityCord(self):
        result = database.getCityCord("London")
        self.assertEqual(float(result[0]),42.98339)
        self.assertEqual(float(result[1]),-81.23304)
    def test_CityTitleAuthor(self):
        #result = solr_query.city_name("Denmark")
        #self.assertEqual(result[1][0], "The Comic History Of England")
        #self.assertEqual(result[1][1], "Gilbert Abbott A'Beckett")
        result = database.getTitleAuthorByCity("Odense")
        print(result[0])
        self.assertEqual(result[0],"The 2000 CIA World Factbook\n")
    def test_AuthorTitle(self):
        result = database.getTitleAuthor()
        self.assertEqual(result[0],"Alaska Days with John Muir\n")
    """
    def test_solr(self):
        result = solr_query.city_name("Denmark")
        self.assertEqual(result[0][0], "A New Voyage Round the World in the Years 1823, 24, 25, and 26. Vol. 1")
        self.assertEqual(result[1][0], "Otto von Kotzebue")
    """



if __name__ == '__main__':
    unittest.main()
