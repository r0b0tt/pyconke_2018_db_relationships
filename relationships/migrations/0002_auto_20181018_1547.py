# Generated by Django 2.1.2 on 2018-10-18 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationships', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=100, unique=True)),
                ('amount', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_customer', to='relationships.Customer')),
            ],
        ),
        migrations.AlterField(
            model_name='passport',
            name='passport_holder',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='passport_citizen', to='relationships.Citizen'),
        ),
    ]