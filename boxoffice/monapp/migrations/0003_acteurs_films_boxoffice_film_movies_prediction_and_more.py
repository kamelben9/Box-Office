# Generated by Django 4.2.11 on 2024-04-09 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0002_actor_director_movie_remove_boxoffice_film_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acteurs_films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acteurs', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'actors',
            },
        ),
        migrations.CreateModel(
            name='Boxoffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boxoffice', models.IntegerField()),
            ],
            options={
                'db_table': 'boxoffice',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=500)),
                ('distributeur', models.CharField(max_length=500)),
                ('genre', models.CharField(default='Unknown', max_length=100)),
            ],
            options={
                'db_table': 'dataset_model_ML',
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=500)),
                ('image', models.URLField()),
                ('genre', models.CharField(default='Unknown', max_length=100)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction', models.FloatField()),
                ('titre', models.CharField(max_length=500)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monapp.movies')),
            ],
            options={
                'db_table': 'prediction',
            },
        ),
        migrations.RemoveField(
            model_name='movie',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.AddField(
            model_name='boxoffice',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monapp.movies'),
        ),
        migrations.AddField(
            model_name='acteurs_films',
            name='film_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monapp.film'),
        ),
    ]
