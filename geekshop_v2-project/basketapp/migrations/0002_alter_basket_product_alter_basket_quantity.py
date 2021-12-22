# Generated by Django 4.0 on 2021-12-15 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_descritption_product_description'),
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.product'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='количество'),
        ),
    ]
