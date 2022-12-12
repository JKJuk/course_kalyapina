from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Person(models.Model):
    M = 'Чоловік'
    F = 'Жінка'
    SEX_CHOICES = [
        (M, M),
        (F, F),
    ]
    last_name = models.CharField(max_length=50, verbose_name='Прізвище')
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    middle_name = models.CharField(max_length=50, verbose_name='По батькові')
    date = models.DateField(verbose_name='Дата народження')
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, verbose_name='Стать')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


class Position(models.Model):
    name_position = models.CharField(max_length=100, verbose_name='Назва посади')
    count_hours_in_week = models.PositiveIntegerField(verbose_name='Кількість годин на тиждень')

    def __str__(self):
        return self.name_position


class Employee(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Людина')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Посада')
    NDS = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], verbose_name='НДС(у %)')
    salary = models.PositiveIntegerField(verbose_name='Заробітня плата')

    def __str__(self):
        return f'{self.person} ({self.position})'
