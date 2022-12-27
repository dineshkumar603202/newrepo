from django.shortcuts import render

# Create your views here.
def Cookie_view(request):
    count=int(request.COOKIES.get('count',0))
    count=count+1
    response=render(request,'home.html',{'count':count})
    response.set_cookie('count',count)
    return response
