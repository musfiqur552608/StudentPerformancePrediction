# Generated by Django 4.0.1 on 2022-03-14 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sppapp', '0004_remove_studentperformance_attendence_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentperformance',
            name='final',
        ),
    ]