# Generated by Django 4.2.11 on 2024-03-12 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0004_comment_field_2_comment_field_3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='field_2',
            field=models.IntegerField(default=42),
        ),
    ]
