import sys
import json
# from pprint import pprint


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    return data


def get_languages(data):
    languages = set()

    for person in data:
        for lang in person['skills']:
            languages.add(lang['name'])

    return languages


def get_key(item):
    return item[1]


def main():
    data = read_json(sys.argv[1])
    languages = get_languages(data['people'])
    result = {}

    for lang in languages:
        for person in data['people']:
            for skill in person['skills']:
                if skill['name'] == lang:
                    if lang in result:
                        result[lang].append([person['first_name'] + ' ' +
                                             person['last_name'],
                                             skill['level']])

                    else:
                        result[lang] = [[person['first_name'] + ' ' +
                                        person['last_name'], skill['level']]]

    for lang in result:
        print(lang + ' - ' +
              sorted(result[lang], key=get_key, reverse=True)[0][0])


if __name__ == '__main__':
    main()
