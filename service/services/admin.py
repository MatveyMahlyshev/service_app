from django.contrib import admin
from clients.models import Client
from services.models import Service, Plan, Subscriprion

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(Subscriprion)