# Generated by Django 2.2.7 on 2019-12-27 12:55

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to=polls.models.user_directory_path)),
            ],
        ),
    ]
