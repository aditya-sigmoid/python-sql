import pandas as pd

if __name__=="__main__":
    path="ques2.xlsx"
    df=pd.read_excel(path)
    path1="/Users/adityagupta/PycharmProjects/python-sql/answers/ques4.xlsx"

    # group dataframe by deptno and dname and add total_compensation
    grp_df = df.groupby(["deptno", "dname"]).agg({"total_compensation": sum}).reset_index().rename(columns={"deptno": "Dept No", "dname": "Dept Name", "total_compensation": "Compensation"})
    # Put it back to data in xlsx format named task_4.xlsx
    grp_df.to_excel(path1, header=True, index=False)