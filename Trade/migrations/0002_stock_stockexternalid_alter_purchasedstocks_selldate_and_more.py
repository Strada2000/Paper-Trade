# Generated by Django 5.0.3 on 2024-04-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='stockExternalId',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='purchasedstocks',
            name='sellDate',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='purchasedstocks',
            name='sellValue',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
