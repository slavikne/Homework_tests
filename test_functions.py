from pprint import pprint

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "20006", "name": "Кандрат Иванов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006', '20006'],
    '3': []
}


def output_name(number):
    """
    Выводит имя по номеру документа
    """
    count = 0
    print_string = ''
    while True:
        number_document = number
        for i in documents:
            if i['number'] == number_document:
                # print(i["name"], '\n')
                print_string += f'{i["name"]}'
                count = 1
        if count == 1:
            break
        else:
            print_string += f'Номер документа не найден, повторите ввод'
    print(print_string)
    return print_string


def out_directories(number):
    """
        Выводит номер полки на котором находится документ
    """
    count = 0
    print_string = ''
    while True:
        number_document = number
        for key, value in directories.items():
            if number_document in value:
                # print(f'Документ находится на {key} полке', '\n')
                directorie = key
                print_string += f'Документ находится на {directorie} полке'
                count = 1
        if count == 1:
            break
        else:
            print_string += f'Номер документа не найден, повторите ввод '
    print(directorie)
    return directorie


def output_list_document():
    """
        Выводит список всех документов
    """
    # for i in documents:
    #     for key, value in i.items():
    #         print(value, end=' ')
    #     print()
    pprint(documents)
    return documents


def add_document(type_document, number_document, full_name, directorie):
    """
        Добавляет новый документ
    """
    while True:
        type = type_document
        if type == '':
            print('Некоректный ввод')
        else:
            break
    while True:
        number = number_document
        if number == '':
            print('Некоректный ввод')
        else:
            break
    while True:
        name = full_name
        if name == '':
            print('Некоректный ввод')
        else:
            break
    new_document = {"type": type, "number": number, "name": name}
    while True:
        directories_document = directorie
        if directories_document not in directories:
            print('Такой полки не существует, повторите ввод ')
        else:
            break
    documents.append(new_document)
    directories[directories_document].append(new_document['number'])
    # print('Документ успешно добавлен')
    # pprint(documents)
    # pprint(directories)
    print(documents)
    return new_document


def del_document(number):
    """
        Удаляет документ из каталога
    """
    count = 0
    while True:
        number_document = number
        for i in documents:
            for key, value in i.items():
                if number_document == value:
                    documents.remove(i)
                    for directorie, numbers in directories.items():
                        for j in numbers:
                            if j == number_document:
                                numbers.remove(j)
                    print(f' Документ удален')
                    count = 1
        if count == 1:
            break
        else:
            print('Номер документа не найден, повторите ввод ')
    print(directories)
    print()


def move_document(number, target_directorie):
    """
        Перемещает документ на указанную полку
    """
    count = 0
    while True:
        number_document = number
        number_directories = target_directorie
        for directorie, numbers in directories.items():
            for j in numbers:
                if j == number_document:
                    numbers.remove(j)
                    count = 1
                    for directorie, numbers in directories.items():
                        if number_directories == directorie:
                            numbers.append(number_document)
                            count += 1
        if count == 2:
            print(f'Докумен {number_document} перемещен на {number_directories} полку')
            break
        else:
            print('Номер документа или целевой полки  введен неверно, повторите ввод ')
    print(directories)
    return number


def add_shelf(number_director):
    """
        Добавляет новую полку
    """
    while True:
        directorie = number_director
        if directorie in directories:
            print('Такая полка  существует, повторите ввод ')
        else:
            directories[directorie] = []
            break
    print(directories, '\n')
    return number_director


def main():

    while True:
        user_input = input(
            """people - p 
shelf - s 
list - l, 
add - a 
delete - d
move - m
add shelf - as
quit - q 
Выбирите команду: """)

        if user_input == 'p':
            output_name('10006')
        elif user_input == 's':
            out_directories('2207 876234')
        elif user_input == 'l':
            output_list_document()
        elif user_input == 'a':
            add_document('passport', '123456', 'Иван Дулин', '2')
        elif user_input == 'd':
            del_document('11-2')
        elif user_input == 'm':
            move_document("20006", '3')
        elif user_input == 'as':
            add_shelf('4')
        elif user_input == 'q':
            print('Программа завершена')
            break
        else:
            print('Команда введена неверно')


main()
