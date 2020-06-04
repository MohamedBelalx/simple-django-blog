from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Articles

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    return render(request,'articles/test.htm',{'articles':articles})


def with_id(request,pk):
    test = get_object_or_404(Articles,pk=pk)
    return render(request,'articles/test2.htm',{'article':test})