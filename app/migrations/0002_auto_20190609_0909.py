# Generated by Django 2.2.1 on 2019-06-09 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classbooknote',
            name='prim',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Примечание'),
        ),
    ]