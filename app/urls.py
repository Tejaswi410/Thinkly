from django.urls import path
from django.views.generic import RedirectView
from .views import (
    ThoughtCreateView,
    ThoughtDeleteView,
    ThoughtListView,
    ThoughtUpdateView,
    add_comment,
    CustomLoginView,
    CustomLogoutView,
    index,
    like_thought,
    register,
)

from django.urls import path
from app.views import create_admin

urlpatterns = [
    path("", RedirectView.as_view(url="/feed/"), name="home"),
    path("feed/", ThoughtListView.as_view(), name="thought-list"),
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("thought/new/", ThoughtCreateView.as_view(), name="thought-create"),
    path("thought/<int:pk>/edit/", ThoughtUpdateView.as_view(), name="thought-update"),
    path(
        "thought/<int:pk>/delete/",
        ThoughtDeleteView.as_view(),
        name="thought-delete",
    ),
    path("create-admin/", create_admin),
    path("thought/<int:pk>/like/", like_thought, name="thought-like"),
    path("thought/<int:pk>/comment/", add_comment, name="thought-comment"),
]


