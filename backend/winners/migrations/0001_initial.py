# Generated by Django 4.0.3 on 2022-06-24 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competition', '0001_initial'),
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competititon_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='competition.competition', verbose_name='competition')),
                ('participant_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='participant.participant', verbose_name='participant')),
            ],
            options={
                'verbose_name': 'Победитель',
                'verbose_name_plural': 'Победители',
            },
        ),
    ]
