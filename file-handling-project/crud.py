from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try:
        readfileandfolder()
        name = input("enter file name: ")
        p = Path(name)

        if not p.exists(): 
            with open(p, "w") as fs:
                data = input("write the data you want to input: ")
                fs.write(data)
            print("File Created Successfully :)")
        else:
            print("this file already exist :(")
    except Exception as err:
        print(f"An Error Occurred as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("which file you want to read: ")
        p = Path(name)

        if p.exists() and p.is_file():  
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
        else:
            print("file not exist")
    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to update: ")
        p = Path(name)

        if p.exists() and p.is_file():  
            print("enter 1 for rename file: ")
            print("enter 2 to overwrite: ")
            print("enter 3 for append: ")
            res = int(input("Enter your choice: "))

            if res == 1:
                name2 = input("Enter the new file name: ")
                p2 = Path(name2)
                p.replace(p2)
                print("File Renamed Successfully :)")

            elif res == 2:
                with open(p, "w") as fs:
                    data = input("enter the data you want to overwrite: ")
                    fs.write(data)
                print("File Overwritten Successfully :)")

            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("write append data: ")
                    fs.write(" " + data)
                print("Data Appended Successfully :)")
        else:
            print("file not exist")
    except Exception as err:
        print(f"the error occured as {err}")

def deletefile() :
    readfileandfolder()
    name = input("enter file you want to delete")
    p = Path(name)
    try :
        if p.exists() and p.is_file() :
            os.remove(p)
            print("file deleted sucessfully :")
        else :
            print("no such file exist")

    except Exception as err :
        print(f"the error occured as {err}")

print("press 1 for creating a file ")
print("press 2 for reading a file ")
print("press 3 for updating a file ")
print("press 4 for deleting a file ")

check = int(input("Enter your choice: "))

if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    updatefile()
elif check == 4:
    deletefile()
else:
    print("Invalid Choice")