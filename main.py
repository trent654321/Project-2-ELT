import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from config import db_path

engine = create_engine(db_path)

def main():

	df = pd.read_csv("data/owid-covid-data.csv")
	print(df.describe())
	#df.to_sql('covid_data', engine)

if __name__ == "__main__":
	main()

