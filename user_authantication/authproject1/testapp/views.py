from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import signupform
from django.http import HttpResponseRedirect
# Create your views here.
def Home_view(request):
    return render(request,'testapp/home.html')
@login_required
def Exam_view(request):
    return render(request,'testapp/Exam.html')

def Signup_view(request):
    form=signupform()
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')

    return render(request,'testapp/signup.html',{'form':form})