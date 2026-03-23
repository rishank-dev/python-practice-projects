# Smart To-Do Manager (v2.0)

## Overview
Smart To-Do Manager is a command-line based task management application built using Python. This version improves upon the initial release by introducing structured data storage, better task tracking, and an improved user interface.

Tasks are stored using JSON format, making the system more reliable and scalable compared to plain text storage.

---

## Features
- Add tasks with title, priority, and due date  
- View all tasks in a structured table format  
- Update existing tasks  
- Mark tasks as completed (tracked using status)  
- Delete tasks permanently  
- Search tasks by task number  
- Persistent storage using JSON  
- Improved CLI display using tabular format  

---

## Project Structure
```
Smart-To-Do-Manager/
│
├── to_do_manager.py
├── task_sample.txt
├── tasks_sample.txt
└── README.md
```

---

## How to Run
1. Make sure Python is installed  
2. Install required dependency:

```
pip install tabulate
```

3. Run the program:

```
python to_do_manager.py
```

4. Follow the menu options in the terminal  

---

## Technologies Used
- Python  
- JSON (for data storage)  
- Tabulate library (for table display)  
- Command Line Interface (CLI)  

---

## Improvements from v1.0
- Switched from plain text storage to JSON format  
- Added task status (Pending / Completed)  
- Improved input validation  
- Better user interface using table format  
- Cleaner and more structured code  

---

## Notes
This version focuses on improving reliability, usability, and structure. It represents a transition from a basic beginner project to a more structured intermediate-level application.

Future versions may include advanced features such as filtering, sorting, and graphical user interface (GUI).
