from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("author/", views.author, name='author'),
    path("add_author/", views.add_author, name='add_author'),
    path("author_detail/<int:pk>", views.author_detail, name='author_detail'),
    path("delete_author/<int:pk>", views.delete_author, name='delete_author'),
    path("update_author/<int:pk>", views.update_author, name='update_author'),
    path("book/", views.book, name='book'),
    path("add_book/", views.add_book, name='add_book'),
    path("book_detail/<int:pk>", views.book_detail, name='book_detail'),
    path("delete_book/<int:pk>", views.delete_book, name='delete_book'),
    path("update_book/<int:pk>", views.update_book, name='update_book'),
]
