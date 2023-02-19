from django.contrib import admin
from calls.models import Client, Call, Service

# Register your models here.
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Call)