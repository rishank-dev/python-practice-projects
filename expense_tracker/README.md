# Monthly Expense Tracker (CLI) - v1.0

A simple and efficient **Command-Line Expense Tracker** built using Python.  
This project helps users record, manage, and analyze their daily expenses with a focus on **monthly reporting**.

---

## Features

- ➕ Add new expenses with category and description  
- 📋 View all recorded expenses in a structured table  
- ❌ Delete expenses easily  
- 📅 Generate monthly expense reports  
- 📊 View category-wise expense summary  
- 💾 Persistent storage using JSON 
- 🖥️ Clean CLI interface using tabulated output  

---

## 🧱 Project Structure

expense-tracker/
│── expense_file.txt     # Stores expense data (JSON format)
│── expense_tracker.py              # Main application file
│── README.md            # Project documentation

---

## 📌 Expense Data Fields

Each expense entry contains:

- Amount (in Rs.)
- Category (food, travel, bill, shopping, other)
- Description
- Date Added
- Time Added

---

## 🛠️ Technologies Used

- Python 3  
- JSON (for data storage)  
- Tabulate (for CLI table display)  
- Datetime module  

---

## ▶️ How to Run

1. Clone the repository:
   git clone https://github.com/your-username/expense-tracker.git

2. Navigate to the project folder:
   cd expense-tracker

3. Run the program:
   python main.py

---

## 📸 Sample Menu

--------------- Menu ---------------

1. Add Expense  
2. View Expenses  
3. Delete Expense  
4. Monthly Report  
5. Category Summary  
6. Exit  

------------------------------------

---

## ⚠️ Limitations (v1.0)

- Amount stored as formatted string (limits calculations)  
- No edit/update feature  
- No unique ID system  
- Limited analytics in reports  

---

## 🔮 Future Improvements (v2.0)

- 💰 Budget tracking system  
- 📈 Graphical reports (matplotlib)  
- 🔍 Search and filter options  
- ✏️ Edit expense functionality  
- 🆔 Unique ID system  
- 📊 Advanced monthly analytics  

---

## 🎯 Learning Outcomes

This project demonstrates:

- File handling with JSON  
- Modular programming  
- CLI application design  
- Basic data analysis  
- Input validation techniques  

---

## 🤝 Contributing

This is a beginner-friendly project. Contributions, suggestions, and improvements are welcome!

---

## 📄 License

This project is open-source.

---

## 👨‍💻 Author

Developed by *[Rishank Gupta]*
