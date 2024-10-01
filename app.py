from flask import Flask, request, jsonify, render_template
from lexer import lexer
from parser import parser

app = Flask(__name__)

# Función que realiza el análisis léxico y sintáctico
def analyze_code(code):
    lexer.lineno = 1  # Reiniciar el contador de líneas antes de analizar el código
    lexer.input(code)

    lexical_results = []
    for token in lexer:
        lexical_results.append({
            'line': token.lineno,
            'character': token.value,
            'symbol': token.type
        })

    # Realizamos el análisis sintáctico y atrapamos errores
    syntactic_results = []
    try:
        parser.parse(code)
        syntactic_results.append({
            'line': "Correcto",
            'character': "",
            'symbol': "",
            'structure': "Estructura correcta"
        })
    except Exception as e:
        syntactic_results.append({
            'line': "Error",
            'character': "",
            'symbol': "",
            'structure': str(e)
        })

    return lexical_results, syntactic_results

# Ruta principal para servir la página
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form['code']
    lexical_analysis, syntactic_analysis = analyze_code(code)  # Llama a la función 'analyze_code'
    return jsonify({
        'lexical': lexical_analysis,
        'syntactic': syntactic_analysis
    })

if __name__ == '__main__':
    app.run(debug=True)
