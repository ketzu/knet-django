# Generated by Django 3.0.5 on 2020-05-10 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photography.Image'),
        ),
    ]
