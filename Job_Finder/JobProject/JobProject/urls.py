from django.contrib import admin
from django.urls import path
from JobApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('register/', signupPage, name='signupPage'),
    path('changePassword/', changePasswordPage, name='changePasswordPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('profile/', profilePage, name='profilePage'),    

    path('homePage/', homePage, name='homePage'),
    path('jobFeedPage/', jobFeedPage, name='jobFeedPage'),
    path('addJobPage/', addJobPage, name='addJobPage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
