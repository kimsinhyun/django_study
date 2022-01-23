from django.forms import ModelForm
from profileapp.models import Profile

#Model Form을 하면 이미 만들어둔 모델의 모양대로 form을 편리하고 빠르게 만들 수 있다.
class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image','nickname','message']