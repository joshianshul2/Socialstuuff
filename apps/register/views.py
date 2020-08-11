from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from django.urls import reverse_lazy
from .models import User, UserManager, Profile1, Profile2, ExampleModel
# from .forms import  ImageUploadForm
from django.http import Http404, HttpResponse, HttpResponseForbidden

# Anji
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import CustomerForm


# from .filters import OrderFilter
# from .decorators import unauthenticated_user, allowed_users, admin_only


def index(request):
    return render(request, 'register/index2.html')


def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    # hashed_password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
    # password= User.objects.create()
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                               password=request.POST['password'], email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')


def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        # if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), user.password.encode('utf-8'))):
        if (request.POST['login_password'] == user.password):
            request.session['id'] = user.id
            return redirect('/success')

        else:
            messages.error(request, 'username or password not correct')
            return redirect('/')
    return redirect('/')


def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }

    place = Profile1.objects.get(id=1)
    print(place.id)

    return render(request, 'login.html', {'info': place})

    # return render(request, 'login.html', context)


def set_password(self, pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    self.password_hash = pwhash.decode('utf8')  # decode the hash to prevent is encoded twice


# profile
def profile(request):
    place = Profile1.objects.get(id='1')
    print(place)
    print(place.id)

    return render(request, "profile.html", {'info': place})


# Fb
def fb(request):
    return render(request, "fb.html")


# twitter
def twitter(request):
    return render(request, "twitter.html")


# linkdien
def linkdien(request):
    return render(request, "linkdien.html")


# insta
def insta(request):
    return render(request, "insta.html")


# About us
def aboutus(request):
    return render(request, "about us.html")


# Save Profile Username and Biography
def saveprofile1(request):
    if request.method == 'POST':
        user1 = request.POST['Username']
        print(user1)
        biography1 = request.POST['Biography']
        # name1=request.POST['first_name']
        # name2=request.POST['last_name']
        # email1 = request.POST['email']
        # add1= request.POST['address']
        # add2 = request.POST['address2']
        # city = request.POST['city']
        # # state = request.POST['state']
        # zip = request.POST['zip']
        # anji=Profile(Username=user1,Biography=biography1,first_name=name1,last_name=name2,email=email1,address=add1,address2=add2,city=city,state=state,zip=zip)
        anji = Profile1(Username=user1, Biography=biography1)
        anji.save()
        return redirect(success)

    return render(request, 'profile.html')


# Save Profile remaining All
def saveprofile2(request):
    if request.method == 'POST':
        # user1=request.POST['Username']
        # biography1=request.POST['Biography']
        name1 = request.POST['first_name']
        name2 = request.POST['last_name']
        email1 = request.POST['email']
        add1 = request.POST['address']
        add2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        anji = Profile2(first_name=name1, last_name=name2, email=email1, address=add1, address2=add2, city=city,
                        state=state, zip=zip)
        anji.save()
        return redirect(success)

    return render(request, 'profile.html')


# About Me
def about_me(request):
    # info = Profile1.objects.all()
    # if request.method == 'POST':
    # user1 = request.POST.get('Username', False)
    # print(user1)
    # if 'Username' in request.POST:
    #     user1 = request.POST['Username']
    # else:
    #     is_private = False
    # place = Profile1.objects.get(Username='Anji')
    place = Profile1.objects.get(id='1')
    print(place)
    print(place.id)

    return render(request, "about_me.html", {'info': place})


# def testimage(request):
#     place = Profile1.objects.get(id=3)
#     print(place.id)
#
#     return render(request, 'login.html', {'info': place})

# @method_decorator(login_required, name='dispatch')
# class UserUpdateView(UpdateView):
#     model = Profile2
#     fields = ('first_name', 'last_name', 'email')
#     template_name = 'login.html'
#     success_url = reverse_lazy('my_account')
#
#     def get_object(self):
#         return self.request.user
# def upload_pic(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             m = ExampleModel.objects.get(id='1')
#             m.model_pic = form.cleaned_data['image']
#             m.save()
#             return HttpResponse('image upload success')
#     return HttpResponseForbidden('allowed only via POST')


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['Username'])
def newprofile(request):
    import pdb;
    pdb.set_trace()
    customer = Profile1.objects.all()


    if request.method == 'POST':
         import pdb;pdb.set_trace()
         form = CustomerForm(request.POST, request.FILES, instance=customer)
         if form.is_valid():
            form.save()


    context = {'form': form}
    return render(request, 'newprofile.html', context)

=s