# Generated by Django 5.0.1 on 2024-01-30 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_comment_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
