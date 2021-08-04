# Project-2-ELT
Project created for Data Analytics and Visualization Bootcamp, Project 2 - Extract, Load and Transform
Created by Trent McNabb and Hinda Filali
Project Proposal:
To use extract data from two sources, transform it and load it into a Postgresql database so that we can query the two sources together to examine the impact of economic indicators on covid cases.
Data sources:
Our World in Data Covid Cases Data:
https://ourworldindata.org/coronavirus-data
World Development Indicators:
https://databank.worldbank.org/source/world-development-indicators#
Downloaded from: https://www.kaggle.com/worldbank/world-development-indicators

This project contains:
README.md       with detailed explanation of project and layout
/data/          A folder which conatins the data sets and the output csv. These aren't stored on the .git, they are stored at https://drive.google.com/drive/folders/1-9SIwBdD7F-gcepIP2xXOw91hC12X89v?usp=sharing
main.py			the file that contains the code which cleans the data and inserts it into the database
config.py		a file that contains the database path to create the sqlalchemy engine
create_dbs.py	a file that contains the code that created the tables in the database
models.py		a file that contains the layout of the tables to be createed using create_dbs.py
query.sql 		a file that contains the sql query that joins the tables
/data/output.csv		a file tha contains the results of the query, can be found at https://drive.google.com/drive/folders/1-9SIwBdD7F-gcepIP2xXOw91hC12X89v?usp=sharing

Technical report:
Initailly created a schema.sql file, and used PGAdmin 4 to load the CSV into Postgres.
Decided to go a different direction, and used sqlalchemy to create the tables and populate them. In this case, we chose not to add multiple columns of the data, as it wasn't necessary for our project. At his stage, we could also confirm or correct data types or data inconsistencies.
The difficulties using PGAdmin included choosing the right length for varchar data, but SQLAlchemy resolved that issue easily.
There was an issue with making the column names contain capital letter, and we had to modify the code the take the capital letters out of the variables columns that we were using.
Using pandas and sql alchemy made choosing data types for the database, and identifying columns that contained data that wasn't the expected type.
The most important thing was choosing the correct primay key for the tables. for the covid data, the primary key was two column, the country and the date.
We were able to query the total cases and link it to income group. There was third table of data (indicators.csv from the World Bank Dataset) that would have allowed us to delve more deeply.

