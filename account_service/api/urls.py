from accounts.views import CreateUser, LoginView, UserDetail, UserList
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("accounts.urls")),
]
