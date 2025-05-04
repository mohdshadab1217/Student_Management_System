import os
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
    n=input("Enter your choice:")
    print()
    match n:
        case "1": 
            if os.path.exists("data_file.txt"):
                fileobj = open("data_file.txt", "r")
                names = fileobj.read()
                print(names)
            else:
                print("No file exists")
            
            print()
        case "2":
            repeat = "y"
            while repeat=="y":
                name = str.title(str.strip(input("Enter name of student:")))+"\n"
                #student_list.append(name)
                fileobj = open("data_file.txt", "a")
                fileobj.write(name+"\n")
                fileobj.close()
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
            name=str.title(str.strip(input("Enter name to delete:")))+"\n"
            if os.path.exists("data_file.txt"):
                with open("data_file.txt", "r") as fileobj:
                    student_list = fileobj.readlines()
                    print(student_list)
                for i in student_list:
                    if i == name:
                        student_list.remove(i)
                        with open("data_file.txt", "w") as fileobj:
                            fileobj.writelines(student_list)
                        print("Name is removed")
                        break
                else:
                    print("Name is not in the list")
                                
            else:
                print("File does not exist")
            print()
        case "4":
            name=str.title(str.strip(input("Enter name to search:")))+'\n'
            with open("data_file.txt", "r") as fileobj:
                student_list = fileobj.readlines()
            index=search(name, student_list)
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
