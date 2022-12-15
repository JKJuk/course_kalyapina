
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),

    path('employee/', views.employee, name='employee'),
    path('employee/edit/<int:id>', views.employee_edit, name='employee_edit'),
    path('employee/delete/<int:id>', views.employee_delete, name='employee_delete'),
    path('employee/add/', views.employee_add, name='employee_add'),

    path('person/', views.person, name='person'),
    path('person/edit/<int:id>', views.person_edit, name='person_edit'),
    path('person/delete/<int:id>', views.person_delete, name='person_delete'),
    path('person/add/', views.person_add, name='person_add'),

    path('position/', views.position, name='position'),
    path('position/edit/<int:id>', views.position_edit, name='position_edit'),
    path('position/delete/<int:id>', views.position_delete, name='position_delete'),
    path('position/add/', views.position_add, name='position_add'),

]
