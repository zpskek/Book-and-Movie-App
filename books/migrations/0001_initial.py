# Generated by Django 3.2.5 on 2021-07-16 03:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('cover_image', models.ImageField(blank=True, upload_to='book_cover_images')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('category', models.ForeignKey(limit_choices_to=models.Q(('kind', 'both'), ('kind', 'book'), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='categories.category')),
                ('writer', models.ForeignKey(limit_choices_to={'kind': 'writer'}, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='people.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
