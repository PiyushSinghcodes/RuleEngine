import operator

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type
        self.left = left
        self.right = right
        self.value = value

    def to_dict(self):
        return {
            'type': self.type,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None,
            'value': self.value
        }

    @classmethod
    def from_dict(cls, data):
        node = cls(data['type'], value=data['value'])
        if data['left']:
            node.left = cls.from_dict(data['left'])
        if data['right']:
            node.right = cls.from_dict(data['right'])
        return node

def parse_rule_string(rule_string):
    rule_string = rule_string.replace("'", "\"")  # Ensure double quotes for JSON compatibility

    if " AND " in rule_string:
        parts = rule_string.split(" AND ")
        left = parse_rule_string(parts[0].strip())
        right = parse_rule_string(" AND ".join(parts[1:]).strip())
        return Node("operator", left=left, right=right, value="AND")
    elif " OR " in rule_string:
        parts = rule_string.split(" OR ")
        left = parse_rule_string(parts[0].strip())
        right = parse_rule_string(" OR ".join(parts[1:]).strip())
        return Node("operator", left=left, right=right, value="OR")
    else:
        return Node("operand", value=rule_string.strip())

def create_rule(rule_string):
    return parse_rule_string(rule_string)

def combine_rules(rules):
    if not rules:
        return None
    combined_node = create_rule(rules[0])
    for rule in rules[1:]:
        combined_node = Node("operator", left=combined_node, right=create_rule(rule), value="OR")
    return combined_node

OPERATORS = {
    '>': operator.gt,
    '<': operator.lt,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '<=': operator.le,
    'IN': lambda x, y: x in y,
    'NOT IN': lambda x, y: x not in y
}

def evaluate_rule(ast, data):
    if ast['type'] == "operand":
        parts = ast['value'].split()
        if len(parts) < 3:
            raise ValueError(f"Invalid operand format: {ast['value']}")
        
        left = parts[0]
        operator_str = parts[1]
        right = " ".join(parts[2:])
        
        left_value = data.get(left)
        
        # Check if right is a numeric value, boolean, or a field in data
        if right.lower() == 'true':
            right_value = True
        elif right.lower() == 'false':
            right_value = False
        elif right.replace('.', '').isdigit():
            right_value = float(right)
        else:
            right_value = data.get(right, right)  # Use the string value if not found in data
        
        # Handle unknown values
        if left_value is None:
            raise ValueError(f"Unknown field: {left}")
        
        op = OPERATORS.get(operator_str)
        if op:
            return op(left_value, right_value)
        else:
            raise ValueError(f"Unknown operator: {operator_str}")
    
    elif ast['type'] == "operator":
        left_result = evaluate_rule(ast['left'], data)
        right_result = evaluate_rule(ast['right'], data)
        
        if ast['value'] == "AND":
            return left_result and right_result
        elif ast['value'] == "OR":
            return left_result or right_result
    
    return False

