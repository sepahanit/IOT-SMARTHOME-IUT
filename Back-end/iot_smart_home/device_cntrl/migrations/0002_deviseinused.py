# Generated by Django 3.2.7 on 2021-12-18 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_cntrl', '0003_remove_house_devices'),
        ('device_cntrl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviseInUsed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn_on_time', models.TimeField(blank=True, null=True)),
                ('turn_off_time', models.TimeField(blank=True, null=True)),
                ('volume', models.CharField(default='NOT SET', max_length=8)),
                ('state', models.CharField(default='NOT SET', max_length=8)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device_cntrl.device')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_cntrl.house')),
            ],
        ),
    ]
