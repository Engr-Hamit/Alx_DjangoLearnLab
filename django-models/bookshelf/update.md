# Update Book Title

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title  # "Nineteen Eighty-Four"

