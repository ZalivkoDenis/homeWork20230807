# ШАГ. Д/з по сроку 07/08/2023 © Денис Заливко

class Method:

    def __init__(self, obj):
        """
        Инициализирует класс
        :param obj: Объект, с которым необходимо работать
        """
        self._obj = obj

    def length(self) -> int:
        """
        Возвращает длину (размерность) объекта
        :return: Длина/размерность объекта класса
        """
        ...

    def is_include(self, find_obj: object) -> bool:
        """
        Проверяет вхождение/членство элемента
        :param find_obj: Элемент, на который проверяется вхождение/членство
        :return: True, если find_obj входит (является членом) объекта класса
        """
        ...


class String(Method):

    def length(self) -> int:
        ...

    def is_include(self, sub_str: str) -> bool:
        ...

    def replace(self, old: str, new: str) -> None:
        ...


class List(Method):

    def length(self) -> int:
        ...

    def is_include(self, find_obj: object) -> bool:
        ...

    def add(self, new_item: object) -> None:
        ...
