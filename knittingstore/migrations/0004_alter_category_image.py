# Generated by Django 4.2.7 on 2024-01-03 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knittingstore', '0003_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/'),
        ),
    ]