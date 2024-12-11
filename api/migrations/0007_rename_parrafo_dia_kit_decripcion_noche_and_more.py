# Generated by Django 5.1.3 on 2024-12-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_kit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kit',
            old_name='parrafo_dia',
            new_name='decripcion_noche',
        ),
        migrations.RenameField(
            model_name='kit',
            old_name='parrafo_noche',
            new_name='descripcion_dia',
        ),
        migrations.AddField(
            model_name='kit',
            name='beneficios',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='kit',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]