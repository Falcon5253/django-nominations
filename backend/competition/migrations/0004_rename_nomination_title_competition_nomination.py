# Generated by Django 4.0.5 on 2022-11-30 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0003_rename_nomination_competition_nomination_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='nomination_title',
            new_name='nomination',
        ),
    ]