# Generated by Django 4.1.3 on 2022-11-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_alter_report_turnover'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(null=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]