# Generated by Django 3.2.18 on 2023-03-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_myuser_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_img',
            field=models.ImageField(blank=True, default='login/templates/user_foto.jpg', null=True, upload_to='login/templates/images/'),
        ),
    ]