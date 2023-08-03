#SQL / 
#MySQL / PostgreSQL / MongoDB / SQLITE3/ Files => Database Engines / Names
#SQL => Structured Query Language -> Table

# Python language


#           Key             Value
database = {1   :   {'Roll':1,'Name':'Jay','Fees':20000, 'Marks':78},
            2   :   {'Roll':2,'Name':'Viru','Fees':25000, 'Marks':69}}

def dashboard():
    print('Welcome to Student Management Project By Batch 1109')
    print("""
                    Menu
                    1. Create a new Student
                    2. Display all students
                    3. Update the students
                    4. Delete the students
    """)

def create_student():
    # pass
    print('Pls Fill all the detials of the student.')
    print()
    uroll = eval(input("Enter the Roll number of the student: "))
    uname = input("Enter the name of the student: ")
    ufees = eval(input("Enter the fees paid by the student: "))
    umarks = eval(input ('Enter the marks of the student: '))

    chotu_dict = {}
    chotu_dict['Roll'] = uroll
    chotu_dict['Name'] = uname
    chotu_dict['Fees'] = ufees
    chotu_dict['Marks'] = umarks
    # print(chotu_dict)
    database[uroll] = chotu_dict
    print()
    print(f"Student {uname} added successfully to the database")


def display_student():
    # print(database.values())
    print()
    print('-'* 85)
    print("|{r:^20}|{n:^20}|{f:^20}|{m:^20}|".format(r="Roll Number", n = "Name", f='Fees Paid', m ='Marks'))
    print('-'* 85)


    for i in database.values():
        # print('-'* 85)
        print("|{r:^20}|{n:^20}|{f:^20}|{m:^20}|".format(r=i['Roll'], n = i['Name'], f=i['Fees'], m =i['Marks']))
        print('-'* 85)




def update_student():
    # pass
    uroll = eval(input('Enter roll number of students to Update: ')) # 1
    if uroll in database:
        print('Pls Fill updated detials of the student.')
        print()
        uname = input("Enter the Updated name of the student: ")
        ufees = eval(input("Enter the updated fees paid by the student: "))
        umarks = eval(input ('Enter the Updated marks of the student: '))

        
        database[uroll]['Name'] = uname
        database[uroll]['Fees'] = ufees
        database[uroll]['Marks'] = umarks

        print(f"Roll number {uroll} updated successfully to database.")

    else:
        print("Invalid roll number to Update!")




def delete_studnet():
    # pass
    uroll = eval(input('Enter roll number of students to delete: ')) # 1
    if uroll in database:
        del database[uroll]
        print(f'Roll number {uroll} deleted successfully from database.')
    else:
        
        
        print('Roll number is not in database!!')


while True:
    dashboard()
    choice = eval(input('Enter your choice:')) # 1 2

    if choice == 1:
        create_student()

    elif choice == 2:
        if len(database) > 0:
            display_student()
        else:
            print('There are no students in the database.')

    elif choice == 3:
        update_student()

    elif choice == 4:
        if len(database)> 0:
            delete_studnet()
        else:
            print('There are no students in the database.')

    else:
        print('Invalid choice!!!... Please enter a valid choice.')

    ch = input('Do you want to continue y/n? :')
    if ch == 'n':
        print(database)
        break