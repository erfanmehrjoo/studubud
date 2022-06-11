from django.forms import ModelForm
from .models import Room , Message
### make your form
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host' , 'paticipants']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'