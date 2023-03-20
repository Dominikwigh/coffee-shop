# Generated by Django 3.2 on 2023-03-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productreview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productreview',
            old_name='user',
            new_name='created_by',
        ),
        migrations.AlterField(
            model_name='productreview',
            name='stars',
            field=models.IntegerField(default=3),
        ),
    ]
