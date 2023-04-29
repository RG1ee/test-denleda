from rest_framework import serializers

from src.apps.authors.api.serializers import AuthorSerializer
from src.apps.books.models import Book


class ListBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
        )


class DetailBookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "description",
            "date_of_publication",
            "author",
        )


class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "description",
        )

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)
