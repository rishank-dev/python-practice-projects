# Smart Notes Manager (v1.0)

A simple terminal-based Notes Manager application built using Python.  
This project allows users to create, view, edit, delete, and search notes with file-based storage.

---

## Features

- Add new notes with title and description
- View all saved notes in a structured table format
- Edit existing notes
- Delete notes permanently
- Search notes by keyword or note number
- Automatic date and time tracking
- Persistent storage using JSON file

---

## Technologies Used

- Python
- JSON (for file storage)
- Tabulate (for table display)

---

## File Structure

- `notes_sample.txt` → Stores all notes data
- `main.py` → Main application file

---

## How It Works

1. On startup, the app loads notes from the file
2. Displays a menu with available options
3. User selects an option
4. App performs the operation
5. Changes are saved to file
6. Loop continues until user exits

---

## Menu Options

1. Add a new note  
2. View all notes  
3. Edit a note  
4. Delete a note  
5. Search for a note  
6. Exit  

---

## Data Format

Each note is stored as a dictionary with:

- Title  
- Description  
- Date_added  
- Time_added  
- (Optional) Date_edited  

---

## Limitations (v1.0)

- No unique ID system (uses index-based selection)
- Basic search functionality
- No categories or tags
- Terminal-based UI only

---

## Future Improvements

- Add unique ID for each note
- Advanced search (by keyword)
- Tags and categories
- Sorting and filtering
- Backup and restore system
- GUI version

---

## Author

Rishank Gupta
