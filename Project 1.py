import pyodbc as odbc
import csv

conn_str = (
    r'Driver=SQL Server;' +
    r'Server=HARIKA-THINKPAD\SQLEXPRESS;' +
    r'Database=NYCTaxi;' +
    r'Trusted_Connection=yes;'
)

def sql_statement(sql_st, file_name):
    conn = odbc.connect(conn_str)
    with conn.cursor() as cursor:
    # Read data from database
       cursor.execute(sql_st)
    # Fetch all rows
       columns = [desc[0] for desc in cursor.description]
       rows = cursor.fetchall()
       for row in rows:
            print(row)

    c = csv.writer(open(file_name,"w"))
    c.writerows(rows)
    conn.close()
sql1 = """
SELECT 
    e.EDept_Id,
    d.Dept_name,
    AVG(e.Emp_Sal) AS avg_salary
FROM 
    EMPLOYEE e
JOIN 
    emp_department d ON e.EDept_Id = d.Dept_id
GROUP BY 
    e.EDept_Id, d.Dept_name;
"""
sql2= """
    	select emp_id,
      count(emp_id) as number_of_employees
	  from employee
	  group by Emp_ID
"""
sql3="""
SELECT 
    e.EDept_Id,
    d.Dept_name,
    sum(e.Emp_Sal) AS sum_salary
FROM 
    EMPLOYEE e
JOIN 
    emp_department d ON e.EDept_Id = d.Dept_id
GROUP BY 
    e.EDept_Id, d.Dept_name;
    """
sql4="""
select emp_zip,
      count(emp_id) as number_of_employees
	  from employee
	  group by Emp_Zip
	  """

sql_statement(sql1, "gwpython1.csv")
sql_statement(sql2,"gwpython2.csv")
sql_statement(sql3,"gwpython3.csv")
sql_statement(sql4,"gwpython4.csv")