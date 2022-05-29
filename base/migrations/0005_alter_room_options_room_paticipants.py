# Generated by Django 4.0.4 on 2022-05-29 16:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_room_host_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='room',
            name='paticipants',
            field=models.ManyToManyField(blank=True, related_name='paticipants', to=settings.AUTH_USER_MODEL),
        ),
    ]