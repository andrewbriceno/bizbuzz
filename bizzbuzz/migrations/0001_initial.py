# Generated by Django 3.0.7 on 2020-06-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Article Title')),
                ('url', models.TextField(verbose_name='Article URL')),
                ('expiration_date', models.DateTimeField(auto_now_add=True)),
                ('summary', models.TextField(verbose_name='Article Summary')),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(verbose_name='Username')),
                ('apple', models.BooleanField(default=True)),
                ('google', models.BooleanField(default=True)),
                ('facebook', models.BooleanField(default=True)),
                ('microsoft', models.BooleanField(default=True)),
            ],
        ),
    ]