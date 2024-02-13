from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/postendpoint', methods=['POST'])
def handle_post():
    # Obtener datos enviados con la solicitud POST
    data = request.get_json()
    
    # Imprimir los datos recibidos en la consola (solo para demostración)
    print(data)
    #dataset = json.loads(data)
    # Imprimir los datos recibidos en la consola (solo para demostración)
    print(data["data"])
    print('*********************')
    print(data["statistics"])

    
    # Responder con un mensaje de confirmación y los datos recibidos
    return jsonify({'message': 'Datos recibidos exitosamente', 'tus_datos': data})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
