# Generated by Django 4.0.3 on 2022-04-04 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('blood_bank_name', models.CharField(max_length=120)),
                ('username', models.CharField(max_length=40, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('contact', models.CharField(default='N/A', max_length=10)),
                ('address', models.CharField(default='N/A', max_length=400)),
                ('roles', models.CharField(default='N/A', max_length=20)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.city')),
            ],
        ),
        migrations.CreateModel(
            name='RBC',
            fields=[
                ('rbc_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_ABpstv', models.IntegerField(default=0)),
                ('quantity_ABngtv', models.IntegerField(default=0)),
                ('quantity_Apstv', models.IntegerField(default=0)),
                ('quantity_Angtv', models.IntegerField(default=0)),
                ('quantity_Bpstv', models.IntegerField(default=0)),
                ('quantity_Bngtv', models.IntegerField(default=0)),
                ('quantity_Opstv', models.IntegerField(default=0)),
                ('quantity_Ongtv', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Platelets',
            fields=[
                ('platelets_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_ABpstv', models.IntegerField(default=0)),
                ('quantity_ABngtv', models.IntegerField(default=0)),
                ('quantity_Apstv', models.IntegerField(default=0)),
                ('quantity_Angtv', models.IntegerField(default=0)),
                ('quantity_Bpstv', models.IntegerField(default=0)),
                ('quantity_Bngtv', models.IntegerField(default=0)),
                ('quantity_Opstv', models.IntegerField(default=0)),
                ('quantity_Ongtv', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Plasma',
            fields=[
                ('plasma_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_ABpstv', models.IntegerField(default=0)),
                ('quantity_ABngtv', models.IntegerField(default=0)),
                ('quantity_Apstv', models.IntegerField(default=0)),
                ('quantity_Angtv', models.IntegerField(default=0)),
                ('quantity_Bpstv', models.IntegerField(default=0)),
                ('quantity_Bngtv', models.IntegerField(default=0)),
                ('quantity_Opstv', models.IntegerField(default=0)),
                ('quantity_Ongtv', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Granulocytes',
            fields=[
                ('granulocytes_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_ABpstv', models.IntegerField(default=0)),
                ('quantity_ABngtv', models.IntegerField(default=0)),
                ('quantity_Apstv', models.IntegerField(default=0)),
                ('quantity_Angtv', models.IntegerField(default=0)),
                ('quantity_Bpstv', models.IntegerField(default=0)),
                ('quantity_Bngtv', models.IntegerField(default=0)),
                ('quantity_Opstv', models.IntegerField(default=0)),
                ('quantity_Ongtv', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='CryoAHF',
            fields=[
                ('cryo_ahf_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity_ABpstv', models.IntegerField(default=0)),
                ('quantity_ABngtv', models.IntegerField(default=0)),
                ('quantity_Apstv', models.IntegerField(default=0)),
                ('quantity_Angtv', models.IntegerField(default=0)),
                ('quantity_Bpstv', models.IntegerField(default=0)),
                ('quantity_Bngtv', models.IntegerField(default=0)),
                ('quantity_Opstv', models.IntegerField(default=0)),
                ('quantity_Ongtv', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
