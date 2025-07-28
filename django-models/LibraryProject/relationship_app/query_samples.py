from LibraryProject.relationship_app.models import Author, Book, Library, Librarian

# Sample data (if not already created)
author = Author.objects.get_or_create(name="George Orwell")[0]
book1 = Book.objects.get_or_create(title="1984", author=author)[0]
book2 = Book.objects.get_or_create(title="Animal Farm", author=author)[0]
library = Library.objects.get_or_create(name="Central Library")[0]
library.books.set([book1, book2])
librarian = Librarian.objects.get_or_create(name="John Doe", library=library)[0]

# 1. Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# 2. List all books in a library
books_in_library = library.books.all()
print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

# 3. Retrieve the librarian for a library
librarian_for_library = Librarian.objects.get(library=library)
print(f"Librarian for {library.name}: {librarian_for_library.name}")

