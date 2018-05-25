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

def getBooks():
    engine = db_connect()
    conn = engine.connect()
    result = conn.execute(text("""
        COPY(SELECT id AS 'id.auto()', book AS 'book.auto()', title AS 'title.auto()' FROM books) TO '/root/temp.csv WITH (FORMAT CSV, HEADER TRUE, DELIMITER E'\t');"""))

getBooks()