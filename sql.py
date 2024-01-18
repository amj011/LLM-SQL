import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),SECTION VARCHAR(25), MARKS INT);

"""
cursor.execute(table_info)

cursor.execute('''Insert Into Student values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into Student values('Krish3','Data Science','A',70)''')
cursor.execute('''Insert Into Student values('Krishna Krishna','Data Science','A',20)''')
cursor.execute('''Insert Into Student values('Vikas','DEVOPS','A',94)''')
cursor.execute('''Insert Into Student values('Krishna','DEVOPS','A',50)''')

print("The inserted records aree")

data = cursor.execute('''SELECT * from STUDENT''')


for row in data:
    print(row)


connection.commit()
connection.close()