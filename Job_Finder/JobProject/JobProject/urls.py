from django.contrib import admin
from django.urls import path
from JobApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginPage, name='loginPage'),
    path('register/', signupPage, name='signupPage'),
    path('changePassword/', changePasswordPage, name='changePasswordPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('homePgae/', homePgae, name='homePgae'),
    path('jobFeedPgae/', jobFeedPgae, name='jobFeedPgae'),
    path('addJobPgae/', addJobPgae, name='addJobPgae'),
]
