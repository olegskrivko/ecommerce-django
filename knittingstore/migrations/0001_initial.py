# Generated by Django 4.2.7 on 2023-12-11 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pattern_pdf', models.FileField(blank=True, null=True, upload_to='pattern_pdfs/')),
                ('gender', models.CharField(choices=[('M', 'Men'), ('W', 'Women'), ('U', 'Unisex')], default='U', max_length=1)),
                ('age_group', models.CharField(choices=[('C', 'Children'), ('T', 'Teenagers'), ('A', 'Adults'), ('S', 'Seniors')], default='A', max_length=1)),
                ('difficulty_level', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('E', 'Expert')], default='B', max_length=1)),
                ('product_type', models.CharField(choices=[('H', 'Hat'), ('S', 'Scarf'), ('C', 'Coat'), ('SW', 'Sweater'), ('O', 'Other')], default='O', max_length=2)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knittingstore.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knittingstore.product')),
            ],
        ),
    ]
