# Generated by Django 3.0 on 2019-12-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_interactions', '0003_auto_20191220_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Рассматривается'), (2, 'Принят'), (3, 'Отклонен'), (4, 'Изменен'), (5, 'Расторгнут')], default=1),
        ),
        migrations.AlterField(
            model_name='team',
            name='league',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Высшая лига'), (2, 'Вторая лига'), (3, 'Третья лига')], default=3),
        ),
    ]
