from database import get_connection

def add_company():
    Company_name=input("Enter company name:")
    Job_role=input("Enter job roles they hire:")
    Min_cgpa=float(input("Enter minimum cgpa company require:"))
    Package=float(input("Average package company provide:"))

    conn=get_connection()
    cursor=conn.cursor()

    query="""
    INSERT INTO Company(Company_name,Job_role,Min_cgpa,Package)
    VALUES(%s,%s,%s,%s)
    """
    cursor.execute(query,(Company_name,Job_role,Min_cgpa,Package))

    conn.commit()
    cursor.close()
    conn.close()

    
def search_company(name):
    conn=get_connection()
    cursor=conn.cursor()

    query="SELECT *FROM Company WHERE Company_name=%s"
    cursor.execute(query,(name,))

    result=cursor.fetchone()
    print(result)

    cursor.close()
    conn.close()

def delete_company(name):
    conn=get_connection()
    cursor=conn.cursor()

    query="DELETE FROM Company WHERE Company_name=%s"

    cursor.execute(query,(name,))
    if cursor.rowcount==1:
        print("Company deleted successfully")
    else:
        print("Company doesn't exist")

    conn.commit()
    cursor.close()
    conn.close()


    