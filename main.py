from database import get_connection

from students import add_student,view_students,search_student,update_student,delete_student
from company import add_company,search_company,delete_company
from application import apply_student,view_application,student_application_details

conn=get_connection()
print("Connected successfully")

def main():
    while True:
        print("----STUDENT PLACEMENT MANAGEMENT PROJECT----")
        print("1 Add Student")
        print("2 View Students")
        print("3 Search Student")
        print("4 Update Student")
        print("5 Delete Student")
        print("6 Add Company")
        print("7 Search Company")
        print("8 Delete Company")
        print("9 Apply Student")
        print("10 View Application")
        print("11 Student_application_details")
        print("12 Exit")

        choice=int(input("Enter your choice:"))
        if choice==1:
            add_student()
        elif choice==2:
            view_students()
        elif choice==3:
            roll_no=int(input("Enter roll_no: "))
            search_student(roll_no)
        elif choice==4:
            roll_no=int(input("Enter roll_no: "))
            update_student(roll_no)
        elif choice==5:
            roll_no=int(input("Enter roll_no: "))
            delete_student(roll_no)
        elif choice==6:
            add_company()
        elif choice==7:
            name=input("Enter company name: ")
            search_company(name)
        elif choice==8:
            name=input("Enter company name: ")
            delete_company(name)
        elif choice==9:
            apply_student()
        elif choice==10:
            view_application()
        elif choice==11:
            student_application_details()
        elif choice==12:
            print("Thank you..")
            break
        else:
            print("Invalid choice!!")
            
            
    conn.close()

main()