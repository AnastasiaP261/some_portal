# Generated by Django 3.2.8 on 2021-10-23 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211023_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentnews',
            old_name='id_new',
            new_name='id_post',
        ),
        migrations.RenameField(
            model_name='commentpublication',
            old_name='id_pub',
            new_name='id_post',
        ),
    ]
