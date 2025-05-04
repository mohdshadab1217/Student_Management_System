student_list= ["Mohd Shadab", "Rohit Sharma", "Shalini Arora", "Asheesh Chanchlani", "Arpita", "Shadab Khan", "Arpita Singh","Arun Jaiswal", "Kajal", "Arpita Sharma"]

def search(a,lst):
    new_list =set()
    if a in lst:
        return lst.index(a)
    else:
        for i in a.split():
            for l,j in enumerate(lst):
                for k in j.split():
                    if i ==k:
                        new_list.add(l)
        return list(new_list)

print("-"*60)
print("   *********WELCOME TO STUDENT MANAGEMENT SYSTEM*********")
print("-"*60)
print("Please select any one option:")
print("1. To view student list")
print("2. To add new name(s) of student in the list")
print("3. To remove data")
print("4. To search data")
print("5. Exit")
print("-"*60)

while True:
    n =(input("Enter your choice:"))
    print()
    match n:
        case "1":
            for i,j in enumerate(student_list):
                print(i,j)
            print()
        case "2":
            repeat = "y"
            while repeat=="y":
                name = str.title(str.strip(input("Enter name of student:")))
                student_list.append(name)
                print("Name is added successfully..")
                repeat = str.lower(input("DO you want to add more names of student (y/n):"))
                while repeat != "n" and repeat != "y":
                    repeat= str.lower(input("Incorrect input, press only 'y' to add more names and 'n' for not:"))
                    if repeat == "n" or repeat == "y":
                        break
                if repeat == "n":
                    break
                elif repeat =="y":
                    continue
            print()
        case "3":
            name=str.title(str.strip(input("Enter name to delete:")))
            if name in student_list:
                student_list.remove(name)
                print("Student name is successfully deleted..")
            else:
                index = search(name, student_list)
                if len(index)==0:
                    print("Name is not found in the list")
                else:
                    print("Exact match is not found but similar names is/are:")
                    for i in index:
                        print(f"{i}. {student_list[i]}")
                    value=input("Enter index value of above name to delete or type 'cancel to cancel the request")
                    while value!='cancel':
                        if value.isdigit() ==True:
                            del student_list[int(value)]
                            break
                        value=input("Incorrect input, enter index value of above name to delete or type 'cancel to cancel the request")
                        if value== 'cancel':
                            break
            print()
        case "4":
            name=str.title(str.strip(input("Enter name to search:")))
            index= search(name, student_list)
            if type(index)==int:
                print("Name is found in the list at index:",index)
            else:
                if len(index)==0:
                    print("Name is not found")
                else:
                    print("Exact match is not found but similar names is/are:")
                    for i in index:
                        print(student_list[i])
            print()
        case "5":
            exit()
        case _:
            print("Enter right option from above menue..")
            print()
