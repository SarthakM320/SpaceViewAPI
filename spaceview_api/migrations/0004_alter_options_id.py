# Generated by Django 4.0.4 on 2022-06-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceview_api', '0003_alter_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]