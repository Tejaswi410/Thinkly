from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.db.models import Count, F
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import CommentForm, StyledAuthenticationForm, ThoughtForm
from .models import Thought



class ThoughtListView(ListView):
    model = Thought
    template_name = "modern_thought_feed.html"
    context_object_name = "thoughts"

    def get_queryset(self):
        queryset = Thought.objects.annotate(
            comment_count=Count('comments')
        )
        if self.request.user.is_authenticated:
            # Annotate whether current user has liked each thought
            queryset = queryset.prefetch_related('liked_by')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ThoughtForm()
        context["comment_form"] = CommentForm()
        # Add liked thoughts set for current user
        if self.request.user.is_authenticated:
            context["liked_thought_ids"] = set(
                Thought.objects.filter(liked_by=self.request.user).values_list('pk', flat=True)
            )
        else:
            context["liked_thought_ids"] = set()
        return context

    def post(self, request: HttpRequest, *args, **kwargs):
        """Handle quick-create from the feed when authenticated."""
        if not request.user.is_authenticated:
            messages.info(request, "Please login to share a thought.")
            return redirect("login")

        form = ThoughtForm(request.POST, request.FILES)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.author = request.user
            thought.save()
            messages.success(request, "Thought shared!")
        else:
            messages.error(request, "Please fix the errors and try again.")
        return redirect("thought-list")


class ThoughtCreateView(LoginRequiredMixin, CreateView):
    model = Thought
    form_class = ThoughtForm
    template_name = "thought_form.html"
    success_url = reverse_lazy("thought-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Thought shared!")
        return super().form_valid(form)


class ThoughtUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Thought
    form_class = ThoughtForm
    template_name = "thought_form.html"
    success_url = reverse_lazy("thought-list")

    def test_func(self):
        thought = self.get_object()
        return thought.author == self.request.user # type: ignore

    def form_valid(self, form):
        messages.success(self.request, "Thought updated.")
        return super().form_valid(form)


class ThoughtDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Thought
    template_name = "thought_confirm_delete.html"
    success_url = reverse_lazy("thought-list")

    def test_func(self):
        thought = self.get_object()
        return thought.author == self.request.user # type: ignore

    def delete(self, request: HttpRequest, *args, **kwargs):
        messages.info(request, "Thought removed.")
        return super().delete(request, *args, **kwargs)


@login_required
def like_thought(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method != "POST":
        messages.info(request, "Please use the like button.")
        return redirect("thought-list")
    thought = get_object_or_404(Thought, pk=pk)
    
    # Check if user has already liked this thought
    if thought.liked_by.filter(pk=request.user.pk).exists():
        messages.info(request, "You've already liked this thought!")
        return redirect("thought-list")
    
    # Add like and track the user
    thought.liked_by.add(request.user)
    Thought.objects.filter(pk=pk).update(likes=F('likes') + 1)
    messages.success(request, "Thanks for the like!")
    return redirect("thought-list")


@login_required
def add_comment(request: HttpRequest, pk: int) -> HttpResponse:
    thought = get_object_or_404(Thought, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thought = thought
            comment.save()
            messages.success(request, "Comment added.")
        else:
            messages.error(request, "Please correct the errors below.")
    return redirect("thought-list")


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponseRedirect(reverse("thought-list"))


def register(request: HttpRequest) -> HttpResponse:
    def _style(form: UserCreationForm) -> UserCreationForm:
        for field in form.fields.values():
            field.widget.attrs.update(
                {
                    "class": "form-control",
                    "placeholder": field.label,
                }
            )
        return form

    if request.method == "POST":
        form = _style(UserCreationForm(request.POST))
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can login now.")
            return redirect("login")
    else:
        form = _style(UserCreationForm())
    return render(request, "registration/register.html", {"form": form})


class CustomLoginView(LoginView):
    authentication_form = StyledAuthenticationForm
    template_name = "registration/login.html"


class CustomLogoutView(LogoutView):
    next_page = "/feed/"


