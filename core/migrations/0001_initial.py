# Generated by Django 2.1.1 on 2018-09-29 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=10, unique=True)),
                ('modelo', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='automovil',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Marca'),
        ),
    ]
