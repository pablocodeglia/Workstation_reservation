# Generated by Django 4.0.4 on 2022-05-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0004_reservations_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='workstations',
            name='photo',
            field=models.ImageField(default='/static/ws_thumb1.png', upload_to='images/'),
        ),
    ]
