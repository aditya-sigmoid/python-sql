import psycopg2
import pandas as pd
import logging

# Task 1
# Write a Python program to list employee numbers,
# names and their managers and save in a xlsx file.

def make_connection_to_db():
    conn_string = "host='localhost' dbname='department' user='postgres' password='password'"
    conn=psycopg2.connect(conn_string)
    cursor=conn.cursor()
    return cursor

def query_run(query):
    cursor=make_connection_to_db()
    try:
        cursor.execute(query)  # this will execute the query
        logging.debug(f" query executed on cursor - {cursor}")
    except:
        logging.error("failed to fetch cursor from database")
    # extracting all data from cursor
    query_result=cursor.fetchall()
    # inserting header in query result
    query_result.insert(0, [cursor.description[i].name for i in range(len(cursor.description))])
    #print(query_result)
    return query_result

def list_to_xlsx(data,path):
    # creating dataframe from data (list_type)
    df=pd.DataFrame(data)
    try:
        # adding data to excel file
        df.to_excel(path,header=False,index=False)
        logging.info(f"Dataframe converted to excel stored in location -{path}")
    except:
        logging.error(f"Unable to convert dataframe to excel in location - {path}")

if __name__=="__main__":

    # query to solve the question
    cursor=make_connection_to_db()
    query = "select e1.empno,e1.ename as emp_name,e2.ename as mgr_name from emp as e1 INNER JOIN emp as e2 on (e1.mgr=e2.empno)"
    data=query_run(query)
    path = "/Users/adityagupta/PycharmProjects/python-sql/answers/ques1.xlsx"
    list_to_xlsx(data,path)

