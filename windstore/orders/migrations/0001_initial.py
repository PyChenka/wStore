# Generated by Django 4.1.3 on 2022-12-07 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0002_alter_gallery_image_alter_product_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('postal_code', models.CharField(max_length=50)),
                ('country', models.CharField(choices=[('Россия', 'Россия'), ('US', 'US')], max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-time_create'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='shop.product')),
            ],
        ),
    ]
