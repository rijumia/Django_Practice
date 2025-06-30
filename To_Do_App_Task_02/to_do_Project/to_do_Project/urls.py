from django.contrib import admin
from django.urls import path
from to_do_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('registerPage/', registerPage, name='registerPage'),
    path('homePage', homePage, name='homePage'),
]
