from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from .forms import Todo_forms,RegistrationForm,LoginForm
from django.contrib.auth import views as auth_view
from .forms import LoginForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.



def create(request):
    if request.method == 'POST':
        form = Todo_forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            print(form.errors)
    else:
        form = Todo_forms()
    return render(request,'create.html',{'form':form})

def list(request):
    todos = Todo.objects.all()
    print(todos)
    return render(request, 'list.html', {'todos': todos})


def details(request,pk):
    fom = get_object_or_404(Todo,pk=pk)
    return render(request,'details.html',{'fom':fom})


def update(request,pk):
    todo = get_object_or_404(Todo,pk=pk)
    if request.method == 'POST':
        form = Todo_forms(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            print(form.errors)
    else:
        form = Todo_forms(instance=todo)
    return render(request,'list.html',{'form':form})


def delete(request,pk):
    todo = get_object_or_404(Todo,pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('list')
    return render(request,'list.html',{'todo':todo})



class Registration(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request,'Registration.html',locals())
    
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"congratulation User Registration Succesfull")
        else:
            messages.warning(request,'Invalid Input Data')
        return render(request, 'Registration.html', locals())
    

def loggout(request):
    logout(request)
    return redirect('login')
