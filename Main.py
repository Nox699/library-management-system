from Library import Library
from LibraryItems import Book, DVD, Game
from Members import Member


def main():
    library = Library()

    library.add_item(Book(1, "The Anarchist Cookbook", "William Powell", 3))
    library.add_item(DVD(2, "Inception", "Nolan", 2))
    library.add_item(Game(3, "FIFA 24", "PS5", 4))

    library.add_member(101, "Tom")
    library.add_member(102, "Emma")

    library.issue_item(1, 101)
    library.issue_item(2, 102)

    library.display_items()
    print()
    library.display_members()
    print()

    library.update_member(101, "Thomas")
    library.update_item(3, title="EA FC 24", platform="PlayStation 5")

    library.remove_item(2)
    library.remove_member(102)

    print()
    library.display_items()
    print()
    library.display_members()

if __name__ == "__main__":
    main()