from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from app import views as app_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    # Auth views
    path("accounts/login/", app_views.CustomLoginView.as_view(), name="login"),
    path("accounts/logout/", app_views.CustomLogoutView.as_view(), name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

