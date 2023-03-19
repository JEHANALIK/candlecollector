from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book , Bookmark
from django.views.generic.edit import CreateView , UpdateView , DeleteView 
from django.views.generic import ListView , DetailView 


def home(request):
    return render(request,'base.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html' , {'books':books})

def books_detail(request, book_id):
    books = Book.objects.get(id= book_id)

    bookmarks_book_doesnt_have = Bookmark.objects.exclude(id__in = books.bookmark.all().values_list('id'))

    return render(request, 'books/detail.html',{
        'books':books,
        'bookmarks': bookmarks_book_doesnt_have
        })


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'  


class BookUpdate(UpdateView):
    model = Book
    fields= ['type' , 'description' , 'language']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'


class BookmarkList(ListView):
    model = Bookmark

class BookmarkDetail(DetailView):
    model = Bookmark

class BookmarkCreate(CreateView):
    model = Bookmark
    fields = '__all__'

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['name' , 'color']

class BookmarkDelete(DeleteView):
    model = Bookmark
    success_url = '/bookmarks/'


# M:M
def assoc_bookmark(request, book_id , bookmark_id):
    Book.objects.get(id=book_id).bookmark.add(bookmark_id) 
    return redirect('detail' , book_id=book_id)

def unassoc_bookmark(request, book_id , bookmark_id):
    Book.objects.get(id=book_id).bookmark.remove(bookmark_id)
    return redirect('detail' , book_id=book_id)