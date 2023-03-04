# Generated by Django 4.1.3 on 2023-03-03 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapitalInvestments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_capex_item1', models.FloatField(default=20000)),
                ('project_capex_item2', models.FloatField(default=20000)),
                ('total_project_capex', models.FloatField(default=40000)),
                ('equity_debt', models.FloatField(default=20)),
                ('debt_repayment_period', models.FloatField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='OperationalCosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_item1_variable', models.FloatField(default=20)),
                ('cost_item2_fixed', models.FloatField(default=2000)),
                ('cost_item2_annual_growth', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Others',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_tax_rate', models.FloatField(default=30)),
                ('interst_rate_debt', models.FloatField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Revenues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.FloatField(default=100)),
                ('annual_volume_growth', models.FloatField(default=1)),
                ('price', models.FloatField(default=100)),
                ('annual_price_growth', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Timelines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_capex', models.FloatField(default=2024)),
                ('end_capex', models.FloatField(default=2026)),
                ('start_operations', models.FloatField(default=2027)),
                ('asset_life', models.FloatField(default=25)),
            ],
        ),
    ]