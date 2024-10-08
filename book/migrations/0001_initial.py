# Generated by Django 5.0.6 on 2024-05-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Book_Name')),
                ('author', models.CharField(max_length=30, verbose_name='Author')),
                ('category', models.CharField(choices=[('Novel', 'Novel'), ('Comic_books', 'Comic_books'), ('Romantic_books', 'Romantic_books'), ('fictional_books', 'fictional_books')], max_length=30)),
                ('description', models.TextField()),
            ],
        ),
    ]
