from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.apps.books.models import Book
from src.apps.books.api.serializers import (
    AllBookSerializer,
    CreateBookSerializer,
    DetailBookSerializer,
)
from src.apps.base.api.mixins import SerializerPerAction


class BookModelViewSet(SerializerPerAction, viewsets.ModelViewSet):
    queryset = Book.objects.all()
    action_serializers = {
        "default": AllBookSerializer,
        "retrieve": DetailBookSerializer,
        "create": CreateBookSerializer,
        "update": DetailBookSerializer,
    }
    permission_classes = (IsAuthenticated,)
