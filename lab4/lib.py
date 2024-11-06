import json
import xmltodict

with open("schedule_saturday.xml", encoding="utf-8") as xml_file:
    parsed_xml = xmltodict.parse(xml_file.read())
    json_data = json.dumps(parsed_xml)
    with open("lib_schedule_saturday.json", "w") as json_file:
        json_file.write(json_data)

with open("schedule_monday.xml", encoding="utf-8") as xml_file:
    parsed_xml = xmltodict.parse(xml_file.read())
    json_data = json.dumps(parsed_xml)
    with open("lib_schedule_monday.json", "w") as json_file:
        json_file.write(json_data)