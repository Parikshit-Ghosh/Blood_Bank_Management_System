# Generated by Django 4.0.3 on 2022-04-07 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_state_alter_city_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.state'),
        ),
    ]