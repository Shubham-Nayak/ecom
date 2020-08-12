# Generated by Django 3.0.8 on 2020-08-11 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_auto_20200811_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=2500, null=True)),
                ('price', models.CharField(max_length=50)),
                ('stock', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Category')),
            ],
        ),
    ]
