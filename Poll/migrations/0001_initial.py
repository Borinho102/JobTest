# Generated by Django 3.1 on 2021-01-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=256, verbose_name='Task Label')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
    ]
