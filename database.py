from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

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