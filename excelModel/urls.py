from django.urls import path, include
from .views import (RevenuesListCreateView,RevenuesDetailEditDeleteView,
                    OperationalCostsListCreateView, OperationalCostsDetailEditDeleteView,
                    CapitalInvestmentsListCreateView, CapitalInvestmentsDetailEditDeleteView,
                    TimelinesListCreateView, TimelinesDetailEditDeleteView,
                    OthersListCreateView, OthersDetailEditDeleteView)

app_name = 'excelModel'

urlpatterns = [

    path('revenues/',RevenuesListCreateView.as_view(),name="RevenuesListCreateView"),
    path('revenues/<int:pk>',RevenuesDetailEditDeleteView.as_view(),name="RevenuesDetailEditDeleteView"),

    path('operationalCosts/',OperationalCostsListCreateView.as_view(),name="OperationalCostsListCreateView"),
    path('operationalCosts/<int:pk>',OperationalCostsDetailEditDeleteView.as_view(),name="OperationalCostsDetailEditDeleteView"),

    path('capital_investments/',CapitalInvestmentsListCreateView.as_view(),name="CapitalInvestmentsListCreateView"),
    path('capital_investments/<int:pk>',CapitalInvestmentsDetailEditDeleteView.as_view(),name="CapitalInvestmentsDetailEditDeleteView"),

    path('timelines/',TimelinesListCreateView.as_view(),name="TimelinesListCreateView"),
    path('timelines/<int:pk>',TimelinesDetailEditDeleteView.as_view(),name="TimelinesDetailEditDeleteView"),

    path('others/',OthersListCreateView.as_view(),name="OthersListCreateView"),
    path('others/<int:pk>',OthersDetailEditDeleteView.as_view(),name="OthersDetailEditDeleteView"),

]