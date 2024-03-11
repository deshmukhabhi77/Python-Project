import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                        port = '3306', 
                        user = 'root', 
                        password = '9098',
                        database = 'pythontest')
        query='create table if not exists user(userID int primary key, username varchar(200), phone varchar(12))'


        cur = self.con.cursor()
        cur.execute(query)
        print('created')

    def insert_user(self,userid, username, phone):
        query = "insert into user(userId,username,phone)values({},'{}','{}')".format(userid, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user save to Database")


#fetchall

    def fetch_all(self):
       query = "select * from user"
       cur=self.con.cursor()
       cur.execute(query)
       for row in cur:
            print("User Id : ",row[0])
            print("User Name : ",row[1])
            print("User Phone : ",row[2])
            print()
            print()

    def delete_user(self, userid):
        query="delete from user where userID ={}".format(userid)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("UserId Daleted !!!")

    
    def update_user(self, userId, newName, newPhone):
        query = "update user set userId = '{}',userName = '{}'wher userPhone={}".format(userId, newName,newPhone)
        print(query)
        cur =self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
        

helper = DBHelper()
#helper.insert_user(int(input("Enter New UserId:")),input("Enter Username: "),int(input("Enter user phone number:")))
#helper.delete_user(int(input("Enter UserID You want to Delete: ")))
#helper.fetch_all()
helper.update_user(1234, 'siraj','9922868543')





 