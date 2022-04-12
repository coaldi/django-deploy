# Generated by Django 3.2.8 on 2021-11-30 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20211130_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gambarblog',
            name='blogs',
            field=models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='blog.blog'),
        ),
        migrations.AlterField(
            model_name='gambarblog',
            name='gambar',
            field=models.ImageField(default='NULL', upload_to=''),
        ),
        migrations.AlterField(
            model_name='gambarblog',
            name='judul_gambar',
            field=models.CharField(default='NULL', max_length=100),
        ),
    ]