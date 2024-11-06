source_schedule_saturday = open('schedule_saturday.xml', 'r', encoding ='utf-8')
source_schedule_monday = open('schedule_monday.xml', 'r', encoding ='utf-8')

output_schedule_saturday = open('schedule_saturday.json', 'w', encoding ='utf-8')
output_schedule_monday = open('schedule_monday.json', 'w', encoding ='utf-8')

def is_tag(token): return token[-1] == '>'

def is_closing_tag(token): return token[0] == '/'

def parse_xml_to_json(input_xml, output_json):
    tokens = []
    for line in input_xml:
        tokens += filter(lambda s: s != ' ', line.strip().replace('>', '><').split('<')[1:-1])

    i,depth = 0, 1
    output_json.write('{\n')
    while i < len(tokens):
        if is_closing_tag(tokens[i]):
            depth -= 1
            output_json.write('\t' * depth + '}')
        elif i != len(tokens) - 1 and  is_tag(tokens[i]) and is_tag(tokens[i+1]):
            if not is_closing_tag(tokens[i]): output_json.write('\t' * depth + f'"{tokens[i][:-1]}": ' + '{')
            depth += 1
        else:
            output_json.write('\t' * depth + f'"{tokens[i][:-1]}": "{tokens[i+1].strip()}"')
            i += 2
        output_json.write(',\n' if (i < len(tokens) - 1 and is_closing_tag(tokens[i]) and not is_closing_tag(tokens[i+1])) else '\n')
        i += 1
    output_json.write('}')

parse_xml_to_json(source_schedule_monday, output_schedule_monday)
parse_xml_to_json(source_schedule_saturday, output_schedule_saturday)