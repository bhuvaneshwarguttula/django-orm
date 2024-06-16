from django.db import models
from datetime import datetime

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
    
