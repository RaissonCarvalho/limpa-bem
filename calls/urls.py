from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClientsTemplateView.as_view(), name='clients-list'),
    path('clients-add/', views.ClientsFormView.as_view(), name='clients-add'),

]