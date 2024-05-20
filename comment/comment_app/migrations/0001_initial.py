# Generated by Django 3.0.3 on 2024-05-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField()),
                ('comment', models.TextField()),
                ('user', models.CharField(max_length=100)),
                ('product_id', models.IntegerField()),
                ('type_product', models.CharField(max_length=100)),
            ],
        ),
    ]
