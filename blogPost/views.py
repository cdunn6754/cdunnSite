from django.shortcuts import render

# Create your views here.
def blogIndex(request):
    return render(request, "blogPost/blog_index.html")
