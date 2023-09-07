from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model() # 유지보수를 위해서 좋은 방법
        # model = User
        fields = ('username', 'profile_image', )


class CustomAuthenticationForm(AuthenticationForm):
    pass