from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #자신의 Info를 업데이트할 때 ID는 바꾸지 못하게 따로 하나의 forms을 생성
        self.fields['username'].disabled = True