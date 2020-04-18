import sqlite3

db = sqlite3.connect("STC_DB.db")
cursor = db.cursor()
def user():
    try:
    
        cursor.execute("CREATE TABLE USER(password varchar(15))")
        print("user table create sucessfull!")
        db.commit()

    except:
        print("User Table already added!")


def teachers():
    try:
        cursor.execute("""CREATE TABLE teacher(first_name varchar(20),
                                                full_name varchar(50),
                                                NIC_NO varchar(12),
                                                Date_Of_Birth varchar(20),
                                                Addmision_date varchar(20),
                                                Address varchar(50),
                                                Contacts int(26),
                                                email varchar(40))""")
        print("teachers table create sucessfull!")
        
        db.commit()
    except:
        print("teacher table already added!")


def students():
    try:    
        cursor.execute("""CREATE TABLE STUDENTS(first_name varchar(30),
                                                full_name varchar(50),
                                                NIC_NO varchar(12),
                                                Date_of_birth varchar(20),
                                                Addmission_no int(6),
                                                Addmited_date varchar(20),
                                                Address varchar(40),
                                                Contacts int(30),
                                                p_name varchar(50))""")
        print("students table create sucessfull!!")
        db.commit()

    except:
        print("student table already added!")



db.close()
user()
teachers()
students()








        
