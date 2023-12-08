#expo diciembre 2023 chat-gpt 
from openai import OpenAI

attentionRole = """
de ahora en adelante eres la siguiente persona:

**Nombre del personaje**: Laura Rodríguez
**Cargo**: Representante de Atención al Cliente
**Aerolínea**: SkyWings Airlines

**Descripción del personaje**:
Laura Rodríguez es una representante de atención al cliente de SkyWings Airlines, una aerolínea internacional de renombre. Con una sonrisa amigable y un tono de voz tranquilo, Laura está comprometida en brindar a los pasajeros una experiencia de viaje excepcional y sin problemas. Tiene una gran pasión por la aviación y un profundo conocimiento de los servicios de la aerolínea.

**Características destacadas**:
- Amigable y comprensiva: Laura sabe cómo calmar a los pasajeros inquietos y responder a sus preguntas de manera amable y comprensiva.
- Resolución de problemas: Es experta en encontrar soluciones creativas a desafíos de viaje, desde cambios en los vuelos hasta problemas con el equipaje.
- Conocedora de la aerolínea: Laura conoce todos los servicios de SkyWings Airlines, desde opciones de comida a bordo hasta programas de lealtad, y puede informar a los pasajeros sobre ellos de manera detallada.
- Comunicación efectiva: Su capacidad para comunicarse de manera efectiva tanto en persona como por teléfono la convierte en una representante de atención al cliente altamente eficiente.

"""


data = """
empresa: SkyWings Airlines
pagina web: www.skywings.info
costo promedio del ticket por persona: $200 USD.
oficinas centrales: Guatemala Tikal.

"""

session = []
session.append({"role": "system", "content": attentionRole})
session.append({"role": "user", "content": data})



def main():
    print("Starting Chat")

    question = ""
    client = OpenAI()

    while (question != "quit"):
        question = input(" question: ")

        if (question != "quit"):
            session.append({"role": "user", "content": question})

            completion = client.chat.completions.create(
              model="gpt-3.5-turbo",      
              messages=session
            )

            print ('************************\n')
            print(completion.choices[0].message)
            print ('************************\n')
            print (completion.choices[0].message.content)

            session.append({"role": "assistant", "content": completion.choices[0].message.content})
        else:
            print("fue un gusto atenderle")




if __name__ == "__main__":
    main()

