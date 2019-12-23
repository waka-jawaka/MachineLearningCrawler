# Generated by Django 2.0 on 2018-03-11 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('link', models.URLField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('main_url', models.URLField()),
                ('url_to_crawl', models.URLField()),
                ('domain', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='site',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Site'),
        ),
    ]