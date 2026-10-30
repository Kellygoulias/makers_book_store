class User:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, username, password, id = None):
        self.id = id
        self.username = username
        self.password = password

    # This tells Python how to compare two Books. 
    # Without this, Python only checks if they are the same object in memory. 
    # With this, it checks if their data (like username and password) matches.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This controls what you see when you print(book).
    # Instead of seeing a confusing code like <User object at 0x102...>, 
    # you'll see the actual ID, username, and password, which is much more useful to us humans
    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.password})"