from django.urls import path

from . import views

urlpatterns = [
    path('',views.login_page,name='login_page'),
	path('login/',views.login_view,name='login'),
	path('logout/',views.logout_view,name='logout'),
	]
