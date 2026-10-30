class Film:

    def __init__(self, id, title, release_year):
        self.id = id
        self.title = title
        self.release_year = release_year

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Film({self.id}, {self.title}, {self.release_year})"