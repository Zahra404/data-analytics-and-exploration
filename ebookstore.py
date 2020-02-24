import sqlite3
import sys  # import system so you can exit program

db = sqlite3.connect("ebookstore")
cursor = db.cursor()
try:
    cursor.execute('''CREATE TABLE IF NOT EXISTS books
    (ID INTEGER PRIMARY KEY, Title TEXT, Author TEXT, QTY INTEGER)''')
    db.commit()
except table_already_exists:
    pass


# function to enter a book
def enter_book(ID, Title, Author, QTY):
    cursor.execute('''INSERT INTO books(ID, Title, Author, QTY) VALUES(?,?,?,?)''', (ID, Title, Author, QTY))
    print(Title + " by " + Author + " was added to bookshelf")
    db.commit()


# only update the QTY as that's the only thing that can be edited on a book
def update_book(ID, Title, Author, QTY):
    cursor.execute('''UPDATE books SET Title=? WHERE ID=? ''', (Title, ID,))
    cursor.execute('''UPDATE books SET Author=? WHERE ID=?''', (Author, ID,))
    cursor.execute('''UPDATE books SET QTY=? WHERE ID=?''', (QTY, ID,))
    print(f"{ID} Has been updated")
    db.commit()


# delete books from database
def delete_book(ID, Title):
    cursor.execute('''DELETE FROM books WHERE ID=?
    ''', (ID,))
    print(Title + " has been deleted ")
    db.commit()


# search database for book (select/fetchall/fetchone)
def search_books(title):
    cursor.execute('''SELECT * FROM books WHERE title=?  
    ''', (title,))
    search = cursor.fetchall()
    print(f"All the books found with the name '\n' {search}")


# added a bookshelf to view books you have entered
def bookshelf():
    cursor.execute('''SELECT * FROM books''')
    bookonshelf = cursor.fetchall()
    print(bookonshelf)


# def to exit
def egress():
    print("Exiting bookshelf ")
    sys.exit()


# input question to receive instruction
while True:
    instruction = int(input("would you like to \nEnter Book(1) \nUpdate Book(2) \nDelete Book(3) \nSearch Book(4) "
                            "\nBookshelf(5) \nExit(0) \n"))
    if instruction == 1:
        try:
            Ident = int(input("ID "))
            bTitle = input("Title ").title()
            bAuthor = input("Author ").title()
            bQTY = int(input("Quantity "))
            enter_book(Ident, bTitle, bAuthor, bQTY)
        except Exception as e:
            pass

    if instruction == 2:
        try:
            Ident = int(input("ID of book"))
            bTitle = input("Updated Title ").title()
            bAuthor = input("Updated Author ").title()
            bQTY = int(input("Updated Quantity "))
            update_book(Ident, bTitle, bAuthor, bQTY)
        except Exception as e:
            pass

    if instruction == 3:
        Ident = int(input("ID "))
        bTitle = input("Title ").title()
        delete_book(Ident, bTitle)

    if instruction == 4:
        try:
            bookTitle = input("name ")
            search_books(bookTitle.title())
        except Exception as e:
            print("There are no books found with the name " + btitle)

    if instruction == 5:
        bookshelf()

    if instruction == 0:
        db.close()
        egress()

    db.commit()
