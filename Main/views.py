from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Calendar, Event, UserCalendar
from .forms import CalendarForm, EventForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from .forms import ShareCalendarForm


# Create your views here.

def home(request):
    if request.user.is_authenticated:   
       user_calendars = UserCalendar.objects.filter(user=request.user)
       events = Event.objects.filter(calendar__in=user_calendars.values('calendar'))
       user_created_calendars = Calendar.objects.filter(users=request.user)
       context = {'user_calendars':user_calendars, 'events':events, 'user_created_calendars':user_created_calendars}
       return render(request, 'Main/home.html',context)
    else:
        return render(request,'Main/home.html',{'not_authenticated':True})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password, email=email)
            return redirect ('login')
        else:
            messages.error(request,"Passwords dont match")
    
    return render(request, 'Main/SignUp.html')

def loginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('home')
        else:
            messages.error(request, "Username or password does not exist")
            
    context = {}
    return render(request, 'Main/SignIn.html' , context)

def logoutUser(request):
    logout(request)
    return redirect ('home')

def MyCalendar(request):
    return render(request, 'Main/MyCalendar.html')

def CreateCalender(request):
    if request.method == 'POST':
        form = CalendarForm(request.POST) 
        if form.is_valid():
            calendar = form.save()
            UserCalendar.objects.create(user=request.user , calendar= calendar)
            return redirect ('home')
    
    else:
        form = CalendarForm()
        context = {'form':form}
    return render(request,'Main/CreateCalendar.html', context)


def CreateEvent(request,calendar_id):
    calendar = Calendar.objects.get(id=calendar_id)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.date_and_time = datetime.combine(form.cleaned_data['date'], form.cleaned_data['time'])
            event.calendar = calendar
            event.save()
            return redirect ('calendar_detail', calendar_id=calendar.id)
    else:
        form = EventForm()
        context= {'form':form, 'calendar':calendar}
        return render(request,'Main/CreateEvent.html',context)

def calendar_detail(request,calendar_id):
    calendar = Calendar.objects.get(id=calendar_id)
    events = Event.objects.filter(calendar=calendar)
    context = {'calendar':calendar, 'events':events}

    return render(request,'Main/calender_detail.html',context)

def delete_calendar(request, calendar_id):
    calendar = Calendar.objects.get(id=calendar_id)
    calendar.delete()
    return redirect('home')

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    calendar_id = event.calendar.id
    event.delete()
    return redirect('calendar_detail', calendar_id=calendar_id)

def edit_calendar(request, calendar_id):
    calendar = get_object_or_404(Calendar, id=calendar_id)

    if request.method == 'POST':
        form = CalendarForm(request.POST, instance=calendar)
        if form.is_valid():
            form.save()
            return redirect('calendar_detail',calendar_id = calendar_id)
    else:
        form = CalendarForm(instance=calendar)
    return render(request, 'Main/edit_calendar.html',{'form':form,'calendar':calendar})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('calendar_detail',calendar_id = event.calendar.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'Main/edit_event.html',{'form':form,'event':event})

@login_required
def share_calendar(request, calendar_id):
    # Retrieve the calendar object
    calendar = Calendar.objects.get(id=calendar_id)

    if request.method == 'POST':
        form = ShareCalendarForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            # Check if the user exists
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                # Handle the case where the user does not exist
                form.add_error('user_id', 'User does not exist')
                return render(request, 'Main/share_calendar.html', {'form': form})

            # Check if the current user owns the calendar
            if request.user in calendar.users.all():
                # Create a UserCalendar object to link the user with the calendar
                UserCalendar.objects.create(user=user, calendar=calendar)
                return redirect('calendar_detail', calendar_id=calendar_id)
            else:
                # Handle the case where the current user does not own the calendar
                form.add_error('user_id', 'You do not have permission to share this calendar')
    else:
        form = ShareCalendarForm()

    return render(request, 'Main/share_calendar.html', {'form': form})

