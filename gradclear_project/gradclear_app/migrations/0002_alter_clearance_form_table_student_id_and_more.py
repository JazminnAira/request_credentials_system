# Generated by Django 4.0.6 on 2022-11-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradclear_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clearance_form_table',
            name='student_id',
            field=models.CharField(max_length=100, verbose_name='Student Id'),
        ),
        migrations.AlterField(
            model_name='graduation_form_table',
            name='student_id',
            field=models.CharField(max_length=100, verbose_name='Student Id'),
        ),
        migrations.AlterField(
            model_name='request_form_table',
            name='student_id',
            field=models.CharField(max_length=100, verbose_name='Student Id'),
        ),
    ]
