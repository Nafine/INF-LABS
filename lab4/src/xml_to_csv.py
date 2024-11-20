import xml.etree.ElementTree as ET
import csv

def parse_xml_to_csv(xml_data, output_file):
    xml_tree = ET.fromstring(xml_data)

    lessons_table = ['classes']
    atr = [[''] for _ in range(6)]

    lessons = xml_tree.find('classes')

    for lesson in lessons:
        lessons_table.append(lesson.tag)

        for i in range(len(lesson)):
            if len(atr[i]) == 1: atr[i][0] = lesson[i].tag
            atr[i].append(lesson[i].text)
    print([lessons_table, *atr])
    csv.writer(open(output_file, 'w'), delimiter=',', lineterminator='\n').writerows([lessons_table, *atr])

parse_xml_to_csv(open('../input/schedule_monday.xml', 'r').read(), '../output/schedule_monday.csv')
parse_xml_to_csv(open('../input/schedule_saturday.xml', 'r').read(), '../output/schedule_saturday.csv')