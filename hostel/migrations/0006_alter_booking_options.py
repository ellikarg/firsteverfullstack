# Generated by Django 3.2.21 on 2023-09-22 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0005_alter_room_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['room', 'check_in']},
        ),
    ]