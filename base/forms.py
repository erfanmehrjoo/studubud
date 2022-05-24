from django.forms import ModelForm
from .models import Room
### make your form
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'