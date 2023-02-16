from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import Client
from .forms import ClientForm
from django.urls import reverse_lazy

class ClientsTemplateView(TemplateView):
  template_name = 'clients/clients.html'
  
  def get_context_data(self, **kwargs):
    context = super(ClientsTemplateView, self).get_context_data(**kwargs)
    context['clients'] = Client.objects.all()

    return context

class ClientsFormView(FormView):
    template_name = 'clients/clients_add.html'
  
    form_class = ClientForm

    success_url = reverse_lazy('clients-list')

    def form_valid(self, form):
      form.save()
      return super().form_valid(form) 