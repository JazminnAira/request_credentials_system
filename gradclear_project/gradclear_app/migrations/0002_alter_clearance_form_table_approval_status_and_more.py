# Generated by Django 4.0.6 on 2022-10-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradclear_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clearance_form_table',
            name='approval_status',
            field=models.CharField(default='ON PROGRESS', max_length=15, verbose_name='Approval Status'),
        ),
        migrations.AlterField(
            model_name='graduation_form_table',
            name='approval_status',
            field=models.CharField(default='ON PROGRESS', max_length=15, verbose_name='Approval Status'),
        ),
    ]
