# Generated by Django 2.1.3 on 2019-01-18 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20181113_0120'),
        ('pointsheets', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pointsheet',
            unique_together={('year', 'month', 'company')},
        ),
    ]
