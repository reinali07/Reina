# Generated by Django 3.0.2 on 2020-02-29 20:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('date', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('concentration', models.FloatField(default=0)),
                ('result', models.FloatField(default=0)),
                ('eid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runexp.Session')),
            ],
        ),
    ]