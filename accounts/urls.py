

from django.urls import path
from django.contrib.auth import views as auth_views #pour que django fasse la difference entre les deux views et savoir lequel des deux choisir
from .forms import LoginFrom
from .import views


app_name= 'accounts'

urlpatterns = [
	#Leave as empty string for base url
  path('register/',views.register,name="register"), 
	path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user=True,authentication_form=LoginFrom),name="login"),
  path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html',next_page='accounts:login'),name="logout")
  ]