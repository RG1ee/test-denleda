from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from src.apps.books.api.views import BookModelViewSet
from src.apps.authors.api.views import AuthorViewSet

router = SimpleRouter()
router.register("books", BookModelViewSet)
router.register("authors", AuthorViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include("src.apps.api_auth.api.urls")),
]
