# Generated by Django 2.1.7 on 2019-04-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('image1', models.ImageField(upload_to='media/')),
                ('image2', models.ImageField(upload_to='media/')),
                ('image3', models.ImageField(upload_to='media/')),
                ('price', models.CharField(max_length=100)),
                ('buildingtype', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('postedon', models.CharField(max_length=100)),
                ('postedby', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('image', models.ImageField(upload_to='media/')),
                ('usertype', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
