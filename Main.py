from Library import Library
from LibraryItems import Book, DVD, Game
from Members import Member


def main():
    library = Library()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Add DVD")
        print("3. Add Game")
        print("4. Remove Item")
        print("5. Update Item")
        print("6. Display Items")
        print("7. Add Member")
        print("8. Remove Member")
        print("9. Update Member")
        print("10. Display Members")
        print("11. Issue Item")
        print("12. Return Item")
        print("13. Exit")

        choice = input("Enter a number: ")

        if choice == "1":
            item_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            copies = int(input("Enter Copies: "))
            library.add_item(Book(item_id, title, author, copies))

        elif choice == "2":
            item_id = int(input("Enter DVD ID: "))
            title = input("Enter Title: ")
            director = input("Enter Director: ")
            copies = int(input("Enter Copies: "))
            library.add_item(DVD(item_id, title, director, copies))

        elif choice == "3":
            item_id = int(input("Enter Game ID: "))
            title = input("Enter Title: ")
            platform = input("Enter Platform: ")
            copies = int(input("Enter Copies: "))
            library.add_item(Game(item_id, title, platform, copies))

        elif choice == "4":
            item_id = int(input("Enter Item ID to remove: "))
            library.remove_item(item_id)

        elif choice == "5":
            item_id = int(input("Enter Item ID to update: "))
            item_type = input("Enter item type (book/dvd/game): ").lower()

            title = input("Enter new title (leave blank to keep same): ")
            copies_input = input("Enter new copies (leave blank to keep same): ")
            copies = int(copies_input) if copies_input else None

            if item_type == "book":
                author = input("Enter new author (leave blank to keep same): ")
                library.update_item(item_id, title=title or None, copies=copies, author=author or None)

            elif item_type == "dvd":
                director = input("Enter new director (leave blank to keep same): ")
                library.update_item(item_id, title=title or None, copies=copies, director=director or None)

            elif item_type == "game":
                platform = input("Enter new platform (leave blank to keep same): ")
                library.update_item(item_id, title=title or None, copies=copies, platform=platform or None)

            else:
                print("Invalid item type")

        elif choice == "6":
            library.display_items()

        elif choice == "7":
            member_id = int(input("Enter Member ID: "))
            name = input("Enter Name: ")
            library.add_member(member_id, name)

        elif choice == "8":
            member_id = int(input("Enter Member ID to remove: "))
            library.remove_member(member_id)

        elif choice == "9":
            member_id = int(input("Enter Member ID to update: "))
            name = input("Enter new name: ")
            library.update_member(member_id, name)

        elif choice == "10":
            library.display_members()

        elif choice == "11":
            item_id = int(input("Enter Item ID: "))
            member_id = int(input("Enter Member ID: "))
            library.issue_item(item_id, member_id)

        elif choice == "12":
            item_id = int(input("Enter Item ID: "))
            member_id = int(input("Enter Member ID: "))
            library.return_item(item_id, member_id)

        elif choice == "13":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try 1-13")

if __name__ == "__main__":
    main()