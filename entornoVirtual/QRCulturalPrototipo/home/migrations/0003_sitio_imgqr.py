# Generated by Django 2.1.5 on 2019-02-08 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190207_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio',
            name='imgQR',
            field=models.ImageField(blank=True, null=True, upload_to='imagenQR'),
        ),
    ]
