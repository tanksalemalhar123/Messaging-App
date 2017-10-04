from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def index(request):
    return render (request,'app/index.html')

@login_required(login_url='/login_form')
def chat(request, app_user2):
    app_user1 = request.user.appuser.id
    contacts = request.user.appuser.contact_list.all()
    u1 = request.user.appuser
    u2 = AppUser.objects.get(id=app_user2)
    if request.method == 'POST':
        text = request.POST.get('chat')
        msg = Message.objects.create(sender=u1, receiver=u2, text=text)
        return redirect('/chat/' + app_user2 + '/')
    else:
        msgs=Message.objects.filter(
                    Q(sender__id=u1.id, receiver__id=u2.id) |
                    Q(sender__id=u2.id, receiver__id=u1.id)).order_by('timestamp')
        return render (request,'app/chat.html',{'msgs':msgs, 'app_user2': u2, 'contacts': contacts})

@login_required(login_url='/login_form')
def app_users(request):
    app_users=AppUser.objects.all()
    return render(request,'app/app_users.html',{'app_users':app_users})


def login_form(request):
    return render(request, 'app/login_form.html')

def login_action(request):
    #authenticate the user
    username= request.POST.get('username')
    password= request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return redirect('/login_form/')


def logout_action(request):
    #logout here
    logout(request)
    return redirect('/')

def register(request):
    #Reg heisterre
    return render(request,'app/register.html')

def register_action(request):
    #Reg app_user
    username=request.POST.get('username')
    password=request.POST.get('password')
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email=request.POST.get('email')
    phone_no=request.POST.get('contact')

    user=User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    app_user = AppUser.objects.create(
        user=user,
        contact=phone_no

    )
    return redirect('/')


@login_required(login_url='/login_form/')
def add_to_contacts(request, app_user_id):
    app_user = AppUser.objects.get(id=app_user_id)
    contacts = request.user.appuser.contact_list.add(app_user)
    return redirect('/my_contacts/')


@login_required(login_url='/login_form/')
def remove_contact(request, app_user_id):
    app_user = AppUser.objects.get(id=app_user_id)
    contacts = request.user.appuser.contact_list.remove(app_user)
    return redirect('/my_contacts/')

@login_required(login_url='/login_form/')
def my_contacts(request):
    contacts = request.user.appuser.contact_list.all()
    return render(request, 'app/contacts.html', {'contacts': contacts})


@login_required(login_url='/login_form/')
def profile(request):

    return render(request, 'app/profile.html')

@login_required(login_url='/login_form/')
def edit_profile(request):
    return render(request, 'app/edit_profile.html')
