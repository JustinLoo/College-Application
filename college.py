import mysql.connector as mysql
#import sql


db = mysql.connect(host = "localhost", user = "root", password = "", database = "college")
#connect to mySQL database. The password is left blank because root has no default password set at the moment
commandHandler = db.cursor(buffered = True)
#this makes it so that it will nto lag

#if it is admin:
def admin():
    print("Success!Welcome admin!")


#checks if credentials are corerect
def authAdmin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username: "))
    passaword = input(str("Password: "))
    if username == "admin":
        if password == "password":
            admin()
        else:
            print("Wrong pasword")
    else:
        print("Login details are wrong")

#main loop executes all the startup
def main():
    while True:
        print("Welcome to my college application")
        print("")
        print("1. Log in as a student")
        print("2. Log in as a teacher")
        print("3. Log in as a admin")

        userInput = input(str("Option:"))
        if userInput == "1":
            print("You have logged in as a student")
        elif userInput == "2":
            print("You have logged in as a teacher")
        elif userInput == "3":
            
            authAdmin()
        else:
            print("This is not a valid input")
        



main()