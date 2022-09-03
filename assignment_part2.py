
class Book:
    def __init__(self, author, title):
        """
        Constructor of a Book class
        :param name: The name of the author
        :param team: The title of the book
        """
        self.author = author
        self.title = title

    def display(self):
        """ Display the author and book title"""
        print(f'{self.title} written by {self.author} ')


if __name__ == "__main__":
    a1 = Book('John Steinbeck', 'Of Mice and Men')
    a2 = Book('Harper Lee', "To Kill a Mockingbird")

    a1.display()
    a2.display()
