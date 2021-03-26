# Generated by Django 3.1.7 on 2021-03-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TushareStockBasic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ts_code', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=500)),
                ('enname', models.CharField(max_length=500)),
                ('market', models.CharField(max_length=100)),
                ('exchange', models.CharField(max_length=100)),
                ('curr_type', models.CharField(max_length=100)),
                ('list_status', models.CharField(max_length=100)),
                ('list_date', models.CharField(max_length=100)),
                ('delist_date', models.CharField(max_length=100)),
                ('is_hs', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tushare_stock_basic',
            },
        ),
    ]
