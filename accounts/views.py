from django.shortcuts import render,redirect
from .forms import UserForm,ProfileForm
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    form = UserForm()
    profile_form= ProfileForm()
    if request.user.is_authenticated:
        return redirect('posts:home')
    if request.method == 'POST':
        form = UserForm(request.POST)
        profile_form= ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user= form.save(commit=False)
            profile= profile_form.save(commit=False)
            profile.user= user
            user.save()
            profile.save()
            return redirect('posts:home')
        else:
            form = UserForm()
            profile_form= ProfileForm()
        
    context = {'form': form,'profile':profile_form}
    return render(request, 'accounts/register.html', context)



# def register(request):
#     if request.user.is_authenticated:
#         return redirect('posts:home')
    
#     form = UserForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('posts:home')
            
#     context = {'form': form}
#     return render(request, 'accounts/register.html', context)

