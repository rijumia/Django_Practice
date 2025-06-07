from django.contrib import admin
from django.urls import path
from userProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='home'),
]
