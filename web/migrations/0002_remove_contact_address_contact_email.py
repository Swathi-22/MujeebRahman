# Generated by Django 4.0.2 on 2022-04-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
