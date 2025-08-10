from django.db import models

class Author(models.Model):
    """
    Represents a book author.
    Fields:
        name: Full name of the author.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book written by an author.
    Fields:
        title: Title of the book.
        publication_year: Year the book was published.
        author: Foreign key linking to the Author model (one author can have many books).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

