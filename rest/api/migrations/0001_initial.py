# Generated by Django 4.2.2 on 2023-06-18 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 6, 19, 1, 25, 7, 670438), editable=False)),
                ('due_date', models.DateTimeField(default=datetime.datetime(2023, 6, 19, 1, 25, 7, 670438))),
                ('status', models.CharField(choices=[('OPEN', 'open'), ('WORKING', 'working'), ('DONE', 'done'), ('OVERDUE', 'overdue')], default='OPEN', max_length=15)),
            ],
        ),
    ]
