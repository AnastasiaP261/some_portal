# Generated by Django 3.2.8 on 2021-10-22 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_likescommentnews_likescommentpublication_likesnews_likespublications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likescommentnews',
            old_name='id_com_new',
            new_name='id_posts',
        ),
        migrations.RenameField(
            model_name='likescommentpublication',
            old_name='id_com_pub',
            new_name='id_posts',
        ),
        migrations.RenameField(
            model_name='likesnews',
            old_name='id_new',
            new_name='id_posts',
        ),
        migrations.RenameField(
            model_name='likespublications',
            old_name='id_pub',
            new_name='id_posts',
        ),
    ]
