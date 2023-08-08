from method import Method


class List(Method):

    def __int__(self, obj: list):
        self._obj = list(obj)

    def length(self) -> int:
        count = 0
        for _ in self._obj: count += 1
        return count

    def is_include(self, find_obj: object) -> bool:
        for item in self._obj:
            if item == find_obj:
                return True
        return False

    def add(self, new_item: object) -> None:
        self._obj.append(new_item)

    def __str__(self):
        return list(self._obj).__str__()
