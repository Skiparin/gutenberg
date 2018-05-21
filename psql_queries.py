from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

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


def create_session():
    Session = sessionmaker(bind=db_connect())
    session = Session()
    return session

def get_titles_for_city(city):
    engine = db_connect()
    conn = engine.connect()
    result = conn.execute(text("""
        select b.title, a.name
        from books b, authors a, cities c,
        books_authors ba, books_cities bc
        where c.name = :city_name and
        b.id = ba.book_id and
        ba.author_id = a.id and
        c.id = bc.city_id and
        bc.book_id = b.id;"""), city_name=city)
    return result

def get_cities_for_title(title):
    engine = db_connect()
    conn = engine.connect()
    result = conn.execute(text("""
        select c.x_cord, c.y_cord from
        cities c, books b, books_cities bc
        where b.title = :title and
        b.id = bc.book_id and
        bc.city_id = c.id;"""), title=title)
    print(result)
    print("result")
    array = []
    for r in result:
        print(r)
        print("r")
        array.append((r[0],r[1]))
    return result

def get_titles_and_cords_for_author(author):
    engine = db_connect()
    conn = engine.connect()
    result = conn.execute(text("""
        select b.title, c.x_cord, c.y_cord
        from books b, authors a, cities c,
        books_authors ba, books_cities bc
        where a.name = :author and
        a.id = ba.author_id and
        ba.book_id = b.id and
        b.id = bc.book_id and
        bc.city_id = c.id;"""), author=author)
    return result


def get_title_for_cords(x,y,r):
    engine = db_connect()
    conn = engine.connect()
    result = conn.execute(text("""
        select b.title, c.name 
        from books b, cities c, books_cities bc
        where circle'((:x,:y), :r)' @> point(x_cord,y_cord) and
        c.id = bc.city_id and
        bc.book_id = b.id;"""), x=x,y=y,r=r)
    return result




