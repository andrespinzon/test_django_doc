# Generated by Django 3.1.5 on 2021-01-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=95, verbose_name='Name')),
                ('date', models.DateField(auto_now_add=True, db_index=True, verbose_name='Date')),
            ],
        ),
    ]