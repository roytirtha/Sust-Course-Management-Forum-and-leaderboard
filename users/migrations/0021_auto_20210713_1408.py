# Generated by Django 3.1.5 on 2021-07-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20210713_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='uploaded_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
