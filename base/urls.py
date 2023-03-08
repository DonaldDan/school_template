from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('',views.home, name="home"),
    path('logout/',views.logoutUser,name="logout"),
    path('school/<str:pk>/',views.school,name="school"),
    path('register/',views.register,name="register"),
    #path('result/',views.result,name="result"),
    #path('national/',views.national,name="national"),
]