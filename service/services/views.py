from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
