# Generated by Django 5.2.4 on 2025-07-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_options_blogpost_gist_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='last_fetched',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
