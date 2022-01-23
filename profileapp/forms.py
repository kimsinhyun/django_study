from django.forms import ModelForm
from profileapp.models import Profile

#Model Form을 하면 이미 만들어둔 모델의 모양대로 form을 편리하고 빠르게 만들 수 있다.
class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        #user까지 넣어버리면 다른사람의 프로필도 만들어버릴 수 있는 가능성이 있기 때문에 안넣음
        #따로 서버 내에서 구현
        fields = ['image','nickname','message']