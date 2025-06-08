from django.shortcuts import render


def homePage(request):
    return render(request, 'home.html')

def addPage(request):
    return render(request, 'addUser.html')

def listPage(request):
    return render(request, 'userList.html')

def editPage(request):
    return render(request, 'userUpdate.html')

def viewPage(request):
    return render(request, 'userDetails.html')
