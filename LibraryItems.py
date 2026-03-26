class LibraryItem:
    def __init__(self, item_id, title, copies):
        self.item_id = item_id
        self.title = title
        self.copies = copies

    def display_info(self):
        return f"Item ID: {self.item_id}, Title: {self.title}, Copies: {self.copies}"


# Book subclass
class Book(LibraryItem):
    def __init__(self, item_id, title, author, copies):
        super().__init__(item_id, title, copies)
        self.author = author

    def display_info(self):
        return f"Book ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Copies: {self.copies}"


# DVD subclass
class DVD(LibraryItem):
    def __init__(self, item_id, title, director, copies):
        super().__init__(item_id, title, copies)
        self.director = director

    def display_info(self):
        return f"DVD ID: {self.item_id}, Title: {self.title}, Director: {self.director}, Copies: {self.copies}"


# Game subclass
class Game(LibraryItem):
    def __init__(self, item_id, title, platform, copies):
        super().__init__(item_id, title, copies)
        self.platform = platform

    def display_info(self):
        return f"Game ID: {self.item_id}, Title: {self.title}, Platform: {self.platform}, Copies: {self.copies}"