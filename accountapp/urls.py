from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import AccountUpdateView, hello_world,AccountCreateView,AccountDetialView

#이렇게 써놓는게 좋다.

app_name = "accountapp"


urlpatterns = [
    # route, view, name
    path('hello_world/', hello_world,  name='hello_world'), #함수 기반 view는 그냥 함수명을 가져오면 됨

    #login logout은 내장 클래스를 사용하기 때문에 이렇게 해주면 된다.
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accountapp/login.html'), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'), #클래스 기반view는 .as_view()를 가져와야 됨
    
    #몇 번 유저객체에 접근할 것인지
    path('detail/<int:pk>', AccountDetialView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    
]
