from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})
  
def smallInteraction1(request):
    return render(request, 'draw/smallInteraction1.html', {})

def smallInteraction2(request):
    return render(request, 'draw/smallInteraction2.html', {})

def largeDisplay(request):
    return render(request, 'draw/largeDisplay.html', {})

def teacherDisplay(request):
    return render(request, 'draw/teacherDisplay.html', {})
  
def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })