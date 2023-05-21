from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

API_URL = 'https://flask-production-6776.up.railway.app/'  # Cambia esto con la URL de tu API

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    response = requests.get(f'{API_URL}/productos')
    productos = response.json()
    return render_template('productos.html', productos=productos)

@app.route('/clientes')
def clientes():
    response = requests.get(f'{API_URL}/clientes')
    clientes = response.json()
    return render_template('clientes.html', clientes=clientes)

@app.route('/ordenes')
def ordenes():
    response = requests.get(f'{API_URL}/ordenes')
    ordenes = response.json()
    return render_template('ordenes.html', ordenes=ordenes)

@app.route('/productos-orden', methods=['GET', 'POST'])
def productos_orden():
    if request.method == 'POST':
        data = {
            'producto_id': request.form.get('producto_id'),
            'orden_id': request.form.get('orden_id'),
            'cantidad': request.form.get('cantidad')
        }
        response = requests.post(f'{API_URL}/productos-orden', json=data)
        if response.status_code == 201:
            message = 'ProductoOrden creado exitosamente'
        else:
            message = 'Error al crear ProductoOrden'
        return render_template('producto_orden.html', message=message)
    else:
        response = requests.get(f'{API_URL}/productos-orden')
        productos_orden = response.json()
        return render_template('producto_orden.html', productos_orden=productos_orden)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
