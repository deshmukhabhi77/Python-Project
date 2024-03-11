from DBhelper import DBHelper

def main():

    while True:
        print("press one to insert new user")
        print("press two to display all user")
        print("press three to delete user")
        print("press four to update user")
        print("press five to exite programm")
        print()
        try:
            choise = int(input())
            if (choise ==1):
                pass
            elif choise ==2:
                pass
            elif choise ==3:
                pass
            elif choise ==4:
                pass
            elif choise ==5:
                break
            else:
                print("invalid input try again!!")
        except Exception as e:
            print(e)
            print("Invalid detail")