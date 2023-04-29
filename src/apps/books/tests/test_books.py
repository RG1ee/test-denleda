import pytest
from model_bakery import baker

from rest_framework import status
from rest_framework.reverse import reverse

from src.apps.books.models import Book


@pytest.mark.django_db
def test_get_book(api_client):
    client = api_client()
    user = baker.make_recipe("authors.author")

    response = client.get(reverse("book-list"))
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    response = client.get(reverse("book-list"))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_post_book(api_client):
    client = api_client()
    user = baker.make_recipe("authors.author")

    data_for_books = {
        "title": "Test Book",
        "description": "Desc Book",
    }

    response = client.post(reverse("book-list"), data=data_for_books, format="json")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    response = client.post(reverse("book-list"), data=data_for_books, format="json")
    assert response.status_code == status.HTTP_201_CREATED

    book = Book.objects.last()
    assert book.author.username == user.username


@pytest.mark.django_db
def test_retrieve_book(api_client):
    client = api_client()
    user = baker.make_recipe("authors.author")
    book = baker.make_recipe("books.book")

    response = client.get(reverse("book-detail", kwargs={"pk": book.id}))
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    response = client.get(reverse("book-detail", kwargs={"pk": book.id}))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_book(api_client):
    client = api_client()
    user = baker.make_recipe("authors.author")
    book = baker.make_recipe("books.book")

    data_for_update = {
        "title": "New Title",
        "description": "New description",
    }

    response = client.patch(
        reverse("book-detail", kwargs={"pk": book.id}),
        data=data_for_update,
        format="json",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    response = client.put(
        reverse("book-detail", kwargs={"pk": book.id}),
        data=data_for_update,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK

    book = Book.objects.last()
    assert book.title == data_for_update["title"]
    assert book.description == data_for_update["description"]


@pytest.mark.django_db
def test_delete_book(api_client):
    client = api_client()
    user = baker.make_recipe("authors.author")
    book = baker.make_recipe("books.book")

    response = client.delete(reverse("book-detail", kwargs={"pk": book.id}))
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    client.force_authenticate(user)
    response = client.delete(reverse("book-detail", kwargs={"pk": book.id}))
    assert response.status_code == status.HTTP_204_NO_CONTENT
