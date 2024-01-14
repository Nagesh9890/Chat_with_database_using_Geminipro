import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')
cursor.execute('''Insert Into STUDENT values('Alice','Data Science','B',75)''')
cursor.execute('''Insert Into STUDENT values('Bob','Data Science','C',64)''')
cursor.execute('''Insert Into STUDENT values('Charlie','Data Science','A',92)''')
cursor.execute('''Insert Into STUDENT values('David','DEVOPS','B',60)''')
cursor.execute('''Insert Into STUDENT values('Eva','DEVOPS','A',80)''')
cursor.execute('''Insert Into STUDENT values('Frank','Data Science','A',88)''')
cursor.execute('''Insert Into STUDENT values('Grace','Data Science','B',70)''')
cursor.execute('''Insert Into STUDENT values('Henry','Data Science','C',55)''')
cursor.execute('''Insert Into STUDENT values('Isla','DEVOPS','B',45)''')
cursor.execute('''Insert Into STUDENT values('Jack','DEVOPS','A',85)''')
cursor.execute('''Insert Into STUDENT values('Kathy','Data Science','A',95)''')
cursor.execute('''Insert Into STUDENT values('Leo','Data Science','C',50)''')
cursor.execute('''Insert Into STUDENT values('Mia','Data Science','B',78)''')
cursor.execute('''Insert Into STUDENT values('Nora','DEVOPS','A',90)''')
cursor.execute('''Insert Into STUDENT values('Oscar','DEVOPS','B',65)''')
cursor.execute('''Insert Into STUDENT values('Pam','Data Science','C',58)''')
cursor.execute('''Insert Into STUDENT values('Quinn','Data Science','A',93)''')
cursor.execute('''Insert Into STUDENT values('Rachel','DEVOPS','C',40)''')
cursor.execute('''Insert Into STUDENT values('Steve','DEVOPS','A',82)''')
cursor.execute('''Insert Into STUDENT values('Tina','Data Science','B',76)''')


## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()
