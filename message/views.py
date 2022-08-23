from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from . forms import UserForm, LoginUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .utils import generate_pass, generate_username
# Create your views here.


# make a view that will return a form 
# so the form with take a post request and generate

def index(request):
    if request.user.is_authenticated:
        return redirect("view-messages")
    user_form = UserForm()
    login_form = LoginUserForm()
    context = {"create_form": user_form, "login_form": login_form}
    return render(request, "index.html", context)


def create_user(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['name']
            username = generate_username()
            password = generate_pass()
            user = User.objects.create(first_name = first_name, username=username, password=password)
            login(request, user)
            return redirect("view-messages")


def view_messages(request):
    return render(request, "messages.html")

def logout_view(request):
    # request.user.delete()
    logout(request)
    return redirect("index")