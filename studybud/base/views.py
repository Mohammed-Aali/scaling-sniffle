from django.shortcuts import render

# Create your views here.

rooms = [
    {"id":1, 'name':'lets learn python!'},
    {"id":2, 'name':'Design with me'},
    {"id":3, 'name':'Front end developers'},
]
arab = 'Saudi Arabia'

def home(request):
    context = { 'rooms': rooms } 
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')
