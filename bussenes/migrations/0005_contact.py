# Generated by Django 3.2.9 on 2021-11-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bussenes', '0004_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]