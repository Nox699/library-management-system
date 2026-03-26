class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item_id):
        self.borrowed_items.append(item_id)

    def return_item(self, item_id):
        if item_id in self.borrowed_items:
            self.borrowed_items.remove(item_id)
        else:
            raise ValueError("Item not borrowed")

    def display_info(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Borrowed Items: {self.borrowed_items}"