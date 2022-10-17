# Generated by Django 4.1.2 on 2022-10-14 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_delete_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDIImage', models.ImageField(upload_to='photos/', verbose_name='Images')),
                ('PRDIProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Product')),
            ],
        ),
    ]
