# Generated by Django 3.0.6 on 2020-07-19 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200719_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
