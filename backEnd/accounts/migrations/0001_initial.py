# Generated by Django 4.2.8 on 2024-05-23 01:29

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(max_length=20)),
                ('birthday', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('남성', '남성'), ('여성', '여성')], max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_img_index', models.IntegerField()),
                ('asset', models.IntegerField(null=True)),
                ('salary', models.IntegerField(null=True)),
                ('interest_industry', models.CharField(choices=[('IT', 'IT'), ('서비스', '서비스'), ('금융', '금융'), ('보험', '보험'), ('인사', '인사'), ('노무', '노무'), ('회계', '회계'), ('세무', '세무'), ('재무', '재무'), ('디자인', '디자인'), ('생산', '생산'), ('영업', '영업'), ('상품기획', '상품기획'), ('교육', '교육'), ('R&D', 'R&D'), ('의료', '의료'), ('건축', '건축'), ('전기', '전기'), ('기계', '기계'), ('고객상담', '고객상담'), ('운송', '운송'), ('미디어', '미디어'), ('스포츠', '스포츠'), ('복지', '복지')], max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
