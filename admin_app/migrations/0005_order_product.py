# Generated by Django 4.2.7 on 2023-12-03 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0004_delete_order_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_app.product')),
            ],
        ),
    ]
