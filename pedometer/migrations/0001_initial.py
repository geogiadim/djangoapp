# Generated by Django 3.1.7 on 2021-03-20 04:40

from django.db import migrations, models
import django.utils.timezone
import pedometer.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steps', pedometer.models.IntegerRangeField(default=1)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
