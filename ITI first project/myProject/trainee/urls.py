from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', trainee_list, name='trainee_list'),
    path('insert', insert_trainee, name='insert_trainee'),
    path('update/<int:id>', update_trainee, name='update_trainee'),
    path('delete/<int:id>', delete_trainee, name='delete_trainee'),
]