# Generated by Django 3.2.4 on 2022-08-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADDDATA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Number', models.CharField(blank=True, max_length=100, null=True)),
                ('Location', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]