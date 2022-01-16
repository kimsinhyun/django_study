from django.urls import path
from accountapp.views import hello_world

#이렇게 써놓는게 좋다.
app_name = "account"


urlpatterns = [
    # route, view, name
    path('hello_world/', hello_world,  name='hello_world'),
]
