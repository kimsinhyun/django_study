from django.forms import ModelChoiceField, ModelForm
from articleapp.models import Article
from django import forms
from projectapp.models import Project
class ArticleCreationForm(ModelForm):
    #이렇게 해줌으로써 html 필드에 원하는 클래스 정보를 넣어줌 (클래스 정보는 미디엄 에디터를 사용하기 위함)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                            'style': 'height: auto; text-align: left'}))
    # 외래키를 고르는 부분인데 그런 것을 사용하는 필드가 ModelChoiceField이다
    # 여기서 굳이 프로젝트, 즉 외래키를 안골라도 되게끔 해줌
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    class Meta:
        model = Article
        fields = ['title','image','project','content']