from utils.serializers import JsonableMixin, XmlableMixin


class Panda(JsonableMixin, XmlableMixin):

    def __init__(self, name, age=23, alive=True):
        self.name = name
        self.age = age
        self.alive = alive

    def __eq__(self, other):
        return self.name == other.name


class Person(JsonableMixin, XmlableMixin):
    def __init__(self, name):
        self.__init__name = name

    def __eq__(self, other):
        return self.name == other.name


p = Panda(name='Ivo')
json_str = p.to_json()
xml_str = p.to_xml()

p1 = Panda.from_json(json_str)
p2 = Panda.from_xml(xml_str)

print(p1.name)
print(p2.name)
print(p.to_json())
print(p.to_xml())

person = Person(name='Rado')
print(Panda.from_json(person.to_json()))
