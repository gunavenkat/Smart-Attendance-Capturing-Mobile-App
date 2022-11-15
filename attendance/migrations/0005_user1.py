# Generated by Django 4.1.3 on 2022-11-13 16:34

import attendance.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_delete_user1'),
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(default='', storage=attendance.storage.OverwriteStorage(), upload_to='profiles')),
            ],
        ),
    ]
