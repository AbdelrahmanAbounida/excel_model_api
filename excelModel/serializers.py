from .models import Revenues,OperationalCosts,CapitalInvestments, Timelines, Others
from rest_framework.serializers import ModelSerializer


class RevenueSerializer(ModelSerializer):
    class Meta:
        model = Revenues
        fields = "__all__"

class OperationalCostSerializer(ModelSerializer):
    class Meta:
        model = OperationalCosts
        fields = "__all__"

class CapitalInvestmentSerializer(ModelSerializer):
    class Meta:
        model = CapitalInvestments
        fields = "__all__"

class TimelineSerializer(ModelSerializer):
    class Meta:
        model = Timelines
        fields = "__all__"

class OtherSerializer(ModelSerializer):
    class Meta:
        model = Others
        fields = "__all__"