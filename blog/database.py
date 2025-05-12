# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine  # Used to create a connection to the database
from sqlalchemy.ext.declarative import declarative_base  # Base class for defining ORM models
from sqlalchemy.orm import sessionmaker  # Used to create a session factory for database interactions

# Define the database connection URL
# Here, we are using SQLite as the database, and the database file is named 'blog.db'
# The 'sqlite:///' prefix indicates that this is a SQLite database
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# Create the database engine
# The engine is responsible for managing the connection to the database
# 'connect_args' is specific to SQLite and allows multiple threads to access the database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# Create a session factory
# A session is used to interact with the database (e.g., querying, adding, or updating data)
# - 'bind=engine': Binds the session to the database engine
# - 'autocommit=False': Disables automatic commits; changes must be explicitly committed
# - 'autoflush=False': Disables automatic flushing of changes to the database
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Create a base class for ORM models
# All database models will inherit from this base class
# It provides metadata and functionality for defining database tables and relationships
Base = declarative_base()