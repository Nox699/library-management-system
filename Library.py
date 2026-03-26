# Library class
from Members import Member
from LibraryItems import Book, DVD, Game

class Library:
    def __init__(self):
        self.items = {} #dictionaries
        self.members = {} #dictionaries

    # Add a new item
    def add_item(self, item):
        if item.item_id in self.items:
            print("Item ID already exists")
        else:
            self.items[item.item_id] = item
            print("Item added successfully")

    # Remove an item
    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item removed successfully")
        else:
            print("Item not found")

    # Update an item
    def update_item(self, item_id, title=None, copies=None, author=None, director=None, platform=None):
        if item_id not in self.items:
            print("Item not found")
            return

        item = self.items[item_id]

        if title is not None:
            item.title = title
        if copies is not None:
            item.copies = copies

        if isinstance(item, Book) and author is not None:
            item.author = author
        elif isinstance(item, DVD) and director is not None:
            item.director = director
        elif isinstance(item, Game) and platform is not None:
            item.platform = platform

        print("Item updated successfully")

    # Show all items
    def display_items(self):
        if not self.items:
            print("No items in the library")
        else:
            for item in self.items.values():
                print(item.display_info())

    # Add a new member
    def add_member(self, member_id, name):
        if member_id in self.members:
            print("Member ID already exists")
        else:
            self.members[member_id] = Member(member_id, name)
            print("Member added successfully")

    # Remove a member 
    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            print("Member removed successfully")
        else:
            print("Member not found")

    # Update member
    def update_member(self, member_id, name=None):
        if member_id not in self.members:
            print("Member not found")
            return

        if name is not None:
            self.members[member_id].name = name

        print("Member updated successfully")

    # Show all members
    def display_members(self):
        if not self.members:
            print("No members in the library")
        else:
            for member in self.members.values():
                print(member.display_info())

    # Issue an item
    def issue_item(self, item_id, member_id):
        if item_id not in self.items:
            print("Item not found")
            return

        if member_id not in self.members:
            print("Member not found")
            return

        item = self.items[item_id]
        member = self.members[member_id]

        if item.copies <= 0:
            print("No copies available")
            return

        item.copies -= 1
        member.borrow_item(item_id)
        print(f"{item.title} issued to {member.name}")

    # Return an item from a member
    def return_item(self, item_id, member_id):
        if item_id not in self.items:
            print("Item not found")
            return

        if member_id not in self.members:
            print("Member not found")
            return

        item = self.items[item_id]
        member = self.members[member_id]

        try:
            member.return_item(item_id)
            item.copies += 1
            print(f"{item.title} returned by {member.name}")
        except ValueError as e:
            print(e)