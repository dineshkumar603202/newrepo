from django.shortcuts import render
from . import forms
# Create your views here.
def Form_view(request):
    form=forms.Studentform()
    if request.method== 'POST':
        form=forms.Studentform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['rollno'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['feedback'])
            print(form.cleaned_data)
            return render(request,'testapp/thankyou.html')
    return render(request,'testapp/form.html',{'form':form})
