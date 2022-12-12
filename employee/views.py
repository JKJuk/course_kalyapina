from django.shortcuts import render, redirect
from .models import Employee, Position, Person
from .forms import PersonForm, PositionForm, EmployeeForm


def about(request):
    return render(request, 'about.html')


def employee(request):
    employees = Employee.objects.all()
    return render(request, 'employee.html', {'employees': employees})


def employee_edit(request, id):
    instance = Employee.objects.get(id=id)
    form = EmployeeForm(instance=instance)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('employee')
    return render(request, 'edit.html', {'form': form, 'name': 'Форма для змінення працівника'})


def employee_add(request):
    form = EmployeeForm()
    if request.method == 'GET':
        return render(request, 'add.html', {'form': form, 'name': 'Додавання нового працівника'})
    elif request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('employee')


def employee_delete(request, id):
    Employee.objects.get(id=id).delete()
    return redirect('employee')


def person(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


def person_edit(request, id):
    instance = Person.objects.get(id=id)
    form = PersonForm(instance=instance)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('person')
    return render(request, 'edit.html', {'form': form, 'name': 'Форма для змінення людини'})


def person_delete(request):
    Person.objects.get(id=id).delete()
    return redirect('person')


def person_add(request):
    form = PersonForm()
    if request.method == 'GET':
        return render(request, 'add.html', {'form': form, 'name': 'Додавання нової людини'})
    elif request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('person')


def position(request):
    positions = Position.objects.all()
    return render(request, 'positions.html', {'positions': positions})


def position_edit(request, id):
    instance = Position.objects.get(id=id)
    form = PositionForm(instance=instance)
    if request.method == 'POST':
        form = PositionForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('position')
    return render(request, 'edit.html', {'form': form, 'name': 'Форма для змінення посади'})


def position_delete(request):
    Position.objects.get(id=id).delete()
    return redirect('position')


def position_add(request):
    form = PositionForm()
    if request.method == 'GET':
        return render(request, 'add.html', {'form': form, 'name': 'Додавання нової посади'})
    elif request.method == 'POST':
        form = PositionForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('position')
