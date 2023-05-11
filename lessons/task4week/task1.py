# Задание 1
"""
class MyObject:
    def __init__(self):
        self.field1 = 1
        self.field2 = "hello"
        self._field3 = [1, 2, 3]


obj = MyObject()
dir_list = dir(obj)
field_names = [name for name in dir_list if not name.startswith("__")]
print(field_names)
"""


# Задание 2

class MyClass:
    def __init__(self):
        self.field = 0

    def my_method(self, arg):
        self.field += arg
        return self.field


obj = MyClass()
method_name = "my_method"
method = getattr(obj, method_name)
result = method(10)
print(result)
print(obj.field)
