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
        select b.title, array_agg(a.name)
        from books b, authors a, cities c,
        books_authors ba, books_cities bc
        where c.name = :city_name and
        b.id = ba.book_id and
        ba.author_id = a.id and
        c.id = bc.city_id and
        bc.book_id = b.id
        group by b.title;"""), city_name=city)
    array = []
    for r in result:
        temp_array = [r[0], r[1]]
        array.append(temp_array)
    return array

def get_cities_for_title(title):
    engine = db_connect()
    conn = engine.connect()
    result = conn.execute(text("""
        select c.x_cord, c.y_cord from
        cities c, books b, books_cities bc
        where b.title = :title and
        b.id = bc.book_id and
        bc.city_id = c.id;"""), title=title)
    array = []
    for r in result:
        array.append((float(r[0]),float(r[1])))
    return array

def get_titles_and_cords_for_author(author):
    engine = db_connect()
    conn = engine.connect()
    result = conn.execute(text("""
        select b.title, array_agg(c.x_cord), array_agg(c.y_cord)
        from books b, authors a, cities c,
        books_authors ba, books_cities bc
        where a.name = :author and
        a.id = ba.author_id and
        ba.book_id = b.id and
        b.id = bc.book_id and
        bc.city_id = c.id
        group by b.title;"""), author=author)
    r_dict = {}
    r_dict["titles"] = []
    r_dict["cords"] = []
    for r in result:
        r_dict["titles"].append(r[0])
        for x,y in zip((r[1]),(r[2])):
            r_dict["cords"].append((float(x),float(y)))
    return r_dict


def get_title_for_cords(x,y,r):
    engine = db_connect()
    conn = engine.connect()
    result = conn.execute(text("""
        select b.title 
        from books b, cities c, books_cities bc
        where circle'(("""+ x + "," + y + ")," + r + """)' @> point(x_cord,y_cord) and
        c.id = bc.city_id and
        bc.book_id = b.id;"""))
    array = []
    for r in result:
        array.append(r[0])
    return array




