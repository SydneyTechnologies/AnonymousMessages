from django.urls import path
from . views import index, create_user, logout_view, view_messages, create_message, login_user


urlpatterns=[
    path("", index, name = "index"),
    path("create-user", create_user, name='create-user'),
    path("view-messages/<str:unsafe_pass>", view_messages, name="view-messages"),
    path("create-message/<str:username>", create_message, name="create-message"),
    path("login", login_user, name="login"),
    path("logout", logout_view, name="logout")

]