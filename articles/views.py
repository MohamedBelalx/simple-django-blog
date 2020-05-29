from django.shortcuts import render
from .models import Articles
# Create your views here.
def index(request):
    articles = Articles.objects.all()
    return render(request,'articles/test.htm',{'articles':articles})