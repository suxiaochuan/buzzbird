# Generated by Django 2.2.3 on 2019-07-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190702_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='media_url',
            field=models.URLField(max_length=1024, null=True),
        ),
    ]
