from django.contrib import admin
from clients.models import Client
from services.models import Service, Plan, Subscription

@admin.register(Client)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'full_adress')

@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_price',)

@admin.register(Plan)
class PlanModelAdmin(admin.ModelAdmin):
    list_display = ('plan_type', 'discount_percent',)


@admin.register(Subscription)
class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'plan',)