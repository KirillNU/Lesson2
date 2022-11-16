#(МОДУЛЬ 1) variables.py

'''
1. Создать новый проект
- В проекте создать новый модуль variables.py
- Выбрать объект для описания из списка: овощ, еда, сотрудник, игрушка (так же можно придумать свой)
- Объявить переменные основных типов данных для описания этого объекта:
- В конце модуля с помощью функции type вывести тип для каждой из объявленных переменных
'''

# Define variables
obj_name = 'Кирилл Баранник'
obj_age = 12
obj_class  = 6
is_grade_prime = True
obj_average_score = 13.5

print('Имя ученика: ', obj_name, ' \n', type(obj_name), '\n',
      'Возраст: ', obj_age, '\n', type(obj_age), '\n',
      'Учебный класс:', obj_class, '\n', type(obj_class), '\n'
      'Отличник: ', is_grade_prime, '\n', type(is_grade_prime), '\n'
      'Средний бал: ', obj_average_score, '\n', type(obj_average_score))

