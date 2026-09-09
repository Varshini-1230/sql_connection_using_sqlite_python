import psycopg2
import random
 
conn = psycopg2.connect("postgresql://neondb_owner:npg_crZG1ilA6gVf@ep-polished-lab-ay995ut1-pooler.c-5.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
cur = conn.cursor()
#cur.execute("DROP TABLE IF EXISTS students")
# Create table
def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")
    conn.commit()
    print("Table created")
 
# Add 100 students
def insert_into_table():
    cur.execute("DELETE FROM students")
 
    for i in range(1, 11):
        cur.execute(
            "INSERT INTO students VALUES (%s, %s, %s)",
            (i, f"Student{i}", random.randint(18, 30))
    )
 
    conn.commit()
    print("Inserted into table")
 
def delete_one_row():
    student_id = int(input("Enter student ID to delete: "))

    
    cur.execute(
            "DELETE FROM students WHERE id = %s",
            (student_id,)
    )
    conn.commit()
    

    
choice=int(input("""Enter your choice:
                 1.create table
                 2.insert into table
                 3.delete row
                 4.do nothing
                 Enter your choice:"""))

if choice==1:
    create_table()
elif choice==2:
    insert_into_table()
elif choice ==3:
    delete_one_row()
elif choice ==4:
    pass
cur.execute("select * from students")
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()