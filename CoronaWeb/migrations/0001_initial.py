# Generated by Django 2.2.7 on 2020-04-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brief', models.TextField()),
                ('caused', models.TextField()),
                ('spread', models.TextField()),
                ('danger', models.TextField()),
            ],
        ),
    ]
