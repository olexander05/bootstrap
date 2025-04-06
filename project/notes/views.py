from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note

def home(request):
    return render(request, 'notes/home.html')

def create_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        note = Note(title=title, content=content)
        note.save()
        return redirect('home')
    return render(request, 'notes/create_note.html')
