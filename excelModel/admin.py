from django.contrib import admin
from .models import Revenues,OperationalCosts,CapitalInvestments, Timelines, Others

admin.site.register(Revenues)
admin.site.register(OperationalCosts)
admin.site.register(CapitalInvestments)
admin.site.register(Timelines)
admin.site.register(Others)

