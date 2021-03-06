# Generated by Django 3.0.5 on 2020-05-10 17:41

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('picture', stdimage.models.JPEGField(null=True, upload_to='gallery/')),
                ('order', models.PositiveIntegerField(default=0)),
                ('in_gallery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photography.Gallery')),
            ],
            options={
                'ordering': ['order', '-pk'],
            },
        ),
        migrations.AddField(
            model_name='gallery',
            name='thumbnail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photography.Image'),
        ),
    ]
