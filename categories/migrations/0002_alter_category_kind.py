# Generated by Django 3.2.6 on 2021-08-07 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='kind',
            field=models.CharField(choices=[('book', 'Book'), ('movie', 'Movie'), ('both', 'Both')], max_length=100),
        ),
    ]