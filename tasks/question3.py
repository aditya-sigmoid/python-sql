import psycopg2
import pandas.io.sql as sql
import pandasql as ps
import pandas as pd
from sqlalchemy import create_engine
import logging
from question1 import make_connection_to_db,query_run,list_to_xlsx
# task 3
# Read and upload the above xlsx in 2) into a new table in the Postgres DB

def task3():
    try:
        engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/department")
        print(engine)
        logging.debug(f"Successfully create engine  - {engine}")
    except:
        print("hello")
        logging.error("failed to create engine")

    with pd.ExcelFile("ques2.xlsx") as xls:
        df = pd.read_excel(xls)
    try:
        df.to_sql(name="task2_table", con=engine, if_exists="replace", index=False)
        logging.debug("table is created from the excel file and data successfully uploaded")
    except:
        logging.debug("Exception occurred while uploading data to table")


if __name__== "__main__":
    task3()



