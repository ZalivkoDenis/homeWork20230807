from method import Method


class String(Method):

    def __init__(self, obj: str):
        if type(obj) == str:
            super().__init__(obj)
        else:
            raise ValueError(f'Был передан объект класса: {type(str)}. Объект должен быть <str>.')

    def length(self) -> int:
        count = 0
        for _ in self._obj:
            count += 1
        return count

    def is_include(self, sub_str: str) -> bool:
        c_str: int = String(sub_str).length()
        for index in range(self.length() - c_str):
            if self._obj[index:index + c_str] == sub_str:
                return True
        return False

    def replace(self, old: str, new: str) -> None:
        if not self.is_include(old): return
        c_str = String(old).length()
        for index in range(self.length() - c_str):
            if self._obj[index:index + c_str] == old:
                self._obj = self._obj[0:index] + new + self._obj[index + c_str:self.length()]

    def __str__(self):
        return self._obj
