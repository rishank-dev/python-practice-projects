# Smart To-Do Manager


# ========== PROJECT START ===========
import json
from tabulate import tabulate
import time

print(" " * 20 + "SMART TO-DO MANAGER")



# Fetch file details
def load_data():
    try:
        with open("task_sample.txt", "r") as file:
            data = file.read().strip()
            if not data:
                return []
            return json.loads(data)
    except (FileNotFoundError or json.JSONDecodeError):
        return []



# Menu Options
def display_menu():
    print(f"\n{'-' * 15} Menu {'-' * 15} \n")
    print(" (1.)  Add new task")
    print(" (2.)  View All tasks")
    print(" (3.)  Update a task")
    print(" (4.)  Mark a task as complete")
    print(" (5.)  Delete a task")
    print(" (6.)  Search for a task")
    print(" (7.)  Exit \n")
    print("-" *40)




# User Choose Task
def menu_choose_task():
    while True:
        choice = input("\nEnter your choice from (1 - 7) : ")
        if choice in ['1','2','3','4','5','6','7']:
            return choice
        else:
            print("Try entering a Valid Choice! ")




# File save helper function
def save_file_helper(tasks_list):
    with open("task_sample.txt", "w") as file:
        json.dump(tasks_list, file)




# Add Task
def add_task(tasks_list):
    print("\nAdding a task..... \n ")
    while True:
        title = input("Enter 'Title' of the task : ").title().strip()
        if title == '':
            print("Title should have some valid characters! \n")
        else:
            break
            
    
    while True:
        priority = input("Choose Priority of the task.(Low/ Medium/High)  : ").upper().strip()
        if priority in ["LOW", "MEDIUM", "HIGH"]:
            break
        else:
            print("Try entering valid priority. \n")
            
    due_date = input("Enter the due date : ").strip()
    
    task = {'Title' : title, 'Priority' : priority, 'Due Date' : due_date, 'Status' : 'Pending'}
    tasks_list.append(task)
    
    save_file_helper(tasks_list)
    
    print("\nTask added successfully!!! \n")
    





# View All Tasks
def view_all_tasks(tasks_list):
    print("\n YOUR TASKS :- \n")
    
    if not tasks_list:
        print("No task added yet.\n")
        return
        
    print('*' * 40)
    print(tabulate(tasks_list, headers="keys", tablefmt = "simple", colglobalalign='center', showindex=range(1, len(tasks_list)+1)))
    print('*' * 40)




# Update Task
def update_task(tasks_list):
    if not tasks_list:
        print("No task added yet.\n")
        return
        
    try:
        task_index = int(input("\nEnter the Task number to update the task : "))
    except ValueError:
        print("Task number should be a valid number")
        return
    
    for index, task in enumerate(tasks_list):
        if task_index == index+1:
            print("\nUpdating the task....")
            
            while True:
                new_title = input("Enter 'Title' of the task : ").title().strip()
                if new_title == '':
                    print("Title should have some valid characters! \n")
                else:
                    break
    
            while True:
                new_priority = input("Update Priority of the task.(Low/ Medium/ High)  : ").upper().strip()
                if new_priority in ["LOW", "MEDIUM", "HIGH"]:
                    break
                else:
                    print("Try entering valid priority. \n")
                    
            new_due_date = input("Update the due date : ").strip()
            
            task['Title'] = new_title
            task['Priority'] = new_priority
            task['Due Date'] = new_due_date
            
            save_file_helper(tasks_list)
            
            print(f"\nTask Number {task_index} updated successfully!!! \n")
            break
            
    else:
        print(f"Task number {task_index} not found.")





# Complete Task
def complete_task(tasks_list):
    if not tasks_list:
        print("No task added yet.\n")
        return
        
    try:
        task_index = int(input("\nEnter task number to mark as complete : "))
    except ValueError:
        print("Task number should be a valid number")
        return
    
    for index, task in enumerate(tasks_list):
        if task_index == index + 1:
            task['Status'] = 'Completed'
            save_file_helper(tasks_list)
            print(f"Task '{task['Title']}' is marked complete.")
            break
            
    else:
        print(f"Task number {task_index} not found.")
        




# Delete task
def delete_task(tasks_list):
    if not tasks_list:
        print("No task added yet.\n")
        return
        
    print("\nThe task deleted will be permanently removed from your To-Do List. \n")
    
    try:
        task_index = int(input("\nEnter task number to delete : "))
    except ValueError:
        print("Task number should be a valid number")
        return
    
    for index, task in enumerate(tasks_list):
        if task_index == index + 1:
            removed = tasks_list.pop(index)
            
            save_file_helper(tasks_list)
            print(f"Task '{removed['Title']}' is deleted from your To-Do List")
            break
    else:
        print(f"Task number {task_index} not found.")




# Search task or view task
def search_task(tasks_list):
    if not tasks_list:
        print("No task added yet.\n")
        return
        
    try:
        task_index = int(input("\nEnter task number to search : "))
    except ValueError:
        print("Task number should be a valid number")
        return
    
    for index, task in enumerate(tasks_list):
        if task_index == index + 1:
            print(f"Searching for task number {task_index} ......")
            print(f"\n Task Number : {task_index} \n")
            print('*' * 40)
            print(tabulate([task], headers="keys", tablefmt = "simple", colglobalalign='center', showindex=[index+1]))
            print('*' * 40)
            break
    else:
        print(f"Task number {task_index} not found.")




# Executing the task entered by the user
def main():
    while True:
        tasks_list = load_data()
        display_menu()
        user_choice = menu_choose_task()
        
        match user_choice:
            case '1':
                add_task(tasks_list)
                time.sleep(2)
            case '2':
                view_all_tasks(tasks_list)
                time.sleep(2)
            case '3':
                update_task(tasks_list)
                time.sleep(2)
            case '4':
                complete_task(tasks_list)
                time.sleep(2)
            case '5':
                delete_task(tasks_list)
                time.sleep(2)
            case '6':
                search_task(tasks_list)
                time.sleep(2)
            case '7':
                print("Exiting the program.....")
                break
    


# Running for main file 
if __name__ == '__main__':
    main()



# ========== PROJECT END ============
