from django.db import models

# Author model represents a book's author.
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's full name

    def __str__(self):
        return self.name


# Book model represents a book and links to an Author.
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book's title
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(
        Author,
        related_name='books',  # Allows reverse access: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

