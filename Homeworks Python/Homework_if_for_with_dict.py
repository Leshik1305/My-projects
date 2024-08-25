questions_and_answers = {
    'Какая версия Python сейчас актуальна?': 'Python3',
    'Какая кодировка используется в строках?' : 'UTF8',
    'Сколько значений есть у bool?' : '2',
    'Какой метод создает новую строку с символами в верхнем регистре?' : '.upper()',
    'Сколько байт выделяется в utf-8 для ASCII символов?' : '1',
    'С помощью какого метода можно узнать длину строки?' : '.len()',
    'Какой индекс у "H" в строке "Hello, World"?' : '0',
    'Сколько пробелов в отступе функции?' : '4',
    'Какой объект, который может возвращать свои вложенные объекты по одному?' : 'Итерабельный',
    'Закреплённая стандартом упорядоченная последовательность знаков какой-либо системы письма?' : 'Кодировка'
}
correct_answers=0
incorrect_answers=0
for questions, expected_answers in questions_and_answers.items():
    while True:
        user_answer = input('Введите ответ на вопрос: {0} '.format(questions))
        if user_answer.lower() == expected_answers.lower():
            correct_answers+=1
            print('Правильный ответ')
            break
        else:
            incorrect_answers+=1
            print('Неверный ответ')
total_answers = incorrect_answers + correct_answers
print(f"Количество верных ответов - {correct_answers} \nКоличество неверных ответов - {incorrect_answers} \nОбщее количество ответов - {total_answers}")



