from django.db import models

# Create your models here.
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    title =  CharField(max_length=200)
    author = CharField(max_length=100)
    publication_year = IntegerField()
