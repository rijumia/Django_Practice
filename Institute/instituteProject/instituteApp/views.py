from django.shortcuts import render

def registerPage(request):
    return render(request, 'register.html')
