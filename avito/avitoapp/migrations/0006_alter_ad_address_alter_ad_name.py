# Generated by Django 4.2.6 on 2023-10-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avitoapp', '0005_ad_phone_alter_ad_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
