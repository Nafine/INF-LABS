import json
import xmltodict

def parse_xml_to_json(xml_data) -> str:
    xml_data = xmltodict.parse(xml_data)
    return json.dumps(xml_data, indent = 4)