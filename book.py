class Book:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, title, author, synopsis, rating, notes, id = None):
        self.id = id
        self.title = title
        self.author = author
        self.synopsis = synopsis
        self.rating = rating
        self.notes = notes        

    # This tells Python how to compare two Books. 
    # Without this, Python only checks if they are the same object in memory. 
    # With this, it checks if their data (like title and author) matches.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This controls what you see when you print(book).
    # Instead of seeing a confusing code like <Book object at 0x102...>, 
    # you'll see the actual ID, title, and author, which is much more useful to us humans
    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author}, {self.synopsis}, {self.rating}, {self.notes})"