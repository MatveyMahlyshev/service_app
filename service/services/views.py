from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from .models import Subscription, Plan
from .serializers import SubscriptionSerializer
from django.db.models import Prefetch

class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client', 
                 queryset=Client.objects.all().select_related('user').only('company_name',
                                                              'user__email'),),

        # Prefetch('plan', queryset=Plan.objects.all().only('plan_type', 'discount_percent')
        #),
        )
    serializer_class = SubscriptionSerializer
