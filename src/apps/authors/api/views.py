from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.apps.authors.models import Author
from src.apps.authors.api.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)
