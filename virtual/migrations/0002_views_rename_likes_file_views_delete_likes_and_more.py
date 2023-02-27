# Generated by Django 4.1.3 on 2023-02-27 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('virtual', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='file',
            old_name='likes',
            new_name='views',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
        migrations.AddField(
            model_name='views',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_view', to='virtual.file'),
        ),
        migrations.AddField(
            model_name='views',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_view', to=settings.AUTH_USER_MODEL),
        ),
    ]
