# Generated by Django 4.0.5 on 2022-07-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceview_api', '0009_alter_options_question_alter_options_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='decision_status',
            field=models.CharField(choices=[('1', 'Liberal'), ('2', 'Socialist')], default='2', max_length=9),
        ),
        migrations.AddField(
            model_name='user',
            name='employment_status',
            field=models.CharField(choices=[('1', 'Employer'), ('2', 'Employee'), ('3', 'Self Employed'), ('4', 'Unemployed'), ('5', 'Student')], default='5', max_length=9),
        ),
        migrations.AddField(
            model_name='user',
            name='marital_status',
            field=models.CharField(choices=[('1', 'Married'), ('2', 'Unmarried')], default='2', max_length=9),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('1', 'male'), ('2', 'female'), ('3', 'Prefer not to say')], default='1', max_length=9),
        ),
    ]
