from platform import release
from django.shortcuts import render
from django.views.generic import CreateView 
from profileapp.models import Profile
from profileapp.forms import ProfileCreationForm
from django.urls import reverse, reverse_lazy
# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'
    
    #model Form 에서 user 객체를 넣지 않고 여기서 구현
    #form_valid는 내장 함수
    def form_valid(self, form):
        temp_profile = form.save(commit=False) #commit=False는 실제 DB에 저장하지 않고 일단 임시로 저장
        temp_profile.user = self.request.user  #user라는 데이터는 request를 보낸 사람만으로 저장되게끔
        temp_profile.save()
        return super().form_valid(form)