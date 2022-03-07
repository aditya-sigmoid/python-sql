import psycopg2
import logging
from question1 import query_run,list_to_xlsx,make_connection_to_db

# Task 2
    # Write a python program to list the Total compensation given till his/her last date
    # or till now of all the employees till date in a xlsx file.
    # columns required: Emp Name, Emp No, Dept Name, Total Compensation, Months Spent in Organization

if __name__ == "__main__" :

    cursor=make_connection_to_db()
    # query to solve the question
    update_end_date = "update jobhist set enddate=current_date where enddate is null;"
    # query to solve the question

    select_query = "SELECT  emp.ename, jh.empno, dept.deptno,dept.dname, round((jh.enddate - jh.startdate)/30) * jh.sal as total_compensation," \
                   " round((enddate - startdate)/30) as emp_month_spent " \
                   "from jobhist as jh inner join emp on (jh.empno = emp.empno) inner join dept on (jh.deptno = dept.deptno);"
    query = update_end_date+select_query
    path = "/Users/adityagupta/PycharmProjects/python-sql/answers/ques2.xlsx"
    list_to_xlsx(query_run(query), path)



