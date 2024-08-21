# Generated by Django 4.2.15 on 2024-08-19 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_template_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='template',
            name='created_by_group',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='template',
            name='created_by_user',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='template',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='template',
            name='modified_by_group',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='template',
            name='modified_by_user',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
