# Generated by Django 4.1.2 on 2022-10-22 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feeling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('feeling1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeling1', to='top.feeling')),
                ('feeling2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeling2', to='top.feeling')),
                ('feeling3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeling3', to='top.feeling')),
            ],
        ),
    ]
