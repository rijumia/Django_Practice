from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from to_do_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('registerPage/', registerPage, name='registerPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('changePassword/', changePassword, name='changePassword'),
    path('homePage', homePage, name='homePage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
