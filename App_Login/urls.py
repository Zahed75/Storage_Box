from django.conf.urls import url
from django.urls import path
from App_Login import views

app_name='App_Login'

urlpatterns = [
    
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('change_profile/',views.user_change,name='change_profile'),
    path('profile/',views.profile,name='profile'),
    path('add-picture',views.add_pro_pic,name='add_pro_pic'),
    path('change-picture/',views.change_pro_pic,name='change_pro_pic'),
    path('password/',views.pass_change,name='pass_change'),
]