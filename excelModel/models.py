from django.db import models

class Revenues(models.Model):
    volume = models.FloatField(null=False,default=100)
    annual_volume_growth = models.FloatField(null=False,default=1) # %
    price = models.FloatField(null=False,default=100) # 
    annual_price_growth = models.FloatField(null=False,default=1) # %

class OperationalCosts(models.Model):
    cost_item1_variable = models.FloatField(null=False,default=20) # %
    cost_item2_fixed = models.FloatField(null=False,default=2000) # 
    cost_item2_annual_growth = models.FloatField(null=False,default=1) # %

class CapitalInvestments(models.Model):
    project_capex_item1 = models.FloatField(null=False,default=20000) 
    project_capex_item2 = models.FloatField(null=False,default=20000) 
    total_project_capex = models.FloatField(null=False,default=40000) 
    equity_debt = models.FloatField(null=False,default=20) # %
    debt_repayment_period = models.FloatField(null=False,default=20) 

class Timelines(models.Model):
    start_capex = models.FloatField(null=False,default=2024)
    end_capex = models.FloatField(null=False,default=2026)
    start_operations = models.FloatField(null=False,default=2027)
    asset_life = models.FloatField(null=False,default=25)

class Others(models.Model):
    income_tax_rate = models.FloatField(null=False,default=30) # %
    interst_rate_debt = models.FloatField(null=False,default=5) # %