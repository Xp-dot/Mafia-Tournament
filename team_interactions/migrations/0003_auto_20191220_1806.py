# Generated by Django 3.0 on 2019-12-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_interactions', '0002_contract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='league',
            field=models.CharField(choices=[(1, 'Высшая лига'), (2, 'Вторая лига'), (3, 'Третья лига')], max_length=20, unique=True),
        ),
    ]