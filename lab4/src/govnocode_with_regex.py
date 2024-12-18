import re
def is_tag(token): return token[-1] == '>'

def is_closing_tag(token): return token[0] == '/'

def parse_xml_to_json(xml_data) -> str:
    tokens = []
    #1 - find all tags and subs < i.e. <tag>123</tag> -> [tag>, 123, /tag>]
    #2 - find all content between two tags
    for line in xml_data.splitlines():
        tokens += re.findall(r'(?!<)/?[^<>/]*>|(?!>)\b[^<>/]+(?!<)', line)
    i,depth = 0, 1
    s = '{\n'
    while i < len(tokens):
        if is_closing_tag(tokens[i]):
            depth -= 1
            s += '\t' * depth + '}'
        elif i != len(tokens) - 1 and  is_tag(tokens[i]) and is_tag(tokens[i+1]):
            if not is_closing_tag(tokens[i]): s+='\t' * depth + f'"{tokens[i][:-1]}": ' + '{'
            depth += 1
        else:
            s += '\t' * depth + f'"{tokens[i][:-1]}": "{tokens[i+1].strip()}"'
            i += 2
        s += ',\n' if (i < len(tokens) - 1 and is_closing_tag(tokens[i]) and not is_closing_tag(tokens[i+1])) else '\n'
        i += 1
    return s+ '}'