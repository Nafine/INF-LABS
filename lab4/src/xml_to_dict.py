import xml.etree.ElementTree as ET
import json
import re

def parse_content(content):
    #check on bool
    bool_reg = re.search(r'(\bfalse\b|\btrue\b)', content)
    if bool_reg:
        return True if bool_reg.group(1) == 'true' else False
    #check for exactly one int or float
    num_reg = re.match(r'^\s*\d+(\.\d+)?\s*$', content)
    if num_reg:
        return float(content) if num_reg.lastindex else int(content)
    #string otherwise
    return content

def xml_to_dict(element):
    #checks on attributes
    if len(element) == 0 and len(element.attrib) == 0:
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