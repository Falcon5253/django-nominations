# Generated by Django 4.0.5 on 2023-01-04 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='competition_id',
        ),
    ]
