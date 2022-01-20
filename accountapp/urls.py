from django.urls import path
from accountapp.views import hello_world,AccountCreateView

#이렇게 써놓는게 좋다.

app_name = "accountapp"


urlpatterns = [
    # route, view, name
    path('hello_world/', hello_world,  name='hello_world'), #함수 기반 view는 그냥 함수명을 가져오면 됨
    path('create/', AccountCreateView.as_view(), name='create'), #클래스 기반view는 .as_view()를 가져와야 됨
]
