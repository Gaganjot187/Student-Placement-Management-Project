from database import get_connection

def add_student():
    Roll_no=int(input("Enter your roll no:"))
    Name=input("Enter your name:")
    Email=input("Enter your email:")
    Phone_no=int(input("Enter your phone-no:"))
    Course=input("Enter your course name:")
    CGPA=float(input("Enter your cgpa:"))
    Skills=input("Enter your skills:")
   
    
    conn=get_connection()
    cursor=conn.cursor()

    query="""INSERT INTO student(Roll_no,Name,Email,Phone_no,Course,CGPA,Skills)
    VALUES(%s,%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(query,(Roll_no,Name,Email,Phone_no,Course,CGPA,Skills))

    conn.commit()
    cursor.close()
    conn.close()

    
def view_students():
    conn=get_connection()
    cursor=conn.cursor()
    
    query="SELECT *FROM Student"

    cursor.execute(query)
    students=cursor.fetchall()

    for stu in students:
        print(stu)
        
    conn.commit()

    cursor.close()
    conn.close()

        
def search_student(roll_no):
    conn=get_connection()
    cursor=conn.cursor()
    
    query="SELECT *FROM Student WHERE Roll_no=%s"

    cursor.execute(query,(roll_no,))
    student=cursor.fetchone()
    print(student)
    
    conn.commit()

    cursor.close()
    conn.close()


def update_student(roll_no):
    conn=get_connection()
    cursor=conn.cursor()
    
    ans=input("What you want to update:").lower()
    if ans=="email" or ans=="e-mail":
        new_email=input("Enter your new email:")

        query="UPDATE Student SET Email=%s WHERE Roll_no=%s"
        cursor.execute(query,(new_email,roll_no))
        
    elif ans=="phone_no" or ans=="phoneno" or ans=="phone-no":
        new_phone=int(input("Enter your new phone-no:"))

        query="UPDATE Student SET Phone_no=%s WHERE Roll_no=%s"
        cursor.execute(query,(new_phone,roll_no))

    conn.commit()

    cursor.close()
    conn.close()
    

def delete_student(roll_no):
    conn=get_connection()
    cursor=conn.cursor()
    
    query="DELETE FROM Student WHERE roll_no=%s"
    cursor.execute(query,(roll_no,))

    if cursor.rowcount==1:
        print("Student deleted successfully")
    else:
        print("Student doesn't exist")
        
    conn.commit()

    cursor.close()
    conn.close()
    














    