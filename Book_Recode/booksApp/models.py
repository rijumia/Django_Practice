from django.db import models

class booksModel(models.Model):
    BooksCover = models.ImageField(upload_to='Media/CoverPic')
    BookTitle = models.CharField(max_length=100)
    BookAuthor = models.CharField(max_length=100)
    BookDescription = models.TextField()
    BookPrice = models.DecimalField(max_digits=10, decimal_places=2)
