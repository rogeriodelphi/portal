# Generated by Django 3.2.11 on 2023-07-28 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]
