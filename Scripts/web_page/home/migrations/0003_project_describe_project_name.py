# Generated by Django 4.2.5 on 2023-09-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='describe',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
