import xml.etree.ElementTree as ET
import json
import re

def parse_content(content):
    #check on bool
    if  re.search(re.compile(r'(\bfalse\b|\btrue\b)'), content):
        return False if re.search(r'false', content) else True
    #check on int or float
    elif re.match(re.compile(r'^\s*\d+(.\d+)?\s*$'), content):
        return float(content) if '.' in content else int(content)
    #string otherwise
    return f'{content}'

def xml_to_dict(element):
    #checks on attributes
    has_attrib = len(element.attrib) != 0
    if len(element) == 0 and not has_attrib:
        return parse_content(element.text)

    #will add attributes if they are exists
    result = {f'@{_}': element.attrib[_] for _ in element.attrib}

    for child in element:
        #if there are many same tags then it's a list
        if child.tag in result:
            #if list already exists
            if isinstance(result[child.tag], list): result[child.tag].append(xml_to_dict(child))
            #otherwise create list
            else: result[child.tag] = [result[child.tag], xml_to_dict(child)]
        #otherwise it's (key: value) object
        else: result[child.tag] = xml_to_dict(child)
    return result

def parse_xml_to_json(xml_data) -> str:
    json_data = ET.fromstring(xml_data)
    return json.dumps(xml_to_dict(json_data), indent = 4)