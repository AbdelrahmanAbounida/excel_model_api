from django.shortcuts import render
from .models import Revenues,OperationalCosts,CapitalInvestments, Timelines, Others
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RevenueSerializer, OperationalCostSerializer, CapitalInvestmentSerializer, TimelineSerializer, OtherSerializer

#################
# Revenues
#################
class RevenuesListCreateView(generics.ListCreateAPIView):
    queryset = Revenues.objects.all()
    serializer_class = RevenueSerializer
    permission_classes = [AllowAny] 

class RevenuesDetailEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Revenues.objects.all()
    serializer_class = RevenueSerializer
    permission_classes = [AllowAny] 

#################
# OperationalCosts
#################
class OperationalCostsListCreateView(generics.ListCreateAPIView):
    queryset = OperationalCosts.objects.all()
    serializer_class = OperationalCostSerializer
    permission_classes = [AllowAny] 

class OperationalCostsDetailEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OperationalCosts.objects.all()
    serializer_class = OperationalCostSerializer
    permission_classes = [AllowAny] 

#################
# CapitalInvestments
#################
class CapitalInvestmentsListCreateView(generics.ListCreateAPIView):
    queryset = CapitalInvestments.objects.all()
    serializer_class = CapitalInvestmentSerializer
    permission_classes = [AllowAny] 

class CapitalInvestmentsDetailEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CapitalInvestments.objects.all()
    serializer_class = CapitalInvestmentSerializer
    permission_classes = [AllowAny] 

#################
# Timelines
#################
class TimelinesListCreateView(generics.ListCreateAPIView):
    queryset = Timelines.objects.all()
    serializer_class = TimelineSerializer
    permission_classes = [AllowAny] 

class TimelinesDetailEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timelines.objects.all()
    serializer_class = TimelineSerializer
    permission_classes = [AllowAny] 

#################
# Others
#################
class OthersListCreateView(generics.ListCreateAPIView):
    queryset = Others.objects.all()
    serializer_class = OtherSerializer
    permission_classes = [AllowAny] 

class OthersDetailEditDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Others.objects.all()
    serializer_class = OtherSerializer
    permission_classes = [AllowAny] 
