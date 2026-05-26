from design import PhysicalBook,EBook,Library

def main():
    library=Library()
    library.load_from_json()
    while True:
        print("--Library Menu--\n")
        print("1.Add Physical Book")
        print("2.Add EBook")
        print("3.Checkout Book")
        print("4.Return Book")
        print("5.Search by Author")
        print("6.Show All Books")  
        print("7.Remove Book")
        print("8.Exit")
        
        choice=input("Enter Your Choice:")
        if choice=="1":
            title=input("Enter Title:")
            author=input("Enter Author:")
            isbn=input("Enter ISBN:")
            available=True
            shelf_location=input("Enter Shelf Location:")
            book=PhysicalBook(title,author,isbn,available,shelf_location)
            library.add_book(book)
            library.save_to_json()
            print("✅ Physical Book Added Successfully!")
        elif choice=="2":
            title=input("Enter Title:")
            author=input("Enter Author:")
            isbn=input("Enter ISBN:")
            available=True
            file_size_mb=float(input("Enter File Size (MB):"))
            ebook=EBook(title,author,isbn,available,file_size_mb)
            library.add_book(ebook)
            library.save_to_json()
            print("✅ EBook Added Successfully!")
        elif choice=="3":
            isbn=input("Enter ISBN to Checkout:")
            print(library.checkout_book(isbn))
        elif choice=="4":
            isbn=input("Enter ISBN to Return:")
            print(library.return_book(isbn))
        elif choice=="5":
            author=input("Enter Author to Search:")
            library.search_by_author(author)
        elif choice=="6":
            library.list_available_books()
        elif choice=="7":
            isbn=input("Enter ISBN to Remove:")
            print(library.remove_book(isbn))
            library.save_to_json()
        elif choice=="8":
            library.save_to_json()
            print("Exiting...")
            break
        else:
            print("Invalid Choice. Please Try Again.")
    
if __name__=="__main__":
    main()
