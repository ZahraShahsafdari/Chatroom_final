# Generated by Django 2.2.7 on 2019-11-28 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20191124_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
