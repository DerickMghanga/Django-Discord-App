from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'  #creates form fields based on attributes in 'Room' model
        exclude = ['host', 'participants']  # exclude a field in the form