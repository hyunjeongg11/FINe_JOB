# Generated by Django 4.2.8 on 2024-05-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_date', models.DateField()),
                ('cur_unit', models.CharField(max_length=100)),
                ('cur_nm', models.TextField()),
                ('ttb', models.TextField()),
                ('tts', models.TextField()),
                ('deal_bas_r', models.TextField()),
            ],
        ),
    ]
