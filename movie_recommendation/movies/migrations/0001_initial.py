# Generated by Django 4.2.6 on 2023-11-07 10:04

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
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug_title', models.SlugField(unique=True)),
                ('overview', models.TextField()),
                ('keywords', models.TextField()),
                ('production_companies', models.TextField()),
                ('production_countries', models.TextField()),
                ('original_language', models.CharField(max_length=20)),
                ('genres', models.CharField(max_length=200)),
                ('runtime', models.FloatField()),
                ('budget', models.IntegerField()),
                ('rating', models.FloatField()),
                ('histories', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
