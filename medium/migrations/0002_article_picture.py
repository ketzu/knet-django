# Generated by Django 3.0.5 on 2020-05-05 18:17

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=stdimage.models.JPEGField(null=True, upload_to='medium/'),
        ),
    ]
