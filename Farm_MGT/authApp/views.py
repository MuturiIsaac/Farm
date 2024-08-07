from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def signup(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['pass1']
        confirmpassword = request.POST['pass2']

        if password1 != confirmpassword:
            messages.warning(request, 'passwords dint match')
            return render(request, 'signup.html')
        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email already exists!")

                return render(request, 'signup.html')
        except Exception as identifier:
            pass

        user = User.objects.create_user(email, password1)
        user.save()
    return render(request, "signup.html")

def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['email']
        userpassword = request.POST['pass1']
        myuser=authenticate(username=username, password=userpassword)
    if myuser is not None:
        login(request, myuser)
        messages.success(request, "Login Successful")
        return render(request, 'index.html')
    else:
        messages.error(request, "invalid Credentials")
        return redirect(request, 'login')
    return render(request, 'login.html')


def handlelogout(request):
    logout(request)
    messages.info(request, "Logout Successful")
    return render(request, 'login.html')