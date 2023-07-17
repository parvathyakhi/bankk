from django.http import HttpResponse
from django.shortcuts import render
def home(request):
#    return HttpResponse('kkkkk')
     return render(request,'index.html')
# Create your views here.
