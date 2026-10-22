from database import get_connection

def apply_student(status="Applied"):
    conn=get_connection()
    cursor=conn.cursor()

    rollno=input("Enter roll_no:")
    companyid=input("Enter company ID:")
    app_date=input("Enter date:")

    query="""
    INSERT INTO Application(Student_id,Company_id,application_date,Status)
    VALUES
    (%s,%s,%s,%s)
    """
    cursor.execute(query,(rollno,companyid,app_date,status))

    conn.commit()

    cursor.close()
    conn.close()


def view_application():
    conn=get_connection()
    cursor=conn.cursor()

    query="SELECT *FROM Application"

    cursor.execute(query)

    app=cursor.fetchall()

    for a in app:
        print(a)
    
    cursor.close()
    conn.close()


def student_application_details():
    conn=get_connection()
    cursor=conn.cursor()

    query="""SELECT Student.Name,Company.Company_name,Company.Job_role,Application.status 
    FROM Application
    JOIN Student 
    ON Student.Roll_no=Application.Student_id
    JOIN Company
    ON Application.Company_id=Company.Company_ID
    """
    cursor.execute(query)
    result=cursor.fetchall()

    for res in result:
        print(res)
    
    cursor.close()
    conn.close()
    












    
    