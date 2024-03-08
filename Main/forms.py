from django import forms
from .models import Calendar, Event
from django.contrib.auth.models import User

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['name','description']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','date','time']

    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
    
class ShareCalendarForm(forms.Form):   
    user_id = forms.IntegerField(label='User ID', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_user_id(self):
        user_id = self.cleaned_data['user_id']
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise forms.ValidationError('User does not exist')
        return user_id
        

    