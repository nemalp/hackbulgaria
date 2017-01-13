import json
import xml.etree.ElementTree as ET


class JsonableMixin:

    def to_json(self):
        data = {
            'dict': self.__dict__,
            'classname': self.__class__.__name__
        }

        return json.dumps(data, indent=4)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        classname = data.get('classname', None)

        if cls.__name__ != classname:
            raise ValueError('{} != {}'.format(classname, cls.__name__))

        return cls(**data['dict'])


class XmlableMixin:
    types = {
        t.__name__: t
        for t in (str, int, float, bool)
    }

    def to_xml(self):
        root = ET.Element(self.__class__.__name__)

        for k, v in self.__dict__.items():
            el = ET.SubElement(root, k, {'type': type(v).__name__})
            el.text = str(v)

        return ET.tostring(root)

    @classmethod
    def from_xml(cls, xml_str):
        root = ET.fromstring(xml_str)

        if root.tag != cls.__name__:
            raise ValueError('{} != {}'.format(root.tag, cls))

        data = {}

        for child in root:
            type_name = child.get('type', 'str')
            type_ = cls.types.get(type_name, str)
            data[child.tag] = type_(child.text)

        return cls(**data)
