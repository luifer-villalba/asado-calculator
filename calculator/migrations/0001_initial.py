# Generated by Django 5.2.1 on 2025-06-05 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AsadoAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('adultos_completa', models.PositiveIntegerField()),
                ('adultos_moderada', models.PositiveIntegerField()),
                ('ninos', models.PositiveIntegerField()),
                ('vegetarianos', models.PositiveIntegerField()),
                ('cortes', models.CharField(blank=True, max_length=255)),
                ('generoso', models.BooleanField(default=False)),
                ('incluir_acompanamientos', models.BooleanField(default=False)),
                ('solo_picada', models.BooleanField(default=False)),
                ('incluir_bebidas', models.BooleanField(default=False)),
                ('resultado', models.JSONField()),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('user_agent', models.TextField(blank=True)),
                ('referer', models.TextField(blank=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
