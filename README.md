# **Terminal-Based Text Editor**

Welcome to my terminal-based text editor project! This project is a personal challenge where I am building a text editor from scratch using Python. I will document my learning process and share my progress, hoping we can all learn together.

---

## **Project Overview**

This text editor is a basic, terminal-based tool that allows users to write, edit, and save text files. It captures keypresses, supports basic text editing, and provides file handling (save/load functionality). The project is being built incrementally with the following core features:

### **Current Features**:
1. **Main Menu**: Allows users to create a new file, open an existing one, or exit the program through a simple interface.


---

## **Planned Features**:
- **Real-time Keypress Handling**: Captures input and displays typed characters in the terminal.
- **Cursor Movement**: Move the cursor using arrow keys.
- **Text Insertion**: Insert characters at the cursor position.
- **Text Deletion**: Support for `Backspace` and `Delete`.
- **File Handling**: Load an existing text file and save the current buffer to a file.
- **Undo/Redo**: Implement basic undo/redo functionality.
- **Advanced Editing**: Support for text selection, cut/copy/paste.
- **Search and Replace**: Add a simple search-and-replace feature.

---

## **Learning and Updates**

I will be sharing regular updates about my progress, including lessons learned and challenges faced. You can follow my journey and updates on LinkedIn (or any other platform).

---

## **How to Run the Project**

### **Prerequisites**:
- Python 3.x
- The `curses` library (installed by default in Linux/macOS)

### **To Run the Project**:
1. **Clone the repository**:
    ```bash
    git clone https://github.com/nekefer/Text-Editor.git
    cd Text-Editor
    ```

2. **Run the text editor**:
    ```bash
    python main.py
    ```

3. **Upcoming usage**:
   - **Arrow Keys**: Move the cursor.
   - **Enter**: Create a new line.
   - **Backspace**: Delete the character before the cursor.
   - **Delete**: Delete the character at the cursor position.
   - **Ctrl+S**: Save the file.
   - **Ctrl+O**: Open a file.
   - **Ctrl+Q**: Quit the editor.

