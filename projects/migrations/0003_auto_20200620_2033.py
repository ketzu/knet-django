# Generated by Django 3.0.7 on 2020-06-20 18:33

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200615_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='git',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=stdimage.models.StdImageField(null=True, upload_to='projects/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
