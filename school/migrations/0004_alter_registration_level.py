# Generated by Django 5.1.3 on 2025-02-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_registration_level_alter_registration_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='level',
            field=models.CharField(choices=[('Basic (200,000 Naira)', 'Basic (200,000 Naira)'), ('Intensive (300,000 Naira)', 'Intensive (300,000 Naira)'), ('Advanced (400,000 Naira)', 'Advanced (400,000 Naira)')], max_length=50),
        ),
    ]
