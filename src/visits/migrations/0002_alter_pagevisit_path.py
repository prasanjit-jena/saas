# Generated by Django 4.2.13 on 2024-07-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagevisit',
            name='path',
            field=models.TextField(blank=True, null=True),
        ),
    ]
