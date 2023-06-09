# Generated by Django 4.0.3 on 2023-06-06 04:05

import backend.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResetPasswordToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(max_length=100, unique=True)),
                ('data', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SendEmailEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('content', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('original_url', models.URLField()),
                ('short_url', models.CharField(max_length=100, unique=True)),
                ('click_count', models.PositiveIntegerField(default=0)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SignUpToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(max_length=100, unique=True)),
                ('data', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('auth_method', models.CharField(max_length=20)),
                ('is_banned', models.BooleanField(default=False)),
                ('company_name', models.CharField(blank=True, default='', max_length=255)),
                ('provides_service', models.CharField(blank=True, default='', max_length=255)),
                ('employee_size', models.CharField(blank=True, default='', max_length=255)),
                ('phone_number', models.CharField(blank=True, default='', max_length=20)),
                ('country', models.CharField(blank=True, default='', max_length=255)),
                ('has_on_boarded', models.BooleanField(default=False)),
                ('first_referrer', models.CharField(blank=True, default='', max_length=512)),
                ('first_url_params', models.JSONField(default=dict)),
                ('pending_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('referral_link_clicks', models.IntegerField(default=0)),
                ('referral_code', models.CharField(default=backend.models.generate_referral_code, max_length=12, unique=True)),
                ('referred_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=255)),
                ('data', models.JSONField()),
                ('ip', models.CharField(max_length=255)),
                ('user_agent', models.CharField(max_length=512, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='backend.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]