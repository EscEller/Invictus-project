# Generated by Django 3.1.7 on 2021-03-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210227_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='mentor',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
