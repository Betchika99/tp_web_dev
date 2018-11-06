# Generated by Django 2.1.3 on 2018-11-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20181104_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата написания'),
        ),
        migrations.AlterField(
            model_name='question',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=70, unique=True, verbose_name='Заголовок ярлыка'),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время регистрации'),
        ),
    ]