# Generated by Django 2.1.5 on 2019-02-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_mentor', models.CharField(max_length=100)),
                ('images', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
