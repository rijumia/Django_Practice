from django.contrib import admin
from django.urls import path
from books.views import home, all_books, add_book, update_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('allbooks/', all_books, name='all_books'),
    path('addbook/', add_book, name='add_book'),
    path('updatebook/', update_book, name='update_book'),
]
