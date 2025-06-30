from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from to_do_App.models import CustomUserModel, ToDoModel
from django.contrib.auth.hashers import check_password

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        
    return render(request, 'login.html')

def registerPage(request):
    if request.method == 'POST':
        user_image = request.FILES.get('user_image')
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        phone_number = request.POST.get('phone_number')
        city_name = request.POST.get('city_name')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_image=user_image,
                full_name=full_name,
                bio=bio,
                phone_number=phone_number,
                city_name=city_name,
                address=address
            )
            user.save()
            return redirect('loginPage')

    return render(request, 'register.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def changePassword(request):
    current_user = request.user
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if current_user.check_password(old_password, current_user.password):
            if new_password == confirm_password:
                current_user.set_password(new_password)
                current_user.save()
                update_session_auth_hash(request, current_user)
                return redirect('loginPage')
    return render(request, 'changePassword.html')

def homePage(request):
    return render(request, 'home.html')