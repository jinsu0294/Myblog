# Generated by Django 2.0.2 on 2018-02-26 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tag'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='blog_posts',
        ),
    ]
