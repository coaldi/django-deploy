# Generated by Django 3.2.8 on 2021-11-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_gambar_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gambar',
            name='gambar',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='gambar',
            name='judul_gambar',
            field=models.CharField(max_length=100),
        ),
    ]
