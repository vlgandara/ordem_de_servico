# Generated by Django 2.0.13 on 2019-06-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordem_de_servico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipamento', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
