from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Room , Topic
from .forms import RoomForm
# Create your views here.

def home(request , *args , **kwargs):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(topic__name__contains=q)
    topics = Topic.objects.all()
    return render(request , 'home.html' , context = {'rooms':rooms , 'topics':topics})


def room(request ,pk):
    room = Room.objects.get(id=int(pk))
    return render(request , 'room.html' , context={'room':room})

def createRoom(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request , 'room_form.html' , context={'form':form})


def updateroom(request , pk):
    room = Room.objects.get(id=int(pk))
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST , instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request , 'room_form.html' , context={'form':form})

def deleteroom(request ,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request , 'delete.html' , context={})