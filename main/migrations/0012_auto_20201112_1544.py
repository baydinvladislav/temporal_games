# Generated by Django 2.2.12 on 2020-11-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201112_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='nice_to_have_1',
            field=models.CharField(blank=True, help_text='Enter a nice to have of vacancy', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='nice_to_have_2',
            field=models.CharField(blank=True, help_text='Enter a nice to have of vacancy', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='requirement_1',
            field=models.CharField(blank=True, help_text='Enter a requirement of vacancy', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='requirement_2',
            field=models.CharField(blank=True, help_text='Enter a requirement of vacancy', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='requirement_3',
            field=models.CharField(blank=True, help_text='Enter a requirement of vacancy', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='responsibility_1',
            field=models.CharField(blank=True, help_text='Enter a responsibility of vacancy', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='responsibility_2',
            field=models.CharField(blank=True, help_text='Enter a responsibility of vacancy', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='responsibility_3',
            field=models.CharField(blank=True, help_text='Enter a responsibility of vacancy', max_length=300, null=True),
        ),
    ]
