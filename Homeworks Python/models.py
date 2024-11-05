from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Filial(models.Model):
    full_address = models.CharField(max_length=255)
    short_address = models.CharField(max_length=32)


class Department(models.Model):
    name = models.CharField(max_length=255)
    floor = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    filial = models.ForeignKey(
        'company.Filial',
        null=True,
        related_name='departments',
        on_delete=models.PROTECT,
    )


class Employee(models.Model):
    full_name = models.CharField(max_length= 64)
    post = models.CharField(max_length=64)
    telephone = models.CharField(max_length=32, null=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(null=True)
    department = models.ForeignKey(
        'company.Department',
        null=True,
        related_name='employees',
        on_delete=models.CASCADE,
    )

Запросы, которые могу выполнить, по итогам урока:

1. Employee.objects.filter(post='Менеджер').count()
Out[48]: 5
2. emp_4_floor = Employee.objects.filter(department__floor=4)

In [51]: for emp in emp_4_floor:
    ...:      print(emp.pk, emp.full_name, emp.post, emp.telephone, emp.birthday, emp.email, emp.department)
    ...:
1 Олег Рябчук Менеджер +7-999-999-99-99 1998-01-16 23123@qweq.ru Department object (1)
2 Алексис Дуарте Рекламщик +7-999-999-89-89 2000-03-12 2dwe23@qweq.ru Department object (1)


3. employees=Employee.objects.filter(Q(department__filial__pk=1) | Q (department__filial__pk=2))

In [55]: for emp in employees:
    ...:     print(emp.pk, emp.full_name, emp.post, emp.telephone, emp.birthday, emp.email, emp.department)
    ...:
1 Олег Рябчук Менеджер +7-999-999-99-99 1998-01-16 23123@qweq.ru Department object (1)
2 Алексис Дуарте Рекламщик +7-999-999-89-89 2000-03-12 2dwe23@qweq.ru Department object (1)
3 Эсекьель Барко Менеджер +7-999-999-89-77 1999-03-29 None Department object (2)
4 Срджан Бабич Босс None 1996-04-22 None Department object (2)
5 Маркиньос Менеджер None None 2dwe23@qwe3q.ru Department object (3)
6 Манфред Угальде Продавец None 2002-05-25 2e23@qweq.ru Department object (3)
7 Шамар Николсон Разработчик None 1997-03-16 None Department object (4)
8 Виллиан Жозе Разработчик +7-999-959-89-89 None 2dwe2@qweq.ru Department object (4)
9 Миенти Абена Системный аналитик None 1994-12-12 None Department object (5)
10 Александр Довбня  Бизнес аналитик +7-999-059-89-89 None 2dwe2@qweq.rsu Department object (5)
11 Антон Зиньковский  Тесттировщик None None None Department object (6)
12 Наиль Умяров Тесттировщик None None None Department object (6)



Запросы, ради которых мне придется погуглить:
1. employees = Employee.objects.filter(department__filial__pk__in=[1, 2])

In [60]: for emp in employees:
    ...:     print(emp.pk, emp.full_name, emp.post, emp.telephone, emp.birthday, emp.email, emp.department)
    ...:
1 Олег Рябчук Менеджер +7-999-999-99-99 1998-01-16 23123@qweq.ru Department object (1)
2 Алексис Дуарте Рекламщик +7-999-999-89-89 2000-03-12 2dwe23@qweq.ru Department object (1)
3 Эсекьель Барко Менеджер +7-999-999-89-77 1999-03-29 None Department object (2)
4 Срджан Бабич Босс None 1996-04-22 None Department object (2)
5 Маркиньос Менеджер None None 2dwe23@qwe3q.ru Department object (3)
6 Манфред Угальде Продавец None 2002-05-25 2e23@qweq.ru Department object (3)
7 Шамар Николсон Разработчик None 1997-03-16 None Department object (4)
8 Виллиан Жозе Разработчик +7-999-959-89-89 None 2dwe2@qweq.ru Department object (4)
9 Миенти Абена Системный аналитик None 1994-12-12 None Department object (5)
10 Александр Довбня  Бизнес аналитик +7-999-059-89-89 None 2dwe2@qweq.rsu Department object (5)
11 Антон Зиньковский  Тесттировщик None None None Department object (6)
12 Наиль Умяров Тесттировщик None None None Department object (6)


2. employees = Employee.objects.filter(email__isnull=True)

In [69]: for emp in employees:
    ...:     print(emp.full_name)
    ...:
Эсекьель Барко
Срджан Бабич
Шамар Николсон
Миенти Абена
Антон Зиньковский
Наиль Умяров
Михаил Игнатов
Данил Пруцев


3. сделал 2000 год, 1990 не указал, при заполнении таблицы

employees = Employee.objects.filter(birthday__year=2000)

In [72]: for emp in employees:
    ...:     print(emp.full_name)
    ...:
Алексис Дуарте

