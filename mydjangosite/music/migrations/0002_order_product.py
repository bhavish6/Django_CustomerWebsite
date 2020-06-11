# Generated by Django 3.0.6 on 2020-05-29 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, null=True)),
                ('Price', models.FloatField(null=True)),
                ('Category', models.CharField(choices=[('indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=200, null=True)),
                ('Description', models.CharField(max_length=200, null=True)),
                ('Date_Created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]