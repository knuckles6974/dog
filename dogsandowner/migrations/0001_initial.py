# Generated by Django 4.0.1 on 2022-06-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dog', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'owners',
            },
        ),
    ]
