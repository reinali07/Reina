# Generated by Django 3.0.2 on 2020-02-29 23:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('runexp', '0003_auto_20200229_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experiment',
            name='edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
