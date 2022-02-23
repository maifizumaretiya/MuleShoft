import sqlite3

con = sqlite3.connect("movie.db")
# con.execute('''create table movies(name,actor text,actress text,director text,released int)''')
print("Create DataBase")


# con.execute("insert into movies(name,actor,actress,director,released) values('Chennai Express','Sharukh khan','Alia Bhatt','Sajid Nadidvala',2015)")
# con.commit()
# print("Insert Record Successfully")
def showdata():
    data = con.execute("select * from movies")
    for row in data:
        print("Movie Name : {}".format(row[0]))
        print("Movie Actor : {}".format(row[1]))
        print("Movie Actress : {}".format(row[2]))
        print("Movie Director : {}".format(row[3]))
        print("Movie Release : {}".format(row[4]))

# showdata()