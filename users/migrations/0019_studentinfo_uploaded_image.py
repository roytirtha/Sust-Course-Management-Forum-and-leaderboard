# Generated by Django 3.1.5 on 2021-07-13 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_teacherinfo_role_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='uploaded_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
