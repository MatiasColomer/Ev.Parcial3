# Generated by Django 5.0.6 on 2024-07-03 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_purchase_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={},
        ),
        migrations.AlterField(
            model_name='purchase',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]