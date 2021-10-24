# используется для сортировки
from operator import itemgetter


class CDdisk:
    """CD-Диски"""
    def __init__(self, id, type, name, get, lib_id):
        self.id = id
        self.type = type
        self.name = name
        self.get = get
        self.lib_id = lib_id


class Lib:
    """Библиотека CD-дисков"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CDLib:
    """
    'Диски в библиотеке' для реализации
    связи многие-ко-многим
    """
    def __init__(self, CD_id, lib_id):
        self.CD_id = CD_id
        self.lib_id = lib_id


# Библиотеки
libs = [
    Lib(1, 'Библиотека фильмов CD'),
    Lib(2, 'Библиотека игр CD'),
    Lib(3, 'Библиотека мультфильмов CD'),
]

# Диски
cd = [
    CDdisk(1, 'Фильм', 'Мальчишник в Вегасе', 167, 1),
    CDdisk(2, 'Фильм', 'Один дома', 678, 1),
    CDdisk(3, 'Фильм', 'Титаник', 342, 1),
    CDdisk(4, 'Игра', 'Mortal Combat', 113, 2),
    CDdisk(5, 'Игра', 'GTA5', 87, 2),
    CDdisk(6, 'Мультфильм', 'Шрэк', 67, 3),
    CDdisk(7, 'Мультфильм', 'Кот в сапогах', 25, 3),
]

cd_libs = [
    CDLib(1, 1),
    CDLib(2, 1),
    CDLib(3, 1),
    CDLib(4, 2),
    CDLib(5, 2),
    CDLib(6, 3),
    CDLib(7, 3),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(b.type, b.name, b.get, l.name)
                   for l in libs
                   for b in cd
                   if b.lib_id == l.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(l.name, bl.lib_id, bl.CD_id)
                         for l in libs
                         for bl in cd_libs
                         if l.id == bl.lib_id]

    many_to_many = [(b.type, b.name, b.get, lib_name)
                    for lib_name, lib_id, CD_id in many_to_many_temp
                    for b in cd if b.id == CD_id]

    print('Задание Г1')
    res_11 = [(b.type, b.name, l.name)
                for l in libs
                for b in cd
                if (b.lib_id == l.id)&(l.name[:18] == "Библиотека фильмов")]
    print(res_11)

    print('\nЗадание Г2')
    res_12_unsorted = []
    # Перебираем все библиотеки
    for l in libs:
        # Список дисков в библиотеке
        l_cd = list(filter(lambda i: i[3] == l.name, one_to_many))
        # Если библиотека не пустая
        if len(l_cd) > 0:
            # Сколько раз брали диск
            l_get = [get for _, _, get, _ in l_cd]
            # Максимальное число
            l_get_max = max(l_get)
            res_12_unsorted.append((l.name, l_get_max))

    # Сортировка по максимальному числу взятий дисков
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание Г3')
    # Сортировка по имени
    res_14 = sorted(many_to_many, key=itemgetter(1))
    # Сортировка по библиотекам
    res_13 = sorted(res_14, key=itemgetter(3))
    print(res_13)

if __name__ == '__main__':
    main()
