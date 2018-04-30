from django.forms import ModelForm
from django.contrib.auth.models import User

from blogUser.models import BlogUser

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
