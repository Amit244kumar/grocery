# Generated by Django 4.2.2 on 2024-02-09 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GR', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='addToCarProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('imageName', models.CharField(max_length=30)),
                ('user_Accounts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GR.useraccounts')),
            ],
        ),
    ]
