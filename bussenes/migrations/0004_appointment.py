# Generated by Django 3.2.9 on 2021-11-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussenes', '0003_auto_20211118_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
            ],
        ),
    ]
