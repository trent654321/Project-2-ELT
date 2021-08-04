import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import db_path
from models import covid_data
from models import countries
from models import Base

engine = create_engine(db_path, echo=True)

def populate_dbs():
	#this populates the selected colums into the databases.
	Session = sessionmaker(engine)
	"""
	with Session() as s:
		s.add(testObject)
		s.commit()
	"""
	df = pd.read_csv("data/owid-covid-data.csv")
	with Session() as s:
		for i in df.index:
			iso_code = df['iso_code'][i]
			continent = df['continent'][i]
			location =  df['location'][i]
			date = df['date'][i]
			total_cases = df['total_cases'][i]
			new_cases = df['new_cases'][i]
			total_deaths = df['total_deaths'][i]
			new_deaths = df['new_deaths'][i]
			icu_patients = df['icu_patients'][i]
			hosp_patients = df['hosp_patients'][i]
			new_tests = df['new_tests'][i]
			total_tests = df['total_tests'][i]
			total_vaccinations = df['total_vaccinations'][i]
			people_vaccinated = df['people_vaccinated'][i]
			people_fully_vaccinated = df['people_fully_vaccinated'][i]
			new_vaccinations = df['new_vaccinations'][i]
			population = df['population'][i]

			row = covid_data(iso_code=iso_code, continent=continent,location=location,date=date,total_cases=total_cases,new_cases=new_cases,total_deaths=total_deaths,new_deaths=new_deaths,\
				icu_patients=icu_patients,hosp_patients=hosp_patients,new_tests=new_tests,total_tests=total_tests,total_vaccinations=total_vaccinations,people_vaccinated=people_vaccinated,\
				people_fully_vaccinated=people_fully_vaccinated,new_vaccinations=new_vaccinations,population=population)
			s.add(row)
		s.commit()

	df = pd.read_csv("data/country.csv")
	with Session() as s:
		for i in df.index:
			CountryCode = df['CountryCode'][i]
			ShortName = df['ShortName'][i]
			TableName = df['TableName'][i]
			LongName = df['LongName'][i]
			Alpha2Code = df['Alpha2Code'][i]
			CurrencyUnit = df['CurrencyUnit'][i]
			Region = df['Region'][i]
			IncomeGroup	= df['IncomeGroup'][i]
			Wb2Code	= df['Wb2Code'][i]
			row = countries(countrycode=CountryCode,ShortName=ShortName,TableName=TableName,LongName=LongName,Alpha2Code=Alpha2Code,CurrencyUnit=CurrencyUnit,Region=Region,incomegroup=IncomeGroup,Wb2Code=Wb2Code)
			s.add(row)
		s.commit()

if __name__ == "__main__":
	populate_dbs()