# Generated by Django 3.0.5 on 2020-05-24 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200525_0248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor', old_name='Email', new_name='Department',
        ),
        migrations.RemoveField(model_name='doctor', name='Speciality',),
        migrations.AddField(
            model_name='doctor',
            name='attendance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.IntegerField(
                choices=[(1, 'Active'), (0, 'Not_Active')], default=1
            ),
        ),
    ]
