from django.urls import path
from . import views
from .views import share_calendar

urlpatterns = [
    path('', views.home , name='home' ),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('mycalendar/', views.MyCalendar, name='MyCalendar'),
    path('createcalender/',views.CreateCalender, name='CreateCalendar'),
    path('create_event/<int:calendar_id>/',views.CreateEvent, name='CreateEvent'),
    path('calendar_detail/<int:calendar_id>/', views.calendar_detail, name='calendar_detail'),
    path('delete_calendar/<int:calendar_id>/', views.delete_calendar, name='delete_calendar'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('edit_calendar/<int:calendar_id>/',views.edit_calendar, name='edit_calendar'),
    path('edit_event/<int:event_id>/',views.edit_event, name='edit_event'),
    path('share-calendar/<int:calendar_id>/', share_calendar, name='share_calendar')
]