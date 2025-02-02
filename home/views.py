from django.shortcuts import render, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .models import Rating

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

@csrf_protect
@login_required(login_url='/login', redirect_field_name=None)

def rate_experience(request):
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        feedback = request.POST.get('feedback')

        # Save the rating to the database
        Rating.objects.create(
            user=request.user,
            rating=rating_value,
            feedback=feedback
        )

        messages.success(request, 'Thank you for your feedback!')
        return redirect('home')

    return render(request, 'rating.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("register")

        user = User(username=username, email=email)
        user.set_password(password)  # This hashes the password
        user.save()

        messages.success(request, "Account created successfully! You can now log in.")
        return redirect("login")

    return render(request, 'register.html')


def index(request):
    print("Current user:", request.user)  # Debugging line
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")
def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print(user)
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect("home")

