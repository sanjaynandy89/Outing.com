# Generated by Django 2.2.3 on 2019-08-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('img', models.ImageField(upload_to='pics')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
