# Generated by Django 5.0.2 on 2024-03-30 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GR', '0003_alter_addtocarproducts_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedBack',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('emailId', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('number', models.IntegerField(max_length=10)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
    ]
