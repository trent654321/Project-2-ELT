import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from config import db_path

engine = create_engine(db_path)

def main():

	df = pd.read_csv("data/country.csv")
	print(df.dtypes)

if __name__ == "__main__":
	main()

