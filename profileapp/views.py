from platform import release
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from django.utils.decorators import method_decorator

from profileapp.models import Profile
from profileapp.forms import ProfileCreationForm
from django.urls import reverse, reverse_lazy
# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'
    
    #model Form 에서 user 객체를 넣지 않고 여기서 구현
    #form_valid는 내장 함수
    def form_valid(self, form):
        temp_profile = form.save(commit=False) #commit=False는 실제 DB에 저장하지 않고 일단 임시로 저장
        temp_profile.user = self.request.user  #user라는 데이터는 request를 보낸 사람만으로 저장되게끔
        temp_profile.save()
        return super().form_valid(form)

    #profileapp:detail로 가려면 pk를 넘겨줘야하는데 success_url로는 추가적인 파라미터를 넘겨줄 수 없기 때문에
    #get_success_url이란 함수를 조금 바꿔줘야 한다. 
    def get_success_url(self):
        return reverse_lazy('accountapp:detail', kwargs={'pk':self.object.user.pk})  #self.object -> profileapp.models.Profile를 가르킴.


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'
    def get_success_url(self):
        return reverse_lazy('accountapp:detail', kwargs={'pk':self.object.user.pk})  #self.object -> profileapp.models.Profile를 가르킴.
    