from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import postgres_copy

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

def getBooks():
    engine = db_connect()
    conn = engine.connect()
    Session = sessionmaker(bind=db_connect())
    session = Session()
    # Export a CSV containing all Queen albums
    query = session.query("id, name, x_cord, y_cord FROM cities")
    with open('/root/cities.csv', 'w') as fp:
        postgres_copy.copy_to(query, fp, engine, format='csv', header=True)
        print(count)
    print("complete")

getBooks()