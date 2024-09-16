from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()  # This created an Array of post class data type
    return render(request,'index.html',{'posts' : posts})

def post(request,pk):
    posts = Post.objects.get(id = pk)
    return render(request,'posts.html',{'posts' : posts})