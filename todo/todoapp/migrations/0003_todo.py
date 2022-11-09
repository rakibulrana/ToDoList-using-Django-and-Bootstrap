# Generated by Django 3.2.16 on 2022-10-12 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('todoapp', '0002_delete_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
