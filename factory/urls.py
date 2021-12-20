from django.urls import path
from . import views

urlpatterns = [
    path('',views.login),
    path('login/',views.login),
    
    path('form/', views.form, name="add"),
    path('table/',views.table),
    path('delete<str:userid>/',views.delete),
    path('update<str:userid>/',views.update),
    path('signup/',views.signup),
    path('logout/',views.logout),
    path('details<str:datid>/',views.details),
   
    
]
