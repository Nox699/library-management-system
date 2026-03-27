from LibraryItems import Book, DVD, Game
from Members import Member
from Library import Library
import pytest

def test_add_item():
    library = Library()
    book = Book(1, "The Anarchist cookbook", "William Powell", 3)

    library.add_item(book)

    assert 1 in library.items
    assert library.items[1].title == "The Anarchist cookbook"


def test_add_member():
    library = Library()

    library.add_member(101, "Tom")

    assert 101 in library.members
    assert library.members[101].name == "Tom"
    
def test_issue_item():
    library = Library()

    library.add_item(Book(1, "The Anarchist cookbook", "William Powell", 2))
    library.add_member(101, "Tom")

    library.issue_item(1, 101)

    assert library.items[1].copies == 1
    assert 1 in library.members[101].borrowed_items
    
def test_return_item():
    library = Library()

    library.add_item(Book(1, "The Anarchist cookbook", "William Powell", 2))
    library.add_member(101, "Tom")

    library.issue_item(1, 101)
    library.return_item(1, 101)

    assert library.items[1].copies == 2
    assert 1 not in library.members[101].borrowed_items
    
def test_remove_item():
    library = Library()

    library.add_item(Book(1, "The Anarchist cookbook", "William Powell", 2))
    library.remove_item(1)

    assert 1 not in library.items
    
def test_remove_member():
    library = Library()

    library.add_member(101, "Tom")
    library.remove_member(101)

    assert 101 not in library.members


def test_issue_no_copies():
    library = Library()

    library.add_item(Book(1, "The Anarchist cookbook", "William Powell", 0))
    library.add_member(101, "Tom")

    library.issue_item(1, 101)

    assert library.items[1].copies == 0


def test_return_not_borrowed():
    library = Library()

    library.add_item(Book(1, "The Anarchist cookbook", "William Pp13owell", 2))
    library.add_member(101, "Tom")

    with pytest.raises(ValueError):
        library.members[101].return_item(1)