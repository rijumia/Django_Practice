from django.shortcuts import render, redirect


def loginPage(request):
    return render(request, 'login.html')

def signupPage(request):
    return render(request, 'signup.html')

def changePasswordPage(request):
    return render(request, 'changePassword.html')

def logoutPage(request):
    return redirect('loginPage')


def homePgae(request):
    return render(request, 'home.html')

def jobFeedPgae(request):
    return render(request, 'jobFeed.html')

def addJobPgae(request):
    return render(request, 'addJob.html')
