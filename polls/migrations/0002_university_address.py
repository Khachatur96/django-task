# Generated by Django 3.1.5 on 2021-01-29 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='address',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]