# Project-2-ELT
Project created for Data Analytics and Visualization Bootcamp, Project 2 - Extract, Load and Transform
Created by Trent McNabb and Hinda Filali

Data sources:
Our World in Data Covid Cases Data:
https://ourworldindata.org/coronavirus-data
World Development Indicators:
https://databank.worldbank.org/source/world-development-indicators#
Downloaded from: https://www.kaggle.com/worldbank/world-development-indicators
The dat

This project contains:
README.md       with detailed explanation of project and layout
/data/          A folder which conatins the data sets. These aren't stored on the .git, they are stored at https://drive.google.com/drive/folders/1-9SIwBdD7F-gcepIP2xXOw91hC12X89v?usp=sharing
main.py			the file that contains the code which cleans the data and inserts it into the database
config.py		a file that contains the database path to create the sqlalchemy engine
create_dbs.py	a file that contains the code that created the tables in the database
models.py		a file that contains the layout of the tables to be createed using create_dbs.py