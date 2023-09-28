from django.contrib import messages, auth
from django.contrib.auth.models import User
# from django.core.checks import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person, Course
from .forms import PersonForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin


# def register(request):
#     if request.method == 'GET':
#         form = UserCreationForm()
#         return render(request, 'register.html', {'form': form})
#     if request.method == 'POST':
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return('login')
#     else:
#         form=UserCreationForm()
#     return render(request,'register.html',{'form':form})
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('explore')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            # login(request, user)
            return redirect('login')
            # post
        else:
            return render(request, 'register.html', {'form': form})


# def sign_in(request):
#     if request.method == 'GET':
#         form = LoginForm()
#         return render(request, 'login.html', {'form': form})
#
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             # user.username = user.username.lower()
#             user.save()
#             messages.success(request, 'You have singed up successfully.')
#             # login(request, user)
#             return redirect('explore')
#             #post
#         else:
#             return render(request, 'login.html', {'form': form})
#

# Create your views here.
# login code
# def login(request):
#     form = RegisterForm(request.POST)
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('explore')
#         else:
#             messages.info(request, "Invalid Response ! Please enter correct username and password")
#             return redirect('login')
#
#     return render(request, "login.html")


def s(request):
    return render(request, "s.html")


# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         cpass = request.POST['password1']
#         if password == cpass:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, "username taken")
#                 return redirect('register')
#
#             else:
#                 user = User.objects.create_user(username=username, password=password)
#                 user.save();
#                 return redirect('login')
#             # print("USER CREATED")
#
#         else:
#             messages.info(request, "password not matching")
#             return redirect('register')
#         return redirect('/')
#     return render(request, "registration.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def explore(request):
    return render(request, "explore.html")


def show(request):
    return render(request, "home.html")


def ack(request):
    return render(request, "ack.html")


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'person_list.html'


class PersonCreateView(SuccessMessageMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'person_form.html'
    success_url = reverse_lazy('person_add')
    success_message = "Successfully Completed"


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'person_form.html'
    success_url = reverse_lazy('person_changelist')


def load_courses(request):
    department_id = request.GET.get('department')
    courses = Course.objects.filter(department_id=department_id).order_by('name')
    return render(request, 'hr/city_dropdown_list_options.html', {'courses': courses})
