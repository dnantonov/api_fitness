# Generated by Django 3.1.6 on 2021-09-04 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='activity',
            field=models.CharField(choices=[('Walking', 'Walking'), ('Running', 'Running'), ('Bike', 'Bike')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='end_activity',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='start_activity',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]