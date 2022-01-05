
import pickle
import mysql.connector

class Database():
    def __init__(self):
        self.db=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='1234',
            database='Face'

        )
        self.mycursor = self.db.cursor()

# mycursor.execute("CREATE TABLE Face (name VARCHAR(50),image BLOB,facecode BLOB,personID int PRIMARY KEY AUTO_INCREMENT)")
    def insert(self,image,fcd):
        self.mycursor.execute("INSERT INTO Face (image,facecode) Values (%s,%s)",(image,fcd))
        self.db.commit()



    def fetchcode(self):
        list=[]
        self.mycursor.execute("SELECT facecode FROM Face ")
        code = self.mycursor.fetchall()
        for element in code:
            Cov=pickle.loads(element[0])
            list.append(Cov)
        return list



    def fetchID(self):
        self.mycursor.execute("SELECT personID FROM Face")
        code = self.mycursor.fetchall()
        if len(code)==0:
            return 0

        return code[-1][0]



    def DeleteAll(self):
        self.mycursor.execute("DELETE FROM Face")
        self.db.commit()


    def FindName(self,id):
        self.mycursor.execute("SELECT name FROM Face WHERE facecode = %s",(id,))
        code = self.mycursor.fetchall()

        return code[0][0]


    def Drop(self):
        self.mycursor.execute("DROP TABLE Face")

    def Create(self):
        self.mycursor.execute("CREATE TABLE face (name VARCHAR(50),image BLOB,facecode BLOB,personID int PRIMARY KEY "
                              "AUTO_INCREMENT, time VARCHAR(50))")

    def Clear(self):
        self.mycursor.execute("UPDATE Face SET name = NULL")
        self.db.commit()


    def ID_reset(self):
        self.mycursor.execute("ALTER Face personID AUTO_INCREMENT = 0")







#p=Database()
#p.Clear()
#p.DeleteAll()
#p.Create()
#p.Create()
