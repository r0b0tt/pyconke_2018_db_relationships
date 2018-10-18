# Generated by Django 2.1.2 on 2018-10-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationships', '0004_auto_20181018_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='students',
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(related_name='subject_students', to='relationships.Subject'),
        ),
    ]