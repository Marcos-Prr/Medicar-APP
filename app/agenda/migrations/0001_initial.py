# Generated by Django 3.2.2 on 2021-05-15 20:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(default=django.utils.timezone.now)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico.medico')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('marcado', models.BooleanField(default=False)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='agenda.agenda')),
            ],
        ),
    ]
