# Generated by Django 3.1.4 on 2021-02-09 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command_1', models.ManyToManyField(related_name='command_1', to='commands.Command', verbose_name='Команда 1')),
                ('command_2', models.ManyToManyField(related_name='command_2', to='commands.Command', verbose_name='Команда 2')),
            ],
        ),
    ]
