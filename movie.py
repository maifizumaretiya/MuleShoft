import sqlite3
import conn
con = sqlite3.connect("movie.db")
class movie:
    def __init__(self):
        pass
        

    def insert():
         name = input("Enter Movie Name : ")
         actor = input("Enter Actor Name : ")
         actress = input("Enter Actress Name : ")
         director = input("Enter Director Name : ")
         released = input("Enter Year Of Release : ")
         con.execute("insert into movies(name,actor,actress,director,released)values(?,?,?,?,?)",(name,actor,actress,director,released))
         con.commit()

    def showdata():
        data = con.execute("select * from movies")
        for row in data:
            print("Movie Name : {}".format(row[0]))
            print("Movie Actor : {}".format(row[1]))
            print("Movie Actress : {}".format(row[2]))
            print("Movie Director : {}".format(row[3]))
            print("Movie Release : {}".format(row[4]))
            print("=============================================")

movie1 = movie
movie1.insert()
movie1.showdata()