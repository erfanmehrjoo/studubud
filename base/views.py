from django.shortcuts import render , redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Room , Topic , Message
from .forms import RoomForm , MessageForm
# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def RegisterPage(request):
    page = 'Register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request , user)
            return redirect('home')
        else:
            messages.error(request , 'ridi')
    return render(request , 'login_register.html' , context={'form':form})

def home(request , *args , **kwargs):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__contains=q))
    room_count = rooms.count()
    topics = Topic.objects.all()
    messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    return render(request , 'home.html' , context = {'rooms':rooms , 'topics':topics , 'room_count':room_count , 'messages':messages})


def room(request ,pk):
    room = Room.objects.get(id=int(pk))
    messages = room.message_set.all().order_by("-created")
    paticipants = room.paticipants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user , 
            room = room ,
            body = request.POST.get('body')
        )
        room.paticipants.add(request.user)
        return redirect('room' , pk=room.id)
    return render(request , 'room.html' , context={'room':room , 'messages':messages , 'paticipants':paticipants})
@login_required(login_url='login')
def UserProfile(request , pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    messages = user.message_set.all()
    topics = Topic.objects.all()
    return render(request , 'profile.html' , context={'user':user , 'rooms':rooms , 'messages':messages , 'topics':topics})
@login_required(login_url='login')
def createRoom(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request , 'room_form.html' , context={'form':form})

@login_required(login_url='login')
def updateroom(request , pk):
    room = Room.objects.get(id=int(pk))
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse("<h1>zayeidie<h1>")
    if request.method == 'POST':
        form = RoomForm(request.POST , instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request , 'room_form.html' , context={'form':form})

@login_required(login_url='login')
def deleteroom(request ,pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("<h1>zayeidie<h1>")
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request , 'delete.html' , context={})

@login_required(login_url='login')
def deletemessage(request ,pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse("<h1>zayeidie<h1>")
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request , 'delete.html' , context={'obg':message})

@login_required(login_url='login')
def updatemessage(request , pk):
    message = Message.objects.get(id=pk)
    form = MessageForm(instance=message)
    if request.user != message.user:
        return HttpResponse("<h1>Zayeidie<h1/>")
    if request.method == 'POST':
        form = MessageForm(request.POST , instance=message)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request , 'room_form.html' , context={'form':form})
