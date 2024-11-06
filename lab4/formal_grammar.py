from xml_to_json import parse_xml_to_json

files = ['schedule_monday.xml', 'schedule_saturday.xml', 'test1.xml', 'test2.xml', 'test3.xml']

for file in files:
    with open(file, 'r', encoding = 'utf-8') as f:
        out = open(file.replace('.xml', '.json'), 'w', encoding='utf-8')
        out.write(parse_xml_to_json(f))