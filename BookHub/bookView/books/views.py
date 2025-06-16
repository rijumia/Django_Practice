from django.shortcuts import render

def home(req):
    return render(req, 'home.html')

def all_books(req):
    return render(req, 'allbook.html')

def add_book(req):
    return render(req, 'addbook.html')

def update_book(req):
    return render(req, 'updatebook.html')