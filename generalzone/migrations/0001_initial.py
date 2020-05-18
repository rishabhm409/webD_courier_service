# Generated by Django 2.2.2 on 2019-06-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('subject', models.CharField(max_length=100)),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.EmailField(max_length=254)),
                ('compalintext', models.TextField()),
            ],
        ),
    ]