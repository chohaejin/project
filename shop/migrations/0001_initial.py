# Generated by Django 4.0.5 on 2022-06-14 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('about', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='shop/images/')),
            ],
        ),
    ]
