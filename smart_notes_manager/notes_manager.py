# Smart Notes Manager App


# ========== PROJECT START ===========
import json
from tabulate import tabulate
import time
from datetime import datetime


print("\n", " " * 20 + "SMART NOTES MANAGER")


# Fetch file details
def load_data():
    try:
        with open("notes_sample.txt", "r") as file:
            data = file.read().strip()
            if not data:
                return []
            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError) :
        return []


# Menu Options
def display_menu():
    print(f"\n{'-' * 15} Menu {'-' * 15} \n")
    print(" (1.)  Add a new note")
    print(" (2.)  View all notes")
    print(" (3.)  Edit a note")
    print(" (4.)  Delete a note")
    print(" (5.)  Search for a note")
    print(" (6.)  Exit \n")
    print("-" * 40)


# User Choose Note
def menu_choose_note():
    while True:
        choice = input("\nEnter your choice from (1 - 6) : ")
        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice
        else:
            print("Try entering a Valid Choice! ")


# File save helper function
def save_file_helper(notes_list):
    with open("notes_sample.txt", "w") as file:
        json.dump(notes_list, file)


# Add Note
def add_note(notes_list):
    print("\nAdding a new NOTE..... \n ")
    while True:
        title = input("Enter 'Title' of the note : ").title().strip()
        if title == "":
            print("Title should have some valid characters! \n")
        else:
            break

    description = input("Enter your note description : ").strip().capitalize()

    add_date = datetime.now().strftime("%d-%m-%Y")
    add_time = datetime.now().strftime("%I:%M:%S %p")

    notes = {
        "Title": title,
        "Description": description,
        "Date_add": add_date,
        "Time_add": add_time,
    }

    notes_list.append(notes)

    save_file_helper(notes_list)

    print("\nNote added successfully!!! \n")


# View All Notes
def view_all_notes(notes_list):
    print("\n YOUR NOTES :- \n")

    if not notes_list:
        print("No notes added yet.\n")
        return

    print("*" * 40)
    table_element = []
    for note in notes_list:
        element = {
            "Title": note["Title"],
            "Description": note["Description"],
            "Added on Date": note["Date_add"],
        }
        table_element.append(element)

    print(
        tabulate(
            table_element,
            headers="keys",
            tablefmt="github",
            colglobalalign="center",
            maxcolwidths=30,
            showindex=range(1, len(table_element) + 1),
        )
    )
    print("\n" + "*" * 40)


# Update Note
def edit_note(notes_list):
    if not notes_list:
        print("No notes added yet.\n")
        return

    try:
        note_index = int(input("\nEnter the Note number to edit : "))
    except ValueError:
        print("Note number should be a valid number")
        return

    for index, note in enumerate(notes_list):
        if note_index == index + 1:
            print("\nEditing the note....")

            while True:
                new_title = input("Enter 'Title' of the note : ").title().strip()
                if new_title == "":
                    print("Title should have some valid characters! \n")
                else:
                    break

            new_description = (
                input("Enter your note description : ").strip().capitalize()
            )
            edit_date = datetime.now().strftime("%d-%m-%Y")

            note["Title"] = new_title
            note["Description"] = new_description
            note["Edit date"] = edit_date

            save_file_helper(notes_list)

            print(f"\nNote Number {note_index} updated successfully!!! \n")
            break

    else:
        print(f"Note number {note_index} not found.")


# Delete note
def delete_note(notes_list):
    if not notes_list:
        print("No note added yet.\n")
        return

    print("\nThe note deleted will be permanently removed. \n")

    try:
        note_index = int(input("\nEnter note number to delete : "))
    except ValueError:
        print("Note number should be a valid number")
        return

    for index, note in enumerate(notes_list):
        if note_index == index + 1:
            removed = notes_list.pop(index)

            save_file_helper(notes_list)
            print(f"Note '{removed['Title']}' is deleted from your notes.")
            break
    else:
        print(f"Note number {note_index} not found.")


# Search note or view note
def search_note(notes_list):
    if not notes_list:
        print("No note added yet.\n")
        return

    try:
        note_index = int(input("\nEnter note number to search : "))
    except ValueError:
        print("Note number should be a valid number")
        return

    for index, note in enumerate(notes_list):
        if note_index == index + 1:
            print(f"Searching for note number {note_index} ......")
            print(f"\n Note Number : {note_index} \n")
            print("*" * 40)
            print(f"Title : ")
            print(f"\t {note['Title']}")

            print(f"Description :")
            print(f"\t {note['Description']} \n")

            print(f"Added on date : ", end=" ")
            print(f"{note['Date_add']}")

            print(f"Added at time : ", end=" ")
            print(f"{note['Time_add']}")

            try:
                last_edit = note["Edit date"]
                print(f"Last edited : ", end=" ")
                print(f"{last_edit}")

            except KeyError:
                pass

            print("*" * 40)
            break
    else:
        print(f"Note number {note_index} not found.")


# Executing the note entered by the user
def main():
    while True:
        notes_list = load_data()
        display_menu()
        user_choice = menu_choose_note()

        match user_choice:
            case "1":
                add_note(notes_list)
                time.sleep(2)
            case "2":
                view_all_notes(notes_list)
                time.sleep(2)
            case "3":
                edit_note(notes_list)
                time.sleep(2)
            case "4":
                delete_note(notes_list)
                time.sleep(2)
            case "5":
                search_note(notes_list)
                time.sleep(2)
            case "6":
                print("Exiting the program.....")
                break


# Running for main file
if __name__ == "__main__":
    main()


# ========== PROJECT END ============
