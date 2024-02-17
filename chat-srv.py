from openai import OpenAI
from flask import Flask, request, jsonify
import json
from flask_cors import CORS 

attentionRole = """
De ahora en adelante tienes el siguiente role:

**Nombre del personaje**: Laura Rodríguez
**Cargo**: Cientifica virtual de datos y analista de cubos de informacion.

**Descripción del personaje**
Laura Rodríguez es una científico de datos virtual, lista para ayudarte a analizar sets de datos, 
proporcionar análisis básicos, investigar el comportamiento de los datos y detectar cualquier dato atípico o que no concuerde con el conjunto proporcionado.

"""


session = []
session.append({"role": "system", "content": attentionRole})

app = Flask(__name__)
CORS(app) 

client = OpenAI()


@app.route('/', methods=['GET'])
def handle_get():
    print('invoked get')
    return "hello world!"
    



@app.route('/postendpoint', methods=['POST'])
def handle_post():
    # Obtener datos enviados con la solicitud POST
    data = request.get_json()

    print(data)

    question = "with the following data: " + json.dumps(data["data"]) +" " + json.dumps(data["question"])
    
    #client = OpenAI()

    session.append({"role": "user", "content": question})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",      
        messages=session
    )

    print(completion.choices[0].message)
    # Responder con un mensaje de confirmación y los datos recibidos
    return jsonify({'answer': str(completion.choices[0].message)})


if __name__ == "__main__":
    app.run(debug=True, port=5000)

