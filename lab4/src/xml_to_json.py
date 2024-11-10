import re
from enum import Enum

class json_type(Enum):
    OBJECT = 0
    NUM = 1
    BOOL = 2
    STR = 3

class json_num:
    def __init__(self, content):
        self.name = get_tag_name(content[0])
        if '.' in content[1]:
            self.val = float(re.match(re.compile(r'^\s*\d+(.\d+)?\s*$'), content[1]).group(0))
        else:
            self.val = int(re.match(re.compile(r'^\s*\d+(.\d+)?\s*$'), content[1]).group(0))

    def parse(self, depth = 1):
        return '\t' * depth + f'"{self.name}": {self.val}'

class json_bool:
    def __init__(self, content):
        self.name = get_tag_name(content[0])
        self.val = re.match(r'\b(true|false)\b', content[1]).group(0)

    def parse(self, depth = 1):
        return '\t' * depth + f'"{self.name}": {self.val}'

class json_str:
    def __init__(self,tokens):
        self.name = get_tag_name(tokens[0])
        self.val = tokens[1]
    def parse(self, depth = 1):
        return '\t' * depth + f'"{self.name}": "{self.val}"'

class json_array:
    def __init__(self, name, content_array):
        self.name = name
        self.content_array = content_array
    def parse(self, depth = 1):
        #open bracket on appropriate depth
        s = '\t' * depth + f'"{self.name}": [\n'
        for i in range(len(self.content_array)):
            obj = self.content_array[i]
            #parse all terrible nested json-objects
            if isinstance(obj, json_object):
                s += '\t' * (depth+1) + '{\n'
                l = len(obj.content)
                for j in range(l):
                    s += obj.content[j].parse(depth+2)
                    if j < l - 1:
                        s += ',\n'
                s += '\n' + '\t' * (depth+1) + '}'

            elif type(obj) is json_str: s += '\t' * (depth+1) + obj.val

            else: s += '\t' * (depth+1) + str(obj.val)

            if i < len(self.content_array) - 1: s += ','

            s += '\n'

        s += '\t' * depth + ']'
        return s

class json_object:
    def __init__(self, content):
        self.content = []
        self.name = get_tag_name(content[0])
        content = content[1:-1]
        i = 0
        current_content = {}
        #iterate through tags
        while i < len(content):
            #if was found opening tag, searches for appropriate closing tag
            if is_opening_tag(content[i]):
                current_opening_tag = content[i]
                j = i + 1
                while j < len(content):
                    if is_closing_tag(content[j]) and get_tag_name(content[j]) == get_tag_name(current_opening_tag):
                        break
                    j+=1

                #parses construction of type <tag> (some content) </tag>
                cur_tag = get_tag_name(current_opening_tag)
                if cur_tag in current_content:
                    current_content[cur_tag].append(parse_content(content[i:j+1]))
                else:
                    current_content[cur_tag] = [parse_content(content[i:j+1])]
                i = j
            i+=1
        for key in current_content:
            if len(current_content[key]) > 1: self.content.append(json_array(key, current_content[key]))
            else: self.content.append(current_content[key][0])

    def parse(self, depth = 1):
        s = '\t' * depth + f'"{self.name}": ' + '{\n'
        l = len(self.content)
        for i in range(l):
            s += self.content[i].parse(depth + 1)
            if i < l - 1:
                s += ','
            s+='\n'
        s += '\t' * depth + '}'
        return s

def get_content_type(content):
    if len(content) == 3:
        if  content[1] == 'true' or content[1] == 'false': return json_type.BOOL
        #matches EXACTLY one valid int or float in a line
        elif re.match(re.compile(r'^\s*\d+(.\d+)?\s*$'), content[1]): return json_type.NUM
        return json_type.STR
    return json_type.OBJECT

def get_tag_name(tag):
    return re.match(r'</?(.*)>', tag).group(1)

def is_opening_tag(token):
    return is_tag(token) and token[1] != '/'

def is_closing_tag(token):
    return is_tag(token) and token[1] == '/'

def is_tag(tag):
    return tag[0] == '<' and tag[-1] == '>'

def parse_content(content):
    match get_content_type(content):
        case json_type.NUM:
            return json_num(content)
        case json_type.BOOL:
            return json_bool(content)
        case json_type.STR:
            return json_str(content)
        case _:
            return json_object(content)

def split_into_tokens(xml_file):
    return re.findall(r'</?[^<>/]*>|(?!\s)[^<>/]+?(?=\s*</)', xml_file)

def parse_xml_to_json(xml_data) -> str:
    return '{\n' + json_object(split_into_tokens(xml_data)).parse() + '\n}'