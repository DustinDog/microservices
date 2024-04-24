
from django.contrib import admin
from django.urls import path
from accounts.views import UserList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserList.as_view())
]
