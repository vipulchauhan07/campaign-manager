# Generated by Django 5.0 on 2024-03-16 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='campaign',
            table='campaign',
        ),
        migrations.AlterModelTable(
            name='campaignowner',
            table='campaign_owner',
        ),
        migrations.AlterModelTable(
            name='owner',
            table='owner',
        ),
        migrations.AlterModelTable(
            name='targetaudience',
            table='target_audience',
        ),
    ]
