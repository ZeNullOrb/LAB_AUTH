# Generated by Django 4.1.7 on 2023-02-16 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_clinic_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
