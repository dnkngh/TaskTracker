# Generated by Django 3.2.15 on 2022-09-24 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projectpermission_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.CharField(help_text='project code', max_length=10, verbose_name='project code'),
        ),
    ]
