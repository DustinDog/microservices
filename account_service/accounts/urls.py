from accounts.views import (
    CreateUser,
    LoginView,
    UserDetail,
    UserList,
    UserDelete,
    UserUpdate,
)
from django.urls import path

urlpatterns = [
    path("", UserList.as_view()),
    path("create/", CreateUser.as_view()),
    path("login/", LoginView.as_view()),
    path("delete/", UserDelete.as_view()),
    path("update/", UserUpdate.as_view()),
    path("<int:pk>/", UserDetail.as_view()),
]
