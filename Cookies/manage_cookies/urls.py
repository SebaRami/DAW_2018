from django.contrib import admin
from django.urls import path, include
from . import views
from .cookies import cookies_demo

urlpatterns = [

	path(r'',views.login1,name='login1'),
    path(r'page1/',views.page1,name='page1'),
    path(r'page2/',views.page2,name='page2'),
    path(r'login_cookie/',cookies_demo,name='login_cookie'),
    path('signup/',views.signup,name='signup'),	
    path('', include('django.contrib.auth.urls')),
]