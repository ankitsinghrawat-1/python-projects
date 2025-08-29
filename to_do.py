import datetime as dt
import time

d = dt.date.today()
t = time.strftime("%H:%M")


def show_menu():
    print("\n ***** TO-DO LIST *****")
    print("1. view task\n" 
    "2. Add a task\n"
    "3. Delete a task\n"
    "4. Exit \n")

def view_task():

    try:
        with open("python\\tasks.txt", "r") as f:
            task = f.readlines()
            if not task:
                print("No task yet!")
            else:
                for i, task in enumerate(task, 1):
                    print(f"{i}. {task.strip()}")
            

    except FileNotFoundError:
        print("File does not exists!")


def add_task():
    task = input("Enter the task you want to add: ")
    with open("python\\tasks.txt", "a") as f:
        f.write(f"{task}               ---{d}---{t} \n")
    print("task added successfully! ")


def delete_task():
    try:
        with open("python\\tasks.txt", "r") as f:
            task = f.readlines()

        view_task()
        choice = int(input("Enter the task number you want to delete: "))
        if 1 <= choice <= len(task):
            del task[choice - 1]
            with open ("python\\tasks.txt", "w") as f:
                f.writelines(task)
            print("task deleted! ")
        else:
            print("Enter a valid task number! ")

    except FileNotFoundError:
        print("Task not found!")
    except ValueError:
        print("Please enter a valid value! ")



while True:
    show_menu()
    option = input("Choose option: ")

    if option == "1":
        view_task()
    elif option == "2":
        add_task()
    elif option == "3":
        delete_task()
    elif option == "4":
        print("Exiting the program\nGood bye!")

    else:
        print("Invalid Choice\nTry again")