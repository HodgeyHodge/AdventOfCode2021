from functools import reduce

def binify(string):
    return "".join(str("{0:04b}".format(int(digit, 16))) for digit in string)

def hexify(string):
    return "".join(str("{:01X}".format(int(string[i:i+4], 2))) for i in range(0, len(string), 4))

def parse(string, n):
    tree = []
    remainder = ''
    for i in range(0, n):
        if '1' not in string:
            break
        packet_version = int(string[0:3], 2)
        packet_type = int(string[3:6], 2)
        if packet_type == 4:
            content = ''
            pos = 6
            while True:
                content += string[pos+1:pos+5]
                if string[pos] == '0':
                    break
                pos +=5
            remainder = string[pos+5:]
            tree.append((packet_version, packet_type, -1, int(content, 2), []))
            string = remainder
        else:
            packet_subtype = int(string[6])
            if packet_subtype == 0:
                length = int(string[7:22], 2)
                content = string[22:22+length]
                remainder = string[22+length:]
                subtree, _ = parse(content, 9999)
                tree.append((packet_version, packet_type, packet_subtype, '', subtree))
                string = remainder
            else:
                children = int(string[7:18], 2)
                content = string[18:]
                subtree, remainder = parse(content, children)
                tree.append((packet_version, packet_type, packet_subtype, '', subtree))
                string = remainder
    return tree, string
    
def sum_version_numbers(tree):
    return sum(node[0] + sum_version_numbers(node[4]) for node in tree)

def calculate_value(node):
    if node[1] == 0:
        return sum(calculate_value(subnode) for subnode in node[4])
    if node[1] == 1:
        return reduce(lambda x, y: x * y, (calculate_value(subnode) for subnode in node[4]))
    elif node[1] == 2:
        return min(calculate_value(subnode) for subnode in node[4])
    elif node[1] == 3:
        return max(calculate_value(subnode) for subnode in node[4])
    elif node[1] == 4:
        return node[3]
    elif node[1] == 5:
        return 1 if calculate_value(node[4][0]) > calculate_value(node[4][1]) else 0
    elif node[1] == 6:
        return 1 if calculate_value(node[4][0]) < calculate_value(node[4][1]) else 0
    elif node[1] == 7:
        return 1 if calculate_value(node[4][0]) == calculate_value(node[4][1]) else 0
    else:
        return -1



# part one

strings = [
    'D2FE28',
    '38006F45291200',
    '8A004A801A8002F478',
    '620080001611562C8802118E34',
    'C0015000016115A2E0802F182340',
    'A0016C880162017C3686B18A3D4780',
]

with open("input.txt") as file:
    strings.append(file.readline())

for string in strings:
    print(string)
    tree, _ = parse(binify(string), 999)
    print(sum_version_numbers(tree))

# part two

strings = [
    'C200B40A82',
    '04005AC33890',
    '880086C3E88112',
    'CE00C43D881120',
    'D8005AC2A8F0',
    'F600BC2D8F',
    '9C005AC2F8F0',
    '9C0141080250320F1802104A08'
]

with open("input.txt") as file:
    strings.append(file.readline())
    
for string in strings:
    print(string)
    tree, _ = parse(binify(string), 999)
    print(calculate_value(tree[0]))







