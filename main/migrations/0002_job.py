# Generated by Django 2.2.12 on 2020-11-12 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a title of job', max_length=200)),
                ('short_description', models.TextField(help_text='Enter a short description of job', max_length=1000)),
                ('full_description', models.TextField(help_text='Enter a full description of job', max_length=3000)),
            ],
        ),
    ]
