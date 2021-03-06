# Generated by Django 3.0.5 on 2020-05-14 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videography', '0002_video_description'),
        ('photography', '0002_auto_20200510_2130'),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videography.Video')),
            ],
        ),
        migrations.CreateModel(
            name='FrontGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photography.Gallery')),
            ],
        ),
    ]
