from django.shortcuts import render
from .models import Thought
from .forms import ThoughtForm, UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request, 'index.html')

#for displaying the thought list
def thought_list(request):
    thoughts = Thought.objects.all().order_by('-created_at')
    return render(request, 'thought_list.html',{'thoughts' :thoughts})


#for creating a thought
@login_required
def thought_create(request):
    if request.method == "POST":
       form = ThoughtForm(request.POST, request.FILES)
       if form.is_valid():
           thought = form.save(commit = False)
           thought.user = request.user 
           thought.save()
           return redirect('thought_list')
    else :
        form = ThoughtForm()
    return render(request, 'thought_form.html', {'form': form})

#for editing thoughts post the user
@login_required
def thought_edit(request, thought_id):
    thought = get_object_or_404(Thought, pk = thought_id, user = request.user)
    if request.method == 'POST':
        form = ThoughtForm(request.POST, request.FILES,instance = thought)
        if form.is_valid():
            thought = form.save(commit = False)
            thought.user = request.user
            thought.save()
            return redirect('thought_list')
    else:
        form = ThoughtForm(instance = thought)
    return render(request , 'thought_form.html', {'form' : form})

#for deleting the thoughts
@login_required
def thought_delete(request,thought_id):
    thought = get_object_or_404(Thought, pk = thought_id, user = request.user)
    if request.method == 'POST':
        thought.delete()
        return redirect('thought_list')
    return render(request, 'thought_confirm_delete.html', {'thought' : thought
    })


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('thought_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html',{'form': form})
