from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Author, Book
from .forms import AddAuthorForm, AddBookForm

def home(request):
    # return HttpResponse("<h1>Hello World!<h1/>")
    return render(request, "home.html")

def author(request):
    authors = Author.objects.all()
    return render(request, "author.html", {'authors':authors})

def add_author(request):
    form = AddAuthorForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('author')
    return render(request, "add_author.html", {'form':form})

def author_detail(request, pk):
    author = Author.objects.get(id=pk)
    return render(request, "author_detail.html", {'author':author})

def delete_author(request, pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return redirect('author')

def update_author(request, pk):
    curr_author = Author.objects.get(id=pk)
    form = AddAuthorForm(request.POST or None, instance=curr_author)
    if form.is_valid():
        form.save()
        return redirect('author')
    return render(request, "update_author.html", {'form':form})

def book(request):
    books = Book.objects.all()
    authors = Author.objects.all().distinct()
    return render(request, "book.html", {'books':books, 'authors': authors})

def add_book(request):
    form = AddBookForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('book')
    return render(request, "add_book.html", {'form':form})

def book_detail(request, pk):
    book = Book.objects.get(id=pk)
    return render(request, "book_detail.html", {'book':book})

def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('book')

def update_book(request, pk):
    curr_book = Book.objects.get(id=pk)
    form = AddBookForm(request.POST or None, instance=curr_book)
    if form.is_valid():
        form.save()
        return redirect('book')
    return render(request, "update_book.html", {'form':form})

