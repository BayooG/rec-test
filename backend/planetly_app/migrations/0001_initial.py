# Generated by Django 3.0.2 on 2021-10-13 17:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsageType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('unit', models.CharField(max_length=20)),
                ('factor', models.FloatField()),
            ],
            options={
                'verbose_name': 'UsageType',
                'verbose_name_plural': 'UsageTypes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('usage_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('usage_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planetly_app.UsageType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planetly_app.User')),
            ],
            options={
                'verbose_name': 'Usage',
                'verbose_name_plural': 'Usage',
            },
        ),
    ]
