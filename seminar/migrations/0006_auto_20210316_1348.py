# Generated by Django 3.1.1 on 2021-03-16 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seminar', '0005_auto_20210316_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminarcustomer',
            name='backup_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='BackupUser',
        ),
    ]
