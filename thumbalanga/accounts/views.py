from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect
from requests import post
from .models import *
from .forms import *

# Create your views here.

def home(request):
    members=Member.objects.all()
    loans=Loan.objects.all()
    context={'members':members,'loans':loans}
    return render(request,'accounts/dashboard.html',context)

def create_member(request):
    form=MemberForm()
    if request.method=='POST':
        form=MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'accounts/member_form.html',context)



def update_member(request,pk_member):
    member=Member.objects.get(id=pk_member)
    form=MemberForm(instance=member)
    if request.method=='POST':
        form=MemberForm(request.POST,instance=member)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/member_form.html',context)


def delete_member(request,pk_delete):
    member=Member.objects.get(id=pk_delete)
    if request.method=="POST":
        member.delete()
        return redirect('/')


    context={'member':member}
    return render(request,'accounts/delete.html',context)



def createLoan(request):
    form_Loan=LoanForm()
    if request.method=="POST":
        form_Loan=LoanForm(request.POST)
        if form_Loan.is_valid():
            form_Loan.save()
            return redirect('/')

    context={'form_Loan':form_Loan}
    return render(request,'accounts/loan_form.html',context)




