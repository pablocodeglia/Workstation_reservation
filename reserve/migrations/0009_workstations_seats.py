# Generated by Django 4.0.4 on 2022-05-20 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0008_alter_workstations_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='workstations',
            name='seats',
            field=models.IntegerField(default=1, max_length=2),
        ),
    ]
