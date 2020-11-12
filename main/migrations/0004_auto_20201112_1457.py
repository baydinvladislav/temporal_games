# Generated by Django 2.2.12 on 2020-11-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201112_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a title of vacancy', max_length=200)),
                ('tag', models.CharField(blank=True, help_text='Enter a tag of job', max_length=200, null=True)),
                ('responsibility', models.CharField(help_text='Enter a responsibilities of vacancy', max_length=200)),
                ('requirement', models.CharField(help_text='Enter a requirements of vacancy', max_length=200)),
                ('nice_to_have', models.CharField(blank=True, help_text='Enter a "nice to have" of vacancy', max_length=200, null=True)),
                ('description', models.TextField(help_text='Enter a short description of vacancy', max_length=2000)),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='full_description',
        ),
        migrations.AddField(
            model_name='job',
            name='tag',
            field=models.CharField(blank=True, help_text='Enter a tag of job', max_length=200, null=True),
        ),
    ]