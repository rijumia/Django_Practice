from django.shortcuts import render
from instituteApp.models import CustomUserModel, TeacherModel, StudentModel

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        usertype = request.POST.get('usertype')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        if password == confirm_password:
            user = Cus

    return render(request, 'register.html')
