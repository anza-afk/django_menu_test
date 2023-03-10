# Generated by Django 4.1.7 on 2023-02-21 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_alter_menu_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='url',
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('menu', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu_app.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu_app.menuitem')),
            ],
        ),
    ]
