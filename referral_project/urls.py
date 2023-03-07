from django.contrib import admin
from django.urls import path
from app.views import index ,home



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('home/',home,name='home'),
]
