from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json

from Operaciones import Operacion

app = Flask(__name__)
CORS(app)

Operaciones = []

@app.route('/suma', methods=['POST'])
def suma():
    global Operaciones
    a = int(request.json['a'])
    b = int(request.json['b'])
    resultado = (a + b)
    return jsonify({
        'message': 'success',
        'resultado': resultado
    })

@app.route('/resta', methods=['POST'])
def resta():
    global Operaciones
    a = int(request.json['a'])
    b = int(request.json['b'])
    resultado = (a - b)
    return jsonify({
        'message': 'success',
        'resultado': resultado
    })

@app.route('/multiplicacion', methods=['POST'])
def multiplicacion():
    global Operaciones
    a = int(request.json['a'])
    b = int(request.json['b'])
    resultado = (a * b)
    return jsonify({
        'message': 'success',
        'resultado': resultado
    })

@app.route('/division', methods=['POST'])
def division():
    global Operaciones
    a = int(request.json['a'])
    b = int(request.json['b'])
    resultado = (a / b)
    return jsonify({
        'message': 'success',
        'resultado': resultado
    })

@app.route('/potencia', methods=['POST'])
def potencia():
    global Operaciones
    a = int(request.json['a'])
    b = int(request.json['b'])
    resultado = (a ** b)
    return jsonify({
        'message': 'success',
        'resultado': resultado
    })

@app.route('/raiz', methods=['POST'])
def raiz():
    global Operaciones
    a = int(request.json['a'])
    b = int(request.json['b'])
    resultado = (a**(1/b))
    return jsonify({
        'message': 'success',
        'resultado': resultado
    })

if __name__ == "__main__":
    app.run(threaded=True, port=3000, debug=True)