from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('detail/<int:pk>/',views.detail,name='detail'),
	path('delete/<int:pk>/',views.delete,name='delete'),
	path('register/',views.register,name='register')
	

]