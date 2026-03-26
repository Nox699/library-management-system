"# library-management-system"



Description:

This project is a Library Management System in Python using object oriented programming.  

It allows users to manage library items such as books, DVDs, and games, as well as members and borrowing and returning items.







Features:

\- Add, remove, and update library items,Book, DVD, Game

\- Add, remove, and update members

\- Issue items to members

\- Return items

\- Display all items and members

\- Error handling for invalid operations





Structure:

The project is divided into multiple files:



\- library.py Handles library functions

\- libraryitems.py Contains LibraryItem, Book, DVD, Game classes

\- members.py Contains Member class

\- main.py Runs the program

\- test\_library.py Contains pytest





Design:

* Dictionares are used to store items and members using IDs 
* Lists are used to store borrowed items for each member
* Inheritence is used with a base class libraryitems and subclasses such as book, dvd and game
* polymorphism is used by having the same method Display\_info() in different classes.
Each class uses this method in its own way. So the program can use the same function name but get different results depending on the item.
* the system seperates classes and methods for functionallity 





How to Run



Run the main program:

bash

python main.py

install pytest:
bash
pip install pytest

to run pytest:
bash 
pytest

