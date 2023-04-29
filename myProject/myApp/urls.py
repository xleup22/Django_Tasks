from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
  
urlpatterns =[
path('', views.home, name='myApp-home'),
path('about', views.about, name='myApp-about'),
path('contact', views.contact, name='myApp-contact'),
path('signin', views.signin, name='myApp-signin'),
path('password', views.password, name='myApp-password'),
# path('profile', views.profile, name='myApp-profile'),
path('product1', views.product1, name='myApp-product1'),
path('product2', views.product2, name='myApp-product2'),
path('product3', views.product3, name='myApp-product3'),
path('smartwatch', views.smartwatch, name='myApp-smartwatch'),
path('smartphone', views.smartphone, name='myApp-smartphone'),
path('television', views.television, name='myApp-television'),
path('reg', views.reg, name='myApp-reg'),
 ]
 
urlpatterns += staticfiles_urlpatterns()
