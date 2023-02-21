from django.shortcuts import render, redirect
from books.models import Book



def index(request):
    return redirect('books')


def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': books
    }
    return render(request, template, context)


def book(request, pub_date):
    template = 'books/books_list.html'
    obj = Book.objects
    books_objects = obj.filter(pub_date=pub_date)
    books_next = obj.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    books_previous = obj.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    context = {
        'books': books_objects,
        'next_book': books_next,
        'previous_book': books_previous,
    }
    return render(request, template, context)
