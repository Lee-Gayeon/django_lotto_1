# Generated by Django 2.2.6 on 2019-11-11 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuessNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('lottos', models.CharField(default='[1, 2, 3, 4, 5, 6]', max_length=255)),
                ('num_lotto', models.IntegerField(default=5)),
                ('update_date', models.DateTimeField()),
            ],
        ),
    ]
