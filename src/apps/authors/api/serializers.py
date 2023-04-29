from rest_framework import serializers

from src.apps.authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "username",
            "first_name",
            "last_name",
            "date_of_birth",
        )
