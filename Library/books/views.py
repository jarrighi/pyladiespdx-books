from django.http import Http404
from django.shortcuts import render

from .models import Book


def book_list_view(request):
    return render(request, 'books/book_list.html', {
        'books': Book.objects.all()
    })


def book_detail_view(request, slug):
    try:
        book = Book.live.get(slug=slug)
    except Book.DoesNotExist:
        raise Http404("That post doesn't exist")

    return render(request, 'books/book_detail.html', {
        'book': book
    })