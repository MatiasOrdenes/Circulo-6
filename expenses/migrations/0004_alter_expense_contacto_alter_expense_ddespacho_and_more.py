# Generated by Django 5.0.6 on 2024-06-13 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_expense_contacto_expense_ddespacho_expense_dfactura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='contacto',
            field=models.CharField(default='Desconocido', max_length=255),
        ),
        migrations.AlterField(
            model_name='expense',
            name='ddespacho',
            field=models.CharField(default='Desconocido', max_length=255),
        ),
        migrations.AlterField(
            model_name='expense',
            name='dfactura',
            field=models.CharField(default='Desconocido', max_length=255),
        ),
        migrations.AlterField(
            model_name='expense',
            name='ncompra',
            field=models.TextField(default='Desconocido', max_length=255),
        ),
    ]