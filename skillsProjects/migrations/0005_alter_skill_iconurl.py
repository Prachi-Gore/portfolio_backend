# Generated by Django 5.1.4 on 2025-01-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillsProjects', '0004_alter_skill_iconurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='iconUrl',
            field=models.CharField(max_length=400),
        ),
    ]
