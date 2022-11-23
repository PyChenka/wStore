# Generated by Django 4.1.3 on 2022-11-21 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(default='')),
                ('image', models.ImageField(upload_to='blog/%Y/%m/%d/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('products', models.ManyToManyField(blank=True, db_table='article_products', related_name='articles', to='shop.product')),
            ],
            options={
                'ordering': ['-time_create'],
            },
        ),
    ]