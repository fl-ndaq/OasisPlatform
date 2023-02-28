# Generated by Django 3.2.13 on 2022-06-20 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0005_relatedfile_groups'),
        ('analysis_models', '0009_analysismodel_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Name for analysis settings template', max_length=255)),
                ('description', models.CharField(blank=True, default=None, help_text='Description for type of analysis run settings.', max_length=255, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings_template', to=settings.AUTH_USER_MODEL)),
                ('file', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='analysis_settings_template', to='files.relatedfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='analysismodel',
            name='template_files',
            field=models.ManyToManyField(blank=True, related_name='analyses_model_settings_template', to='analysis_models.SettingsTemplate'),
        ),
    ]
