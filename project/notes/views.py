from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NoteForm
from .models import Note

def home(request):
    return render(request, 'notes/home.html')



@login_required
def create_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        note = Note(title=title, content=content, user=request.user)
        note.save()
        return redirect('home')
    return render(request, 'notes/create_note.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'notes/login.html', {'form': form})

# def note_list(request):
#
#     if request.user.is_authenticated:
#         notes = Note.objects.filter(user=request.user)
#     else:
#         notes = Note.objects.all()
#     return render(request, 'notes/note_list.html', {'notes': notes})

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})

@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form})

@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    return render(request, 'notes/delete_note.html', {'note': note})

