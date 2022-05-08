from django.forms import ModelForm
from .models import Contact,Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields =('title','slug','content','status')

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']



    