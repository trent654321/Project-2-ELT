import sqlalchemy
from sqlalchemy import Column, Date, Integer, Numeric, String
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import PrimaryKeyConstraint

Base = declarative_base()

class covid_data_table(Base):
	__tablename__ = "covid_data"
	loc_code = Column(String())
	continent = Column(String())
	date = Column(Date())
	__table_args__ = (
		PrimaryKeyConstraint(loc_code, date),
		{},
	)

class countries_table(Base):
	__tablename__ = "countries"
	CountryCode = Column(String(), primary_key=True)
	ShortName = Column(String())