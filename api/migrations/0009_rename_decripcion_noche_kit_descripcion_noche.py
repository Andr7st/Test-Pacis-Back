# Generated by Django 5.1.3 on 2024-12-11 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_beneficios_kit_beneficios_dia_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kit',
            old_name='decripcion_noche',
            new_name='descripcion_noche',
        ),
    ]
