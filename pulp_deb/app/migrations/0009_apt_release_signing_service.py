# Generated by Django 2.2.11 on 2020-03-13 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_rename_last_version'),
        ('deb', '0008_debremote_gpgkey'),
    ]

    operations = [
        migrations.CreateModel(
            name='AptReleaseSigningService',
            fields=[
                ('signingservice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.SigningService')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.signingservice',),
        ),
    ]