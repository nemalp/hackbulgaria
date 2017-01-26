from datetime import datetime
from fields import Field, EmailField, CharField, DateTimeField
import json


class SerializerMeta(type):

    def __new__(cls, name, bases, clsdict):
        fields = {}

        for attr, value in clsdict.items():
            if isinstance(value, Field):
                fields[attr] = value

        for attr, _ in fields.items():
            clsdict.pop(attr)

        clsdict['_fields'] = fields

        return super().__new__(cls, name, bases, clsdict)


class Serializer(metaclass=SerializerMeta):

    def __init__(self, instance):
        self._obj = instance
        self._called_validation = False

    def is_valid(self):
        valid = True

        for field_name, field in self._fields.items():
            if not field.validate(getattr(self._obj, field_name)):
                valid = False
                break

        self._called_validation = True
        return valid

    @property
    def data(self):
        if not self._called_validation:
            raise Exception('.is_valid() must be called before .data')

        return json.dumps({field_name: field.transform(
            getattr(self._obj, field_name))
                    for field_name, field in self._fields.items()}, indent=4)


class Comment(object):

    def __init__(self, email, content, created_at=None):
        self.email = email
        self.content = content

        if created_at is None:
            created_at = datetime.now()

        self.created_at = created_at


class CommentSerializer(Serializer):
    email = EmailField()
    content = CharField()
    created_at = DateTimeField()


comment = Comment(email='radorado@hakbulgaria.com',
                  content='wie naistina li hakvate?')
serializer = CommentSerializer(comment)

# print(serializer.is_valid())
# print(serializer.data)
