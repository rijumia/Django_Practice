from django.contrib import admin
from django.urls import path
from to_do_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
]
