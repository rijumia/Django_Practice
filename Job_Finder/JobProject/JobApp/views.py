from django.shortcuts import render, redirect


def loginPage(request):
    return render(request, 'login.html')

def signupPage(request):
    return render(request, 'signup.html')

def changePasswordPage(request):
    return render(request, 'changePassword.html')

def logoutPage(request):
    return redirect('loginPage')
