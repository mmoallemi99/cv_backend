# Generated by Django 2.2.4 on 2019-08-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20190816_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='about',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
