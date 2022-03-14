# Generated by Django 4.0.1 on 2022-03-04 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendence', models.IntegerField()),
                ('homeWork', models.IntegerField()),
                ('classTest', models.IntegerField()),
                ('tutorialWatching', models.IntegerField()),
                ('examResult', models.IntegerField()),
                ('quiz', models.IntegerField()),
                ('assignment', models.IntegerField()),
                ('extraCA', models.IntegerField()),
                ('readingNotes', models.IntegerField()),
            ],
        ),
    ]