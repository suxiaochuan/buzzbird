# Generated by Django 2.2.3 on 2019-07-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190718_0531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='media_url',
        ),
        migrations.AddField(
            model_name='member',
            name='weibo_id',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='type',
            field=models.CharField(choices=[('instagram', 'Instagram'), ('twitter', 'Twitter'), ('instagram_v2', 'Instagram V2'), ('weibo', 'Weibo')], max_length=16),
        ),
    ]
