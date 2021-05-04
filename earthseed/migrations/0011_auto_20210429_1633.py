# Generated by Django 3.2 on 2021-04-29 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earthseed', '0010_auto_20210429_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='forum',
        ),
        migrations.AddField(
            model_name='topic',
            name='forum',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='earthseed.forum'),
            preserve_default=False,
        ),
    ]
