# Generated by Django 4.0.3 on 2022-06-24 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizer', '0001_initial'),
        ('nominations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(verbose_name='Дата')),
                ('nomination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition', to='nominations.nomination', verbose_name='nomination')),
                ('organizer_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='competition', to='organizer.organizer', verbose_name='organizer')),
            ],
            options={
                'verbose_name': 'Номинация',
                'verbose_name_plural': 'Номинации',
            },
        ),
    ]