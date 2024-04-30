# Generated by Django 5.0.4 on 2024-04-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='needhelp',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='file/'),
        ),
        migrations.AddField(
            model_name='needhelp',
            name='let',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='needhelp',
            name='log',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
