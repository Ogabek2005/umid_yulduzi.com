# Generated by Django 5.0.4 on 2024-04-26 13:44

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField()),
                ('media_file', models.FileField(upload_to='blog_media/', verbose_name='Media file')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(code='invalid_phone', message='Telefon raqam xato kiritildi', regex='^\\+998\\d{9}$')], verbose_name='Phone number')),
                ('first_name', models.CharField(max_length=250, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=250, verbose_name='Last Name')),
                ('description', models.TextField()),
                ('card_number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Faqat sonlardan tashkil topgan qiymat kiriting.', regex='^\\d+$')], verbose_name='Card number')),
                ('passport_series', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(message='Passport seriya xato kiritildi', regex='^[A-Z]+$')], verbose_name='Passport series')),
                ('passport_number', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='Faqat sonlardan tashkil topgan qiymat kiriting.', regex='^\\d+$')], verbose_name='Passport number')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
                ('media_file', models.FileField(upload_to='claim_media/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Amount')),
                ('dedlayn', models.DateTimeField(blank=True, null=True)),
                ('claim', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='confirmations', to='common.claim', verbose_name='Confirmation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('sponsor_amount', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Sponsor amount')),
                ('sponsor_name', models.CharField(blank=True, default='Anonim', max_length=255, null=True, verbose_name='Sponsor name')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('payment_type', models.CharField(max_length=250, verbose_name='Payment type')),
                ('claim', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sponsors', to='common.claim', verbose_name='Sponsor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
