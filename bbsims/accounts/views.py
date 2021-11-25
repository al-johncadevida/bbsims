from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import CreateView
from .forms import ResidentSignUpForm, OfficialSignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Resident
from datetime import datetime
from blog.models import Post
from dash.models import APost
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def register(request):
    date_today = datetime.now().date()
    return render(request, 'accounts/register.html', {'date_today':date_today})
def login_1(request):
    date_today = datetime.now().date()
    return render(request, 'accounts/login1.html', {'date_today':date_today})

class resident_register(CreateView):
    model = User
    form_class = ResidentSignUpForm
    template_name = 'accounts/resident_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('news-feed3')

@method_decorator(login_required, name='dispatch')
class official_register(CreateView):
    model = User
    form_class = OfficialSignUpForm
    template_name = 'accounts/official_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dash-board')


def login_resident(request):
    announcements = APost.objects.all().order_by('-date_posted')
    resident_post = Post.objects.all().order_by('-date_posted')
    # User = get_user_model()
    all_user = Resident.objects.all().order_by('-first_name')

    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('news-feed3')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'accounts/login_resident.html',
                  context={'announcements': announcements, 'resident_post': resident_post, 'all_user': all_user,'form':AuthenticationForm()})

def login_official(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_official==True:
                login(request,user)
                return redirect('dash-board')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'accounts/login_official.html',
                  context={'form':AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def u_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/u_profile.html', context)

def profile(request):
    return render(request, 'accounts/profile.html')


# def profile(request):
#     # announcement = APost.objects.all().order_by('-date_posted')
#     # resident_posts = Post.objects.all().order_by('-date_posted')
#     user = get_object_or_404(Resident, id=request.POST.get('user_id'))
#     user_post = Post.objects.filter(author=user).order_by('-date_posted')
#     return render(request, 'blog/profile.html', {'user_post': user_post,})




def a_profile(request):
    return render(request, 'accounts/a_profile.html')

def a_u_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('a_profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/a_u_profile.html', context)