# Generated by Django 4.0.2 on 2022-02-17 03:20

import bookkeeperapi.validators.rating
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('synopsis', models.CharField(max_length=1200)),
                ('page_length', models.PositiveIntegerField()),
                ('goodreads_link', models.URLField()),
                ('image', models.ImageField(null=True, upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Bookkeep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.CharField(blank=True, max_length=500)),
                ('profile_pic', models.ImageField(null=True, upload_to=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_read', models.DateField()),
                ('rating', models.IntegerField(validators=[bookkeeperapi.validators.rating.validate_rating])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeperapi.book')),
                ('bookkeep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeperapi.bookkeep')),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeperapi.shelf')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeperapi.book')),
                ('bookkeep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeperapi.bookkeep')),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeperapi.shelf')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('datetime', models.CharField(max_length=500)),
                ('pag_num', models.IntegerField(default=0)),
                ('user_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeperapi.userbook')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookkeep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeperapi.bookkeep')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeperapi.post')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_follow', to='bookkeeperapi.bookkeep')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_follow', to='bookkeeperapi.bookkeep')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookkeeperapi.genre'),
        ),
    ]
