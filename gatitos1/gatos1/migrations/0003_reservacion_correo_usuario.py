# Generated by Django 5.0 on 2023-12-16 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatos1', '0002_reservacion_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='correo_usuario',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]