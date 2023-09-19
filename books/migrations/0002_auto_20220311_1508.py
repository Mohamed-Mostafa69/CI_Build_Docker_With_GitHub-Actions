# Generated by Django 3.2.2 on 2022-03-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.RemoveField(
            model_name='book',
            name='num_pag',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publiacation_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='book',
            name='rating_count',
        ),
        migrations.RemoveField(
            model_name='book',
            name='text_review_count',
        ),
        migrations.AddField(
            model_name='book',
            name='average_rating',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='book',
            name='language_code',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='book',
            name='num_pages',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AddField(
            model_name='book',
            name='ratings_count',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='book',
            name='text_reviews_count',
            field=models.CharField(default='', max_length=70),
        ),
    ]
