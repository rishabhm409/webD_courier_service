# Generated by Django 2.2.2 on 2019-06-26 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalzone', '0003_carrer'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
