# Generated by Django 3.0.5 on 2020-06-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_fronttext'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontIcons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
