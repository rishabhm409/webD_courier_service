# Generated by Django 2.2.2 on 2019-06-25 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalzone', '0002_auto_20190624_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('qualification', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
                ('address', models.TextField()),
                ('contactno', models.CharField(max_length=50)),
                ('emailaddress', models.EmailField(max_length=254)),
                ('cv', models.FileField(upload_to='cv/')),
            ],
        ),
    ]
