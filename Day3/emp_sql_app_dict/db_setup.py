<<<<<<< HEAD
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import Base, Employee


#db setup
engine = create_engine("sqlite:///employee_app_db.db", echo = True)

Base.metadata.create_all(engine) #creates tables

#Session for sql operations
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()# for sql ops
=======
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import Base, Employee


#db setup
engine = create_engine("sqlite:///employee_app_db.db", echo = True)

Base.metadata.create_all(engine) #creates tables

#Session for sql operations
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()# for sql ops
>>>>>>> a39d113e5de6b4b6bf55bdc5b19cdb5f807b00f4
