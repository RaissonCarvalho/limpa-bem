# Generated by Django 4.1.7 on 2023-02-18 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0003_alter_call_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='calls.client'),
        ),
    ]
