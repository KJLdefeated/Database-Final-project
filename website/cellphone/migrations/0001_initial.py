# Generated by Django 4.0.3 on 2022-12-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellphone_id', models.IntegerField(verbose_name='cellphone_id')),
                ('brand', models.CharField(max_length=100, verbose_name='brand')),
                ('model', models.CharField(max_length=100, verbose_name='model')),
                ('operating_system', models.CharField(max_length=100, verbose_name='operating_system')),
                ('internal_memory', models.FloatField(verbose_name='internal_memory')),
                ('RAM', models.FloatField(verbose_name='RAM')),
                ('performance', models.FloatField(verbose_name='performance')),
                ('main_camera', models.FloatField(verbose_name='main_camera')),
                ('selfie_camera', models.FloatField(verbose_name='selfie_camera')),
                ('battery_size', models.FloatField(verbose_name='battery_size')),
                ('screen_size', models.FloatField(verbose_name='screen_size')),
                ('weight', models.FloatField(verbose_name='weight')),
                ('price', models.FloatField(verbose_name='price')),
                ('release_date', models.DateField(auto_now=True, verbose_name='release_date')),
            ],
        ),
        migrations.CreateModel(
            name='rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.FloatField(verbose_name='user_id')),
                ('cellphone_id', models.IntegerField(verbose_name='cellphone_id')),
                ('rating', models.FloatField(verbose_name='rating')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.FloatField(verbose_name='user_id')),
                ('age', models.FloatField(verbose_name='age')),
                ('gender', models.CharField(max_length=100, verbose_name='gender')),
                ('occupation', models.CharField(max_length=100, verbose_name='occupation')),
            ],
        ),
    ]