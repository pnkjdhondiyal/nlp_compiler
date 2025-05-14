from flask import Flask, request, jsonify, send_from_directory
import os

# Your existing imports...
from nlp_processing import parser
from code_generator import python_generator
from compiler import llvm_compiler

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/compile', methods=['POST'])
def compile():
    data = request.get_json()
    instruction = data.get("instruction", "")
    
    info = parser.extract_info(instruction)
    code = python_generator.generate_python_code(info["operation"], info["variables"])
    output = llvm_compiler.compile_and_run(code, lang="python")
    
    return jsonify({"code": code, "output": output})

if __name__ == '__main__':
    app.run(debug=True)
