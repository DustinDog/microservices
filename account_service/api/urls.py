from accounts.views import CreateUser, LoginView, UserDetail, UserList
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(),
        name="swagger-ui",
    ),
    path("users/", include("accounts.urls")),
]
