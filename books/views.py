from django.shortcuts import render, redirect
from django.core.paginator import Paginator
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
    obj = Book.objects
    template = 'books/books_list.html'

    paginator = Paginator(obj.all().order_by('pub_date'), 1)
    page_str = obj.get(pub_date=pub_date).pub_date
    page = paginator.get_page(page_str)
    ...

    context = {
        'books': obj.filter(pub_date=pub_date),
        # 'page': page,
    }
    return render(request, template, context)
