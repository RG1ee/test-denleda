from django.db import models

from src.apps.authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title of Book")
    description = models.TextField(verbose_name="Book Description")
    date_of_publication = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"
