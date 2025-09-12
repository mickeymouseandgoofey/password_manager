""" from django.urls import path
from . import views

urlpatterns = [
    path('', views.vault_home, name='vault_home'),  # new
    path('add/', views.add_credential, name='add_credential'),
] """

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_credential, name='add_credential'),
    path('dashboard/', views.dashboard, name='dashboard'),  # 👈 this is the fix
]



from . import views

urlpatterns += [
    path('register/', views.register, name='register'),
]
