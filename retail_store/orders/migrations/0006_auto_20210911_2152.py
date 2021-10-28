# Generated by Django 3.2.6 on 2021-09-11 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.contact', verbose_name='contact'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_info',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='orders.productinfo', verbose_name='product detail'),
            preserve_default=False,
        ),
    ]
