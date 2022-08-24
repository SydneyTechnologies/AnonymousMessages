from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView
from . forms import UserForm, LoginUserForm, MessageForm
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
            user = User.objects.create_user(first_name = first_name, username=username, password=password)
            login(request, user)
            return redirect("view-messages", password)

def login_user(request):
    if request.method == "POST":
        login_form = LoginUserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user=user)
                return redirect("view-messages", password)
            else:
                return HttpResponse("not working")


def view_messages(request, unsafe_pass):
    inbox_location = request.build_absolute_uri(reverse("create-message",  args=[request.user.username]))
    context = {"inbox": inbox_location, "unsafe": unsafe_pass}
    return render(request, "messages.html", context)


def create_message(request, username):
    target_user = User.objects.get(username = username)
    message_form = MessageForm()
    context = {"target": target_user, "form": message_form}

    if target_user is not None:
        return render(request, "send-message.html", context)
    else:
        return HttpResponse("Target User not found")


def logout_view(request):
    # request.user.delete()
    logout(request)
    return redirect("index")