from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home),
       path('home/<str:email>', views.profile),
    path('logout', views.home),
    path('payment/', views.payment),
    path('register', views.register),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('history/<str:id>', views.history),
      path('editprofile/', views.editprofile),
      path('donepayment/<str:id>', views.donepayment),
      path('cancelpayment/<str:id>', views.cancelpayment),

]