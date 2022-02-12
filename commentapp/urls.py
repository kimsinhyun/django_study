from importlib.resources import path
from commentapp.views import CommentCreateView, CommentDeleteView
from django.urls import path

app_name = 'commentapp'

urlpatterns = [
    path('create/',CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>',CommentDeleteView.as_view(), name='delete')
]