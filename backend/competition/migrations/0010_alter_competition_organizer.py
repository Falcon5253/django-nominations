# Generated by Django 4.0.5 on 2023-01-17 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competition', '0009_alter_competition_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition', to=settings.AUTH_USER_MODEL, verbose_name='organizer'),
        ),
    ]
