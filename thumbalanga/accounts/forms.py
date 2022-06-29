
from cProfile import label
from django import forms
from django.forms import ModelForm
from .models import *


class MemberForm(ModelForm):
    class Meta:
        model=Member
        fields= ('name','gender','phone','date_joined','next_of_kin','next_of_kin_Phone')
        labels={
            'name':'',
            'gender':'',
            'phone':'',
            'date_joined':'',
            'next_of_kin':'',
            'next_of_kin_Phone':'',






        }
        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':'Gender'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'date_joined':forms.TextInput(attrs={'class':'form-control','placeholder':'Date Joined'}),
            'next_of_kin':forms.TextInput(attrs={'class':'form-control','placeholder':'Next of Kin'}),
            'next_of_kin_Phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Next of Kin Phone'}),
                }




class LoanForm(ModelForm):
    class Meta:
        model=Loan
        fields=('member','date_applied','amount','status')
        labels={
            'member':'',
            'date_applied':'',
            'amount':'',
            'status':'',

        }

        widgets={
            'member':forms.Select(attrs={'class':'form-control','placeholder':'Select Member'}),
            'date_applied':forms.DateInput(attrs={'class':'form-control','placeholder':'Date '}),
            'amount':forms.TextInput(attrs={'class':'form-control','placeholder':'Amount Required'}),
            'status':forms.Select(attrs={'class':'form-control','placeholder':'Status'}),

        }

