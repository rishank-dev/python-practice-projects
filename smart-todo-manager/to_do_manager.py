# Smart To-Do Manager



# ========== PROJECT START ===========

# (1.) Check or make the file to store tasks
try:
    f = open("task_manager.txt", "r")

except FileNotFoundError as e:
    f = open("task_manager.txt", "w")

finally:
    f.close()



# •••••••••••••••••••••••••••••••••••••••••



# (2.) Display user with options to choose to execute a task
print(f"{" "*20} SMART TO-DO MANAGER")

# → Menu Options
def display_menu():
    print(f"\n{'-' * 15} Menu {'-' * 15} \n")
    print("1 → Add Task \n2 → View All Tasks \n3 → Update Task \n4 → Complete Task \n5 → Delete Task \n6 → Search Task \n")
    print("-" *40)


# → User Choose Task
def menu_choose_task():
    while True:
        try :
            choice = int(input("\nEnter your choice according to the task you want to perform (1 - 7) : "))
            if choice in [1,2,3,4,5,6]:
                return choice
            else:
                print("Try entering a Valid Choice! ")
                
        except :
            print("Try entering a Valid Choice! ")



# •••••••••••••••••••••••••••••••••••••••••



# (3.) Logic to carry the task entered by the user

# → Add Task
def add_task():
    print("\nAdding a task..... \n ")
    title = input("Enter the 'Title' of the task : ").title()
    
    while True:
        p = input("Choose Priority of the task.(L → low, M → medium, H → high) : ").upper()
        if p not in ["L", "M", "H"]:
            print("Enter from (L / M / H) \n")
        else :
            if p=='L':
                priority = 'Low'
            elif p=='M':
                priority = 'Medium'
            elif p=='H':
                priority = 'High'
            break
            
    due_date = input("Enter the due date : ")
    
    while True:
        try : 
            task_id = int(input("Enter a numeric task id : "))
            break
        except :
            print("Enter a valid numeric ID \n")
        
    task = [str(task_id), title, priority, due_date]
    
    with open("task_manager.txt", "a") as f:
        f.write(str(task) + "\n")
    
    print("\nTask added successfully!!! \n")
    



# → View All Tasks
def view_all_tasks():
    print("\n YOUR TASKS \n")
    with open("task_manager.txt", "r") as f:
        content = f.read()
        
    list_content = content[:-1].split('\n')
    for i in list_content:
        values = i[2:-2].split("\', \'")
        print(f"Task ID : {values[0]}")
        print(f"Task Title : {values[1]}")
        print(f"Task Priority : {values[2]}")
        print(f"Task Due-Date : {values[3]} \n")




# → Update Task
def update_task():
    while True:
        try : 
            id = int(input("\nEnter the Task ID to update the task : "))
            break
        except :
            print("Try entering a valid numeric Task ID \n")
            
    with open("task_manager.txt", "r") as f:
        content = f.read()
        
    list_content = content[:-1].split('\n')
    for index,i in enumerate(list_content):
        values = i[2:-2].split("\', \'")
        if values[0] == str(id):
            list_content.pop(index)
            with open("task_manager.txt","w") as f:
                f.write("\n".join(list_content) + "\n")
            
            print("\nUpdating the task....")
            
            title = input("Update  the 'Title' of the task : ").title()
    
            while True:
                p = input("Update Priority of the task.(L → low, M → medium, H → high) : ").upper()
                if p not in ["L", "M", "H"]:
                    print("Enter from (L / M / H) \n")
                else :
                    if p=='L':
                        priority = 'Low'
                    elif p=='M':
                        priority = 'Medium'
                    elif p=='H':
                        priority = 'High'
                    break
                    
            due_date = input("Update the due date : ")
            task_id = id
            
            task = [str(task_id), title, priority, due_date]
            
            with open("task_manager.txt", "a") as f:
                f.write(str(task) + "\n")
            
            print("\nTask updated successfully!!! \n")
            break
            
    else:
        print("Task ID not found")



