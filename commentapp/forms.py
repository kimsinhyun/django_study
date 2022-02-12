from django.forms import ModelForm
from commentapp.models import Comment

class ComentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']