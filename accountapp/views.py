from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from accountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accountapp.forms import AccountUpdateForm

#FBV  (함수기반 view)
def hello_world(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            hello_world_list =  HelloWorld.objects.all()
            #reserse는 특정 url로 리다이렉트해주는 함수
            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        elif request.method == "GET":
            hello_world_list =  HelloWorld.objects.all()

            return render(request, 'accountapp/hello_world.html', context={ 'hello_world_list' : hello_world_list })
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

#CBV 클래스 기반 View
class AccountCreateView(CreateView):
    model = User
    #form_class -> CreateView에서 오버라이딩 ; UserCreationForm은 import해서 사용할 수 있는 간단한 내장 form
    form_class = UserCreationForm

    #성공했을 때 reverse_lazy를 사용해서 보여줄 화면에 연결시켜줌
    #reverse와 reverse_lazy차이 -> reverse_lazy는 곧바로 처리되는게 아니라 나중에 해당 변수가 직접 접근되었을 때 실행 됨
    #따라서 success할 때 동작시킬 것이기 때문에 lazy로 정의 
    #reverse_lazy   ->  클래스형 view에서 사용
    #reverse        ->  함수형 view에서 사용
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'   #회원가입할 때 보일 HTML

class AccountDetialView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'
    # #UpdateView 안에 있는 view라는 함수 아래 주석이 원래 기존 방식 코드
    # def get(self, *args, **kwargs):
    #     return super().get(*args, **kwargs)
    def get(self, *args, **kwargs):
        # 로그인이 되어 있고 현재 request를 보내고 있는 유저와 같을 시, 만약 두 번째 조건이 없으면 1번 유저가 2번 유저를 삭제할 수 있음!!
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()
        

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()
        
