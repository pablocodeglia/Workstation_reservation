# Generated by Django 4.0.4 on 2022-05-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0007_alter_workstations_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workstations',
            name='photo',
            field=models.ImageField(default='workstations/ws_thumb1.png', upload_to='workstations/'),
        ),
    ]
