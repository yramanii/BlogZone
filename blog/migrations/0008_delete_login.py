# Generated by Django 3.2.5 on 2021-07-28 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_delete_signup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
    ]
