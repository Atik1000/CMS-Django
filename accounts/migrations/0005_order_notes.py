# Generated by Django 3.1.4 on 2020-12-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201216_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='notes',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
