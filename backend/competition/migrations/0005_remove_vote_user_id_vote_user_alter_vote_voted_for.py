# Generated by Django 4.0.5 on 2023-01-07 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competition', '0004_alter_competition_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='user_id',
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vote',
            name='voted_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.participant', verbose_name='voted_for'),
        ),
    ]
