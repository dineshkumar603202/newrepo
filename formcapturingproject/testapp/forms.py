from django import forms
from django.core import validators
#validation for name
#def namestartwith_d(value):
#   if value[0]!='d':
#       raise forms.ValidationError("name should start with d")
#def nameendswith_h(value):
#   if value[-1]!='h':
#       raise forms.ValidationError("name should ends with h")

 




class Studentform(forms.Form):
    name=forms.CharField(label='dinesh name')
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    #by clean_method validation
    #def clean_name(self):
    #    inputname=self.cleaned_data['name']
    #    if len(inputname)>=4:
    #        return inputname
    #    else:
    #       raise forms.ValidationError('ivalid name')'''

    #full validation by clean method
    def clean(self):
        print('total validation')
        cleaned_data=super().clean()
        inputname=cleaned_data['name']
        if len(inputname)<=4:
            raise forms.ValidationError('name should be greater than 4')

