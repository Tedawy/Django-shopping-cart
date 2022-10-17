# Generated by Django 4.1.2 on 2022-10-14 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-PRDPrice']},
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='PRDDesc',
            field=models.TextField(default=None, verbose_name='Product Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCategory',
            field=models.CharField(choices=[('Fruits', 'Fruits'), ('Vegetables', 'Vegetables')], max_length=15, null=True, verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDName',
            field=models.CharField(max_length=30, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDQuantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Quantity'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDIImage', models.ImageField(upload_to='photos/', verbose_name='Images')),
                ('PRDIProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Product')),
            ],
        ),
    ]
