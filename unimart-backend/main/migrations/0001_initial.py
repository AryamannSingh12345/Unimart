# Generated by Django 4.0.2 on 2022-03-29 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email_id', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='seller_post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_index=True, max_length=64)),
                ('price', models.IntegerField()),
                ('exchange_items', models.CharField(max_length=64)),
                ('img', models.ImageField(upload_to='photos')),
                ('image_name', models.CharField(max_length=128)),
                ('product_description', models.TextField()),
                ('preferred_location', models.TextField()),
                ('preferred_contact', models.CharField(max_length=64)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='buyer_post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_index=True, max_length=64)),
                ('budget_range', models.CharField(max_length=64)),
                ('preferred_location', models.TextField()),
                ('preference_details', models.TextField()),
                ('preferred_contact', models.CharField(max_length=64)),
                ('date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