# → Complete Task
def complete_task():
    print("\nThe task completed will be permenantly removed from you To-Do List \n")
    while True:
        try : 
            id = int(input("Enter the Task ID of the task completed : "))
            break
        except :
            print("Try entering a valid numeric Task ID \n")
            
    with open("task_manager.txt", "r") as f:
        content = f.read()
        
    list_content = content[:-1].split('\n')
    for index,i in enumerate(list_content):
        values = i[2:-2].split("\', \'")
        if values[0] == str(id):
            removed = list_content.pop(index)[2:-2].split("\', \'")
            with open("task_manager.txt","w") as f:
                f.write("\n".join(list_content) + "\n")
                
            print("\nFollowing task is Completed and removed from To-Do List :-")
            print(f"Task ID : {removed[0]}")
            print(f"Task Title : {removed[1]}")
            print(f"Task Priority : {removed[2]}")
            print(f"Task Due-Date : {removed[3]} \n")
            break
    else:
        print("Task ID not found !! ")



# → Delete task
def delete_task():
    print("\nThe task deleted will be permenantly removed from you To-Do List \n")
    while True:
        try : 
            id = int(input("Enter the Task ID of the task you want to delete : "))
            break
        except :
            print("Try entering a valid numeric Task ID \n")
            
    with open("task_manager.txt", "r") as f:
        content = f.read()
        
    list_content = content[:-1].split('\n')
    for index,i in enumerate(list_content):
        values = i[2:-2].split("\', \'")
        if values[0] == str(id):
            removed = list_content.pop(index)[2:-2].split("\', \'")
            with open("task_manager.txt","w") as f:
                f.write("\n".join(list_content) + "\n")
                
            print("\nFollowing task is deleted from To-Do List :-")
            print(f"Task ID : {removed[0]}")
            print(f"Task Title : {removed[1]}")
            print(f"Task Priority : {removed[2]}")
            print(f"Task Due-Date : {removed[3]} \n")
            break
    else:
        print("Task ID not found !! ")
    


# → Search task or view task
def search_task():
    print("\nSearching the task..... \n")
    while True:
        try : 
            id = int(input("Enter the Task ID of that task : "))
            break
        except :
            print("Try entering a valid numeric Task ID \n")
            
    with open("task_manager.txt", "r") as f:
        content = f.read()
        
    list_content = content[:-1].split('\n')
    for index,i in enumerate(list_content):
        values = i[2:-2].split("\', \'")
        if values[0] == str(id):
            find = list_content[index][2:-2].split("\', \'")
            print("\nHere are the details of the task : :-")
            print(f"Task ID : {find[0]}")
            print(f"Task Title : {find[1]}")
            print(f"Task Priority : {find[2]}")
            print(f"Task Due-Date : {find[3]} \n")
            break
    else:
        print("Task ID not found !! ")




# •••••••••••••••••••••••••••••••••••••••••



# (4.) Executing the task entered by the user
def execute():
    user_choice = menu_choose_task()
    
    if user_choice == 1:
        add_task()
    elif user_choice == 2:
        view_all_tasks()
    elif user_choice == 3:
        update_task()
    elif user_choice == 4:
        complete_task()
    elif user_choice == 5:
        delete_task()
    elif user_choice == 6:
        search_task()
    




# •••••••••••••••••••••••••••••••••••••••••



# (5.) Repeat the task by going to menu or exit
def menu_exit():
    while True:
        repeat = input("\nEnter 'm' to return to menu and 'q' to quit : ")
        if repeat == 'm':
            return True
        elif repeat == 'q':
            return False
        else:
            print("Try entering a valid choice (m/q) : ")
            




# •••••••••••••••••••••••••••••••••••••••••



# (6.) Running the main loop
def main():
    while True:
        display_menu()
        execute()
        if not menu_exit():
            print("\nExiting the app...... \nGood Bye")
            break

main()




# ========== PROJECT END ============
