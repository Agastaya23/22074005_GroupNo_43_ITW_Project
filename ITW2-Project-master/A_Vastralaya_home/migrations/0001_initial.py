# Generated by Django 4.2.7 on 2023-11-02 06:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(default=datetime.datetime(2023, 11, 2, 6, 15, 21, 933709, tzinfo=datetime.timezone.utc))),
                ('phoneNum', models.CharField(default='+911234567890', max_length=15)),
                ('email', models.EmailField(default='johndoe@email.com', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('addr1', models.CharField(max_length=200)),
                ('fname', models.CharField(default='John', max_length=100)),
                ('lname', models.CharField(default='Doe', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_rating', models.DecimalField(decimal_places=1, max_digits=5)),
                ('p_description', models.CharField(max_length=500)),
                ('p_buycount', models.IntegerField()),
                ('p_brand', models.CharField(max_length=100)),
                ('p_category', models.CharField(max_length=100)),
                ('p_image', models.ImageField(upload_to='static/images/')),
                ('p_price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A_Vastralaya_home.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.DecimalField(decimal_places=2, default=10000.0, max_digits=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A_Vastralaya_home.orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A_Vastralaya_home.products')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A_Vastralaya_home.products'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='A_Vastralaya_home.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
