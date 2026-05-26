# 📚 Library Management System

A Python-based Library Management System built using Object-Oriented Programming concepts. Supports adding, removing, searching, checking out, and returning books — with data persistence using JSON.

---

## ✨ Features

- Add Physical Books and EBooks separately
- Checkout and return books with availability tracking
- Search books by author
- Remove books from the library
- Data persistence — books are saved and restored using JSON
- Built with OOP — inheritance, encapsulation, composition

---

## 🗂️ Project Structure

```
library-management-system/
├── design.py       # Book, PhysicalBook, EBook, Library classes
├── main.py         # Menu-driven interface
├── library.json    # Auto-generated data file
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository
```bash
   git clone <yhttps://github.com/hima933/Library-Management-System.git>
   cd library-management-system
```

2. No external dependencies — uses Python built-in libraries only

3. Run the program
```bash
   python main.py
```

---

## 🖥️ Sample Output

```
--Library Menu--
1. Add Physical Book
2. Add EBook
3. Checkout Book
4. Return Book
5. Search by Author
6. Show All Books
7. Remove Book
8. Exit

Enter Your Choice: 1
Enter Title: Fluent Python
Enter Author: Luciano Ramalho
Enter ISBN: 005
Enter Shelf Location: A3
✅ Physical Book Added Successfully!
```

---

## 🧠 What I Learned

- Implementing OOP concepts — classes, inheritance, composition, encapsulation
- Using `super()` to extend base class functionality
- Data persistence with `json.dump()` and `json.load()`
- Error handling with `try/except`
- Organizing code into classes and modules
- Building a complete working project end to end

---

## 🛠️ Technologies Used

- Python 3
- JSON (built-in)
- VS Code

---
