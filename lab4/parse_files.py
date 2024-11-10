from idlelib.iomenu import encoding

import govnocode
import govnocode_with_regex
import lib
import xml_to_dict
import xml_to_json
import sys

def get_algo(num):
    match num:
        case 1: return govnocode.parse_xml_to_json
        case 2: return lib.parse_xml_to_json
        case 3: return govnocode_with_regex.parse_xml_to_json
        case 4: return xml_to_dict.parse_xml_to_json
        case 5: return xml_to_json.parse_xml_to_json

while True:
    print("Which algorithm do you want to use?\n\ngovnocode: 1\nlib: 2\ngovnocode_with_regex: 3\nformal_grammar: 4\nmy_algo: 5")
    print("Type corresponding number or \"exit\" to exit")

    a = input()

    if a == 'exit':
        sys.exit()
    elif a not in '12345':
        print("No no no, type number from 1 to 5")
        continue

    algo = get_algo(int(a))

    for file in open('tables.txt', 'r').read().splitlines():
        source = open('source/' + file + '.xml', 'r', encoding='utf-8')
        out = open('out/' + file + '.json', 'w', encoding='utf-8')
        out.write(algo(source.read()))
        print('Parsed ' + file)

    if algo == lib.parse_xml_to_json or algo == xml_to_dict.parse_xml_to_json:
        for file in open('additional_tables.txt', 'r', encoding='utf-8').read().splitlines():
            source = open('source/' + file + '.xml', 'r', encoding='utf-8')
            out = open('out/' + file + '.json', 'w', encoding='utf-8')
            out.write(algo(source.read()))
            print('Parsed ' + file)
    print("Parsing finished\n")