# Generated by Django 4.1.3 on 2023-03-23 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_alter_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(choices=[(None, 'Choose country'), ('Russia', 'Russia'), ('US', 'US')], max_length=20),
        ),
    ]
