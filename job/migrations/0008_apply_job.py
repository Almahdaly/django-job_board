# Generated by Django 5.1.1 on 2024-10-02 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='job.job'),
            preserve_default=False,
        ),
    ]
