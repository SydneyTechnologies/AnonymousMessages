from django.urls import path
from . views import index, create_user, logout_view, view_messages


urlpatterns=[
    path("", index, name = "index"),
    path("create-user", create_user, name='create-user'),
    path("view-messages", view_messages, name="view-messages"),
    path("logout", logout_view, name="logout")

]