from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    date_of_birth = models.DateField(
        verbose_name="Date of birthday",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
