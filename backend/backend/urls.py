from django.contrib import admin
from django.urls import path
from progress.views import *
from home.views import *
from adhd.views import *
from rl_model.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('progress/', progress_tracking, name='progress_tracking'),
    path('update-time-spent/', update_time_spent, name='update_time_spent'),
    path('', home, name='home'),
    path('adhd/', adhd, name='adhd'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('api/chart-data/', chart_data, name='chart_data'),
]

urlpatterns += [
    path('signup/', signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]