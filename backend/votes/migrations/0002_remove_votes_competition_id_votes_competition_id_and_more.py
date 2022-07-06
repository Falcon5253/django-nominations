# Generated by Django 4.0.3 on 2022-06-24 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competition', '0001_initial'),
        ('participant', '0002_alter_participant_participations_number'),
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='competition_id',
        ),
        migrations.AddField(
            model_name='votes',
            name='competition_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='competition.competition', verbose_name='competition'),
        ),
        migrations.RemoveField(
            model_name='votes',
            name='user_id',
        ),
        migrations.AddField(
            model_name='votes',
            name='user_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.RemoveField(
            model_name='votes',
            name='voted_for',
        ),
        migrations.AddField(
            model_name='votes',
            name='voted_for',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='participant.participant', verbose_name='voted_for'),
        ),
    ]
