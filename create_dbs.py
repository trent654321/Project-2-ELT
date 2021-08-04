import sqlalchemy
from models import covid_data
from models import countries
from models import Base
from sqlalchemy import create_engine
from config import db_path

engine = create_engine(db_path, echo=True)
Base.metadata.create_all(engine)