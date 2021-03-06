# Generated by Django 3.1.7 on 2021-02-28 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210227_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.departmentinformation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='first_name',
            field=models.CharField(default='oleg', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_head',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(default='kuz', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='office',
            field=models.CharField(default=54, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='patronymic',
            field=models.CharField(default='da', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='phone_number',
            field=models.CharField(default=34, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='position',
            field=models.CharField(default='Сотрудник', max_length=30),
        ),
    ]
