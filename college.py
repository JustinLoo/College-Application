import mysql.connector as mysql

db = mysql.connect(host="localhost",user="root",password="",database="college")
commandHandler = db.cursor(buffered=True)

print("___________________________________________________________________")

def teacher_session():
    while 1:
        print("___________________________________________________________________")
    
        print("")
        print("Teacher's Menu")
        print("1. Mark student register")
        print("2. View register")
        print("3. Logout")
        print("___________________________________________________________________")
    
        userInput = input(str("Option : "))
        if userInput == "1":
            print("")
            print("Mark student register")
            commandHandler.execute("SELECT username FROM users WHERE privilege = 'student'")
            records = commandHandler.fetchall()
            date    = input(str("Date : DD/MM/YYYY : "))
            for record in records:
                record = str(record).replace("'","")
                record = str(record).replace(",","")
                record = str(record).replace("(","")
                record = str(record).replace(")","")
                #Present | Absent | Late
                status = input(str("Status for " + str(record) + "P/A/L : "))
                queryValues = (str(record),date,status)
                commandHandler.execute("INSERT INTO attendance (username, date, status) VALUES(%s,%s,%s)",queryValues)
                db.commit()
                print(record + " Marked as " + status)
        elif userInput == "2":
            print("")
            print("Viewing all student registers")
            commandHandler.execute("SELECT username, date, status FROM attendance")
            records = commandHandler.fetchall()
            print("Displaying all registers")
            for record in records:
                print(record)
            print("___________________________________________________________________")
        elif userInput == "3":
            break
            print("___________________________________________________________________")
        else:
            print("No valid option was selected")
            print("___________________________________________________________________")

def student_session(username):
    while 1:
        print("___________________________________________________________________")
    
        print("")
        print("Student's Menu")
        print("")
        print("1. View Register")
        print("2. Download Register")
        print("3. Logout")
        print("___________________________________________________________________")

        userInput = input(str("Option : "))
        if userInput == "1":
            print("Displaying register")
            username = (str(username),)
            commandHandler.execute("SELECT date, username, status FROM attendance WHERE username = %s",username)
            records = commandHandler.fetchall()
            for record in records:
                print(record)
            print("___________________________________________________________________")
        elif userInput == "2":
            print("Downloading Register")
            username = (str(username),)
            commandHandler.execute("SELECT date, username, status FROM attendance WHERE username = %s",username)
            records = commandHandler.fetchall()
            for record in records:
                with open("C:/Users/Johan Godinho/Desktop/register.txt", "w") as f:
                    f.write(str(records)+"\n")
                f.close()
            print("All records saved")
            print("___________________________________________________________________")
        elif userInput == "3":
            break
            print("___________________________________________________________________")
        else:
            print("No valid option was selected")
            print("___________________________________________________________________")


def admin_session():
    while 1:
        print("___________________________________________________________________")
    
        print("")
        print("Admin Menu")
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")
        print("5. Logout")
        print("___________________________________________________________________")

        userInput = input(str("Option : "))
        if userInput == "1":
            print("")
            print("Register New Student")
            username = input(str("Student username : "))
            password = input(str("Student password : "))
            queryValues = (username,password)
            commandHandler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s,'student')",queryValues)
            db.commit()
            print(username + " has been registered as a student")
            print("___________________________________________________________________")
        
        elif userInput == "2":
            print("")
            print("Register New Teacher")
            username = input(str("Teacher username : "))
            password = input(str("Teacher password : "))
            queryValues = (username,password)
            commandHandler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s,'teacher')",queryValues)
            db.commit()
            print(username + " has been registered as a teacher")
            print("___________________________________________________________________")
    
        elif userInput == "3":
            print("")
            print("Delete Existing Student Account")
            username = input(str("Student username : "))
            queryValues = (username,"student")
            commandHandler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",queryValues)
            db.commit()
            
            if commandHandler.rowcount < 1:
                print("User not found")
                print("___________________________________________________________________")
            else:
                print(username + " has been deleted")
                print("___________________________________________________________________")
            print("___________________________________________________________________")

        elif userInput == "4":
            print("")
            print("Delete Existing Teacher Account")
            username = input(str("Teacher username : "))
            queryValues = (username,"teacher")
            commandHandler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",queryValues)
            db.commit()
            if commandHandler.rowcount < 1:
                print("User not found")
                print("___________________________________________________________________")
            else:
                print(username + " has been deleted")
                print("___________________________________________________________________")
            print("___________________________________________________________________")

        elif userInput == "5":
            break
            print("___________________________________________________________________")
        else:
            print("No valid option selected")
            print("___________________________________________________________________")

def studentAuth():
    print("___________________________________________________________________")
    
    print("")
    print("Student's Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    queryValues = (username, password, "student")
    commandHandler.execute("SELECT username FROM users WHERE username = %s AND password = %s AND privilege = %s",queryValues)
    if commandHandler.rowcount <= 0:
        print("Invalid login details")
        print("___________________________________________________________________")
    else:
        student_session(username)
        print("___________________________________________________________________")
def teacherAuth():
    print("___________________________________________________________________")
    
    print("")
    print("Teacher's Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    queryValues = (username, password)
    commandHandler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'teacher'",queryValues)
    if commandHandler.rowcount <= 0:
        print("Login not recognized")
        print("___________________________________________________________________")
    else:
        teacher_session()
        print("___________________________________________________________________")

def adminAuth():
    print("___________________________________________________________________")
    
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password !")
            print("___________________________________________________________________")
    else:
        print("Login details not recognised") 
        print("___________________________________________________________________")

def main():
    while 1:
        print("___________________________________________________________________")
    
        print("Welcome to the college system")
        print("")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")
        print("___________________________________________________________________")

        userInput = input(str("Option : "))
        if userInput == "1":
            studentAuth()
        elif userInput == "2":
            teacherAuth()
        elif userInput == "3":
            adminAuth()
        else:
            print("No valid option was selected")

main()