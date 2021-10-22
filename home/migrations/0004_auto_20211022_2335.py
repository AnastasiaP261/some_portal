# Generated by Django 3.2.8 on 2021-10-22 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_auto_20211022_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentnews',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentpublication',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='dislikes_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='likes_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commentpublication',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]