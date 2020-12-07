# Generated by Django 3.1.4 on 2020-12-06 06:50

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
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=264, verbose_name='Put a Title')),
                ('slug', models.SlugField(max_length=264, unique=True)),
                ('video_content', models.FileField(upload_to='videos', verbose_name='Upload video')),
                ('thumbnail', models.ImageField(blank=True, upload_to='thumbnails', verbose_name='Put Thumbnail')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
                ('videos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_comment', to='Its_Streaming_App.videos')),
            ],
            options={
                'ordering': ['-comment_date'],
            },
        ),
    ]