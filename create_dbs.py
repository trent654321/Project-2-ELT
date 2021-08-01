import sqlalchemy
from models import covid_data_table
from models import countries_table
from models import Base
from sqlalchemy import create_engine
from config import db_path

engine = create_engine(db_path, echo=True)
Base.metadata.create_all(engine)