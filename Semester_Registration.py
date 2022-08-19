class finance:
    def __init__(self,name,reg_no,branch,semester,email,date,electives,backlogs,form_type,total_fees,paid_amount,due_amount,payment_status,payment_span):
        self.reg_no = reg_no
        self.name = name
        self.branch = branch
        self.semester = semester
        self.email = email
        self.date = date
        self.electives = str(electives)
        self.backlogs = str(backlogs)
        self.form_type = form_type
        self.total_fees = str(total_fees)
        self.paid_amount = str(paid_amount)
        self.due_amount = str(due_amount)
        self.payment_status = payment_status
        self.payment_span = payment_span
        file = open("E:\\Programming\\Python\\userdetails.txt",'a')
        file.write(self.reg_no+"\t"+self.name+"\t"+self.branch+"\t"+self.semester+"\t"+self.email+"\t"+self.date+"\t"+self.electives+"\t"+self.backlogs+"\t"+self.form_type+"\t"+self.total_fees+"\t"+self.paid_amount+"\t"+self.due_amount+"\t"+self.payment_status+"\t"+self.payment_span+"\n")
        file.close()

    def receipt_generation(self):
        file = open("E:\\Programming\\Python\\userdetails.txt",'r')
        data = file.readlines()
        start = 0
        stop = 0
        detail = 1
        for details in data:
            reg = details[0:9]
            if(self.reg_no == reg):
                print("***************Student Payment Receipt****************")
                print()
                while(stop != -1):
                    stop = details.find("\t",start)
                    if(detail == 1):
                        print("Registration No:")
                    elif(detail == 2):
                        print("Name:")
                    elif(detail == 3):
                        print("Department:")
                    elif(detail == 4):
                        print("Semester:")
                    elif(detail == 5):
                        print("Email:")
                    elif(detail == 6):
                        print("Date of registration:")
                    elif(detail == 7):
                        print("No. of electives:")
                    elif(detail == 8):
                        print("No. of backlogs:")
                    elif(detail == 9):
                        print("Form type:")
                    elif(detail == 10):
                        print("Total fees:")
                    elif(detail == 11):
                        print("Paid amount:")
                    elif(detail == 12):
                        print("Due amount:")
                    elif(detail == 13):
                        print("Payment Status:")
                    elif(detail == 14):
                        print("Payment Span:")
                    else:
                        break
                    print(details[start:stop])
                    detail += 1
                    start = stop + 1
                break
        file.close()

class student:
    def __init__(self,reg_no,password = None):
        self.reg_no = reg_no
        if(password != None):
            self.password = password
            file = open("E:\\Programming\\Python\\userpassword.txt",'a')
            file.write(self.reg_no+"\t"+self.password+"\n")
            print("Successfully registered registration no:",self.reg_no)
            file.close()
            return
        print("Successfully logged in registration no:",self.reg_no)

    def registration(self):
        form_type = input("Please enter the form you'd like to fill (A or B):")
        if(form_type == 'A' or form_type == 'a' or form_type == 'B' or form_type == 'b'):
            print("Welcome to form",form_type)
            name = input("Please enter the student name:")
            reg_no = input("Please enter the student's registration number:")
            branch = input("Please enter the student's branch:")
            semester = input("Please enter the student's current semester")
            email = input("Please enter the student's email ID:")
            date = input("Please enter the date of registration:")
            electives = input("Please enter the number of electives:")
            backlogs = input("Please enter the number of backlogs(if any):")
            payment_status = "Unpaid"
            total_fees = 305000
            paid_amount = int(input("Enter the amount of fees paid:"))
            due_amount = total_fees - paid_amount
            if(due_amount <= 0):
                due_amount = 0
                payment_status = "Paid"
            elif(due_amount > 0 and due_amount <= total_fees):
                payment_status = "Due"
            payment_span = input("Payment span (Installment or lumpsum):")
            obj2 = finance(name,reg_no,branch,semester,email,date,electives,backlogs,form_type,total_fees,paid_amount,due_amount,payment_status,payment_span)
            obj2.receipt_generation()
        else:
            print("Please enter the correct form type!")
            self.registration()

def menu():
    print("\t************MAIN MENU**************")
    print()

    choice = input("""
                      A: Student sign up
                      B: Student sign in
                      Q: Quit/Log Out

                      Please enter your choice: """)

    print()

    if (choice == "A" or choice =="a"):
        user_sign_up()
        menu()
    elif (choice == "B" or choice =="b"):
        user_sign_in()
        menu()
    elif choice=="Q" or choice=="q":
        return
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        menu()

def user_sign_up():
    print("Welcome to user sign up!")
    reg_no = input("Please enter the user's registration number (9 digits):")
    if(len(reg_no) != 9):
        print("Please enter a valid registration ID")
        return
    password = input("Please enter the user's password:")
    file = open("E:\\Programming\\Python\\userpassword.txt",'r')
    sid = file.readlines()
    # print(sid)
    found = False
    for reg in sid:
        for j in range(9):
            if(reg[j] != reg_no[j]):
                break
            elif(j == 8):
                found = True
        if(found == True):
            print("Error, user already exists!")
            file.close()
            return
    file.close()
    obj = student(reg_no,password)

def user_sign_in():
    print("Welcome to user sign in!")
    reg_no = input("Please enter the user's registration number (9 digits):")
    if(len(reg_no) != 9):
        print("Please enter a valid registration ID")
        return
    password = input("Please enter the user's password:")
    file = open("E:\\Programming\\Python\\userpassword.txt",'r')
    sid = file.readlines()
    print(sid)
    found = False
    for reg in sid:
        for j in range(9):
            if(reg[j] != reg_no[j]):
                break
            elif(j == 8):
                found = True
        if(found == True):
            i = 0
            j = 10
            authenticated = False
            if(len(reg) - 11 == len(password)):
                while(i < len(password) and reg[j+i] == password[i]):
                    if(i == len(password)-1):
                        print("Correct Password")
                        authenticated = True
                        break
                    i+=1
            if(i != len(password)-1):
                print("Incorrect password")
            if(authenticated == True):
                break

    if(found == True):
        print("User Sign in successful!")

    else:
        print("Invalid registration no. or password")
        file.close()
        return
    obj = student(reg_no)
    file.close()
    obj.registration()

menu()