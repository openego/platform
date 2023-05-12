# Generated by Django 3.2.15 on 2023-04-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataedit', '0025_auto_20230427_1403'),
    ]

    operations = [
        migrations.RunSQL('ALTER TABLE dataedit_peerreviewmanager ALTER COLUMN is_open_since TYPE text USING is_open_since::text'),

        migrations.AlterField(
            model_name='peerreviewmanager',
            name='is_open_since',
            field=models.DurationField(null=True),
        ),
    ]