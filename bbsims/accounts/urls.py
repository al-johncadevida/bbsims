from django.urls import path
from .import  views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('profile/', views.profile, name='profile'),
     path('u_profile/', views.u_profile, name='u_profile'),
     path('a_profile/', views.a_profile, name='a_profile'),
     path('a_u_profile/', views.a_u_profile, name='a_u_profile'),
     path('resident_register/',views.resident_register.as_view(), name='resident_register'),
     path('official_register/',views.official_register.as_view(), name='official_register'),
     path('login_1/',views.login_1, name='login_1'),
     path('login-resident/',views.login_resident, name='login_resident'),
     path('login-official/',views.login_official, name='login_official'),
     path('logout/',views.logout_view, name='logout'),

]