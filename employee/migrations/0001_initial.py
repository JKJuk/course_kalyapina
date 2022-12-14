# Generated by Django 4.0.2 on 2022-12-02 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_position', models.CharField(max_length=100)),
                ('count_hours_in_week', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NDS', models.FloatField()),
                ('salary', models.PositiveIntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.person')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.position')),
            ],
        ),
    ]
