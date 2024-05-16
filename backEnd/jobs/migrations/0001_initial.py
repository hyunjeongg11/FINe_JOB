# Generated by Django 4.2.8 on 2024-05-16 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('company', models.TextField()),
                ('url', models.TextField()),
                ('deadline', models.TextField()),
                ('location', models.TextField()),
                ('experience', models.TextField()),
                ('requirement', models.TextField()),
                ('jobtype', models.TextField()),
            ],
        ),
    ]
