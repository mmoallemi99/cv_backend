# Generated by Django 2.2.4 on 2019-08-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20190816_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='resume_language',
            field=models.CharField(choices=[('en', 'English'), ('fa', 'فارسی')], max_length=30),
        ),
    ]
