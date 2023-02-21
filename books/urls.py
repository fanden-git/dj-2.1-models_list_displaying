from django.urls import path
from .views import index, books_view, book


urlpatterns = [
    path('', index),
    path('books/', books_view, name='books'),
    path('books/<str:pub_date>', book, name='book'),
]
