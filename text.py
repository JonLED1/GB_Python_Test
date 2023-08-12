main_menu = '''\nГлавное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все записи
    4. Добавить запись
    5. Изменить запись
    6. Удалить запись
    7. Выход\n'''

input_choice = 'Выберите пункт меню: '

load_successful = 'Файл успешно открыт!'
save_successful = 'Файл успешно сохранен!'

nb_empty = 'Файл пуст или не загружен!'

input_new_note = 'Введите новую запись: '
def new_note_successful(id):
    return f'Запись №{id} успешно добавлена!'

change_index = 'Введите индекс записи для изменения: '
def change_successful(id):
    return f'Запись №{id} успешно изменена!'
def change_error(id):
    return f'Запись №{id} не найдена!'

del_index = 'Введите индекс записи для удаления: '
def del_successful(id):
    return f'Запись №{id} успешно удалена!'
def del_error(id):
    return f'Запись №{id} не найдена!'
