from flask import Blueprint, request, jsonify, render_template
from .rule_ast import create_rule, combine_rules, evaluate_rule, Node

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@main.route('/create_rule', methods=['POST', 'GET'])
def create_rule_route():
    if request.method == 'GET':
        return render_template('create-rule-form.html')
    
    data = request.json
    rule_string = data.get('rule_string')
    
    if not rule_string:
        return jsonify({"error": "rule_string is required."}), 400
    
    try:
        ast = create_rule(rule_string)
        return jsonify({"ast": ast.to_dict()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@main.route('/combine_rules', methods=['POST', 'GET'])
def combine_rules_route():
    if request.method == 'GET':
        return render_template('combine-rules-form.html')
    
    data = request.json
    rules = data.get('rules')
    
    if not rules or not isinstance(rules, list):
        return jsonify({"error": "rules must be a non-empty list."}), 400
    
    try:
        combined_ast = combine_rules(rules)
        return jsonify({"combined_ast": combined_ast.to_dict()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@main.route('/evaluate_rule', methods=['POST', 'GET'])
def evaluate_rule_route():
    if request.method == 'GET':
        return render_template('evaluate-rule-form.html')
    
    data = request.json
    rule_data = data.get('data')
    ast_dict = data.get('ast')

    if not ast_dict or not rule_data:
        return jsonify({"error": "AST and data are required."}), 400

    try:
        result = evaluate_rule(ast_dict, rule_data)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@main.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200