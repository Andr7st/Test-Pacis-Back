
# Generated by Django 5.1.3 on 2024-12-05 19:37

# Generated by Django 5.1.3 on 2024-12-05 16:12


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='ingredientes',
            field=models.JSONField(default=list),
        ),
    ]
