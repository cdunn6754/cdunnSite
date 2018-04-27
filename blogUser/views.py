from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.shortcuts     import redirect

from blogUser.models import BlogUser
from blogUser.forms  import UserForm

# Create your views here.
class TestBlogView(TemplateView):
    template_name = 'blogUser/test_blog.html'

def createUser(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            # hash password
            user.set_password(user.password)
            user.save()

            blogUser = BlogUser(user=user)
            blogUser.save()
            return redirect("blogUser:index")
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
    return render(
        request,
        "blogUser/bloguser_create_form.html",
        {
            'user_form' : user_form
        }
        )
