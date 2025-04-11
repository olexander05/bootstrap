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

# ASYNC VIEWS CODE:

# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
# from asgiref.sync import sync_to_async
# from .forms import NoteForm
# from .models import Note
#
# async def home(request):
#     return render(request, 'notes/home.html')
#
#
# @sync_to_async
# def create_note_obj(title, content, user):
#     note = Note(title=title, content=content, user=user)
#     note.save()
#
#
# @login_required
# async def create_note(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         content = request.POST['content']
#         await create_note_obj(title, content, request.user)
#         return redirect('home')
#     return render(request, 'notes/create_note.html')
#
#
# async def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'notes/login.html', {'form': form})
#
#
# @sync_to_async
# def get_user_notes(user):
#     return list(Note.objects.filter(user=user))
#
#
# @login_required
# async def note_list(request):
#     notes = await get_user_notes(request.user)
#     return render(request, 'notes/note_list.html', {'notes': notes})
#
#
# @sync_to_async
# def get_note_by_user(pk, user):
#     return get_object_or_404(Note, pk=pk, user=user)
#
#
# @sync_to_async
# def save_note_form(form):
#     form.save()
#
#
# @sync_to_async
# def delete_note_obj(note):
#     note.delete()
#
#
# @login_required
# async def edit_note(request, pk):
#     note = await get_note_by_user(pk, request.user)
#     if request.method == 'POST':
#         form = NoteForm(request.POST, instance=note)
#         if form.is_valid():
#             await save_note_form(form)
#             return redirect('home')
#     else:
#         form = NoteForm(instance=note)
#     return render(request, 'notes/edit_note.html', {'form': form})
#
#
# @login_required
# async def delete_note(request, pk):
#     note = await get_note_by_user(pk, request.user)
#     if request.method == 'POST':
#         await delete_note_obj(note)
#         return redirect('home')
#     return render(request, 'notes/delete_note.html', {'note': note})

