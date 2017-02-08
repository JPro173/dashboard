from django.shortcuts import render
from django.views.generic.list import ListView

from notes.models import Note


class NotesListView(ListView):
    model = Note
